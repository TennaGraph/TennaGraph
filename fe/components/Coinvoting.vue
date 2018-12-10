<template>
  <v-layout>

    <v-layout v-if="!isProposalExistsInVotingManager || !proposalVotingInfo">

      <pulse-loader v-if="isProposalExistsInVotingManager == undefined || (!proposalVotingInfo && isProposalExistsInVotingManager == true)"></pulse-loader>
      <v-layout v-else-if="isProposalExistsInVotingManager == false" column>
        <v-flex>
          <p class="px-2">Coinvoting has not been enabled for this EIP. Deploy the SmartContract via meta-mask to begin.</p>
          <p>{{ proposalVotingInfo }}</p>
        </v-flex>
        <v-flex>
          <v-btn dark color="breeze" :loading="isAddingProposal"  @click="addProposalToVotingManager">START COINVOTING</v-btn>
        </v-flex>
      </v-layout>
    </v-layout>

    <v-layout column v-else>
      <p>Active since date {{ votingCreatedAt | formatDateTime }}</p>
      <v-layout row class="wrapper" wrap>
        <v-flex xs9>
          <v-layout row align-center justify-start v-for="decision in decisions" :key="decision.title">
            <v-flex xs2>
              <span class="text-truncate">
                <svg width="20" height="10" viewBox="5 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="5" cy="5" r="5" :fill="decision.color"/>
                </svg>
                {{ decision.title }}
              </span>
            </v-flex>
            <v-layout align-center fill-height wrap>
              <v-flex xs8>
                <v-text-field placeholder="Placeholder" :value="decision.address"></v-text-field>
              </v-flex>
              <v-layout xs1>
                <v-btn icon @click="openQrCode(decision.title, decision.address)">
                  <v-avatar size="18px" tile>
                    <v-img src="/icons/qr_code_mini.svg"></v-img>
                  </v-avatar>
                </v-btn>
                <v-btn icon :href="etherscanUrl(decision.address)" target="_blank">
                  <v-avatar size="18px" tile>
                    <v-img src="/icons/chip_link.svg"></v-img>
                  </v-avatar>
                </v-btn>
              </v-layout>
            </v-layout>
          </v-layout>
        </v-flex>
        <v-flex xs3>
          <apexchart v-if="votingResults.length > 0" type=donut :options="chartOptions" :series="votingResults"/>
        </v-flex>
      </v-layout>
    </v-layout>
  </v-layout>
</template>

<script>

  import commonErrorsMixin from "~/mixins/commonErrorsMixin";
  import successAlertsMixin from "~/mixins/successAlertsMixin";
  import VueApexCharts from 'vue-apexcharts'
  import PulseLoader from '@/components/PulseLoader.vue';

  import votingManagerABI from "~/contracts/VotingManager.json";
  import truffleContract from 'truffle-contract'

  export default {
    name: "coinvoting",
    mixins: [
      commonErrorsMixin,
      successAlertsMixin,
    ],
    components: {
      apexchart: VueApexCharts,
      PulseLoader
    },
    props: {
      eipId: {
        type: [String, Number],
        required: true
      },
      w3: {
        type: Object,
      },
    },
    data() {
      return {
        yayAddress: "0x0ca1328ba92c5ad1d51c81bd6c0c458c8cc8a650",
        chartOptions: {
          labels: ["Yay", "Nay", "Abstain"],
          colors: ['#45C299', '#F03D3D', '#B1B1B1'],
          legend: {
            show: false,
          },
          stroke: {
            width: 2
          },
          dataLabels: {
            enabled: false
          },
        },
        VotingManagerContract: undefined,
        isProposalExistsInVotingManager: undefined,
        proposalVotingInfo: undefined,
        votingResults: [],
        isAddingProposal: false
      }
    },
    created() {
      this.initVotingManager()
    },
    computed: {
      votingManagerAddress() {
        return this.$store.getters['app/contractVotingManagerAddress'];
      },
      isVotingActive() {
        if (!this.proposalVotingInfo) return undefined;
        return this.proposalVotingInfo[1]
      },
      votingCreatedAt() {
        if (!this.proposalVotingInfo) return undefined;
        return new Date(this.proposalVotingInfo[2] * 1000)
      },
      votingAddresses() {
        if (!this.proposalVotingInfo) return undefined;
        return {
          yay: this.proposalVotingInfo[3],
          nay: this.proposalVotingInfo[4],
          abstain: this.proposalVotingInfo[5],
        }
      },
      series() {
        return this.votingResults.map(value => parseInt(value))
      },
      decisions() {
        return [
          {
            title: "Yay",
            address: this.votingAddresses.yay,
            color: "#45C299"
          },
          {
            title: "Nay",
            address: this.votingAddresses.nay,
            color: "#F03D3D"
          },
          {
            title: "Abstain",
            address: this.votingAddresses.abstain,
            color: "#DADADA"
          },
        ]
      }
    },
    methods: {
      initVotingManager() {
        if (!this.w3 && this.votingManagerAddress) return;
        const contract = truffleContract(votingManagerABI);
        contract.setProvider(this.w3.currentProvider);
        this.VotingManagerContract = contract;

        this.loadEIPCoinVotingInfo()
      },
      async loadEIPCoinVotingInfo() {
        try {
          const instance = await this.VotingManagerContract.at(this.votingManagerAddress);
          this.isProposalExistsInVotingManager = await instance.isProposalExists.call(this.eipId);

          if (!this.isProposalExistsInVotingManager) return;
          this.proposalVotingInfo = await instance.proposals.call(this.eipId);
          const res = await instance.votingResults.call(this.eipId);
          this.votingResults.length = 0
          res.forEach(el => {
            this.votingResults.push(parseInt(el))
          })
        } catch(e) {
          this.setErrors(e.message)
        }
      },
      async addProposalToVotingManager() {
        try {
          const instance = await this.VotingManagerContract.at(this.votingManagerAddress);
          const transactionInfo = await this.w3.promisify.transactionInfo()
          this.isAddingProposal = true;
          await instance.addProposal(this.eipId, true, transactionInfo);

          await this.loadEIPCoinVotingInfo()
          this.isAddingProposal = false;
        } catch(e) {
          this.isAddingProposal = false;
          this.setErrors(e.message)
        }
      },
      async openQrCode(option, address) {
        const data = {
          address: address,
          option: option
        }
        await this.$store.dispatch("ui/openQrCodeMenu", data)
      },
      etherscanUrl(address) {
        return process.env.etherscanUrl + "address/" + address
      }
    },
    watch: {
      w3(newValue) {
        this.initVotingManager(newValue)
      },
      votingManagerAddress(newValue) {
        this.initVotingManager(newValue)
      }
    }
  }
</script>

<style scoped>

</style>
