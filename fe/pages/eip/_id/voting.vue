<template>
  <div class="voting-results">
    <div class="vr-header">
      <svg class="vr-header__logo" width="31" height="29" viewBox="0 0 31 29" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M25.9517 18.6481C25.0381 20.225 23.9417 21.3253 22.3338 21.7654C19.2275 22.6455 15.9385 21.6553 14.4767 18.1346C13.1245 14.8706 13.1245 11.4966 14.4767 8.23266C15.4634 5.84885 17.2906 4.49191 19.8853 4.34522C22.48 4.19852 24.4899 5.22539 25.8055 7.49918C25.8421 7.57253 25.9152 7.64587 26.0613 7.86592C26.0613 6.98574 26.0979 6.28894 26.0613 5.55546C26.0248 4.96867 26.2075 4.74863 26.8288 4.74863C27.8155 4.7853 28.8022 4.7853 29.8254 4.74863C30.3005 4.74863 30.4467 4.96867 30.4832 5.40876C30.4832 5.88552 30.337 6.14224 29.8254 6.14224C29.1311 6.14224 28.4002 6.14224 27.6693 6.14224C27.6693 6.47231 27.6693 6.69235 27.6693 6.94907C27.6693 11.7167 27.6693 16.4843 27.6693 21.2519C27.6693 22.9389 27.3404 24.5159 26.2806 25.9095C25.1477 27.4131 23.6129 28.1466 21.8222 28.33C19.3371 28.5867 17.0714 27.9999 15.2076 26.2396C14.6229 25.6895 14.696 25.1027 15.4634 24.8093C15.6461 24.7359 16.0116 24.956 16.1943 25.1394C17.9484 26.753 19.9949 27.2298 22.2972 26.7163C24.3072 26.2762 25.769 24.5892 25.9517 22.4255C26.0248 21.2519 25.9517 20.005 25.9517 18.6481ZM26.1344 13.1103C25.9152 11.9367 25.8055 10.7265 25.4401 9.58959C24.7092 7.20578 22.955 5.84885 20.6527 5.7755C18.4601 5.70215 16.6328 7.02241 15.7923 9.40622C14.9152 12.0101 14.9152 14.6506 15.9385 17.2178C16.7425 19.2715 18.2408 20.4818 20.5066 20.5184C22.8089 20.5551 24.3072 19.3082 25.1843 17.2911C25.8421 16.0075 25.9883 14.5773 26.1344 13.1103Z" fill="black"/>
        <path d="M0 4.96864C0.255812 4.27183 0.803981 4.12514 1.46178 4.23516C2.11959 4.34518 2.48504 4.08846 2.66776 3.42833C2.88703 2.54816 3.25247 1.74133 3.58138 0.861154C3.7641 0.311045 4.16608 0.0176519 4.7508 0.0176519C6.65111 -0.0556961 6.68767 0.0176528 6.68767 1.88803C6.68767 2.65818 6.68767 3.39166 6.68767 4.19848C7.71091 4.19848 8.69761 4.19848 9.68431 4.19848C10.4883 4.19848 10.7441 4.4552 10.7807 5.22536C10.8172 5.70212 10.7807 6.1422 10.7807 6.61897C10.7441 7.20575 10.4518 7.49914 9.86704 7.49914C8.84379 7.49914 7.82055 7.49914 6.72421 7.49914C6.72421 7.75586 6.68767 7.9759 6.68767 8.15928C6.68767 10.6898 6.68767 13.2203 6.72421 15.7508C6.72421 16.1542 6.76075 16.5943 6.87039 16.9977C7.08966 18.0246 7.93018 18.648 9.09961 18.7214C9.5016 18.758 9.94013 18.7214 10.3421 18.758C10.8172 18.7947 11.1096 19.0514 11.1461 19.5649C11.1461 20.1517 11.1461 20.7018 11.1461 21.2886C11.1461 21.7286 10.8903 22.0587 10.4518 22.0587C8.91688 22.022 7.30893 22.0954 5.8106 21.802C3.7641 21.3986 2.48503 19.6382 2.41194 17.5478C2.33886 14.5039 2.33886 11.4233 2.30232 8.37932C2.30232 8.1226 2.30232 7.90255 2.30232 7.57249C1.79069 7.57249 1.3887 7.57249 0.986708 7.57249C0.438539 7.57249 0.146185 7.2791 0.10964 6.72899C0.10964 6.36225 0.0365446 6.03218 0 5.66544C0 5.40873 0 5.18868 0 4.96864Z" fill="black"/>
      </svg>
      <span class="vr-header__logo-text">tennagraph</span>
    </div>

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

    <div v-else-if="votingResults.length && gasvotingStats.length">
      <div class="vr-body">
        <div class="vr-chart-box">
          <div class="vr-chart-box__pie">
            <apexchart height="150" type="donut" :options="chartOptions" :series="votingResults"></apexchart>
          </div>
          <section>
            <div class="vr-chart-box__name">Coinvote</div>
            <div :class="coninvotingStatsMax.class">{{ coninvotingStatsMax.percentage | toFixed2 }}%</div>
            <div class="vr-chart-box__info">
              <div>{{ votingResults.reduce((v, c) => v + c, 0) | toFixed2 }} ETH</div>
              <!--<div>3% of all ETH</div>-->
            </div>
          </section>
        </div>
        <div class="vr-chart-box">
          <div class="vr-chart-box__pie">
            <apexchart height="150" type="donut" :options="chartOptions" :series="gasvotingResults"></apexchart>
          </div>
          <section>
            <div class="vr-chart-box__name">Gasvote</div>
            <div :class="gasvotingStatsMax.class">{{ gasvotingStatsMax.percentage | toFixed2 }}%</div>
            <div class="vr-chart-box__info">
              <div>{{ gasvotingResults.reduce((v, c) => v + c, 0) }} UNITS</div>
              <!--<div>120 Devs voted</div>-->
            </div>
          </section>
        </div>
        <div class="vr-chart-box">
          <div class="vr-chart-box__pie">
            <apexchart height="150" type="donut" :options="chartOptions" :series="stancesResults"></apexchart>
          </div>
          <section>
            <div class="vr-chart-box__name">Influencers</div>
            <div :class="stancesStatsMax.class">{{ stancesStatsMax.percentage | toFixed2 }}%</div>
            <div class="vr-chart-box__info">
              <div>{{ stancesResults.reduce((v, c) => v+c, 0) }} influencer / s</div>
            </div>
          </section>
        </div>
      </div>
      <div class="vr-footer">
        <div class="vr-footer__left">
          <img class="vr-fox" src="/icons/vr-fox.png" alt="">
          <span>Signal your stance</span>
        </div>
        <div class="vr-footer__right">
          <div v-if="isAddingVote" class="vr-loading">
            <pulse-loader></pulse-loader>
          </div>
          <div v-else class="vr-buttons">
            <button class="vr-btn vr-btn--success" :disabled="!votingAddresses" @click="vote(votingAddresses.yay)">Yea</button>
            <button class="vr-btn vr-btn--danger" :disabled="!votingAddresses" @click="vote(votingAddresses.nay)">Nay</button>
            <button class="vr-btn vr-btn--default" :disabled="!votingAddresses" @click="vote(votingAddresses.abstain)">Abstain</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import apexchart from 'vue-apexcharts'
  import commonErrorsMixin from "~/mixins/commonErrorsMixin";

  import votingManagerABI from "~/contracts/VotingManager.json";
  import votingOptionABI from "~/contracts/VotingOption.json";
  import truffleContract from 'truffle-contract'
  import web3Instance from "~/utils/web3Instance.js";
  import PulseLoader from '@/components/PulseLoader.vue';


  export default {
    layout: 'clear',
    components: {
      apexchart,
      PulseLoader,
    },
    mixins: [
      commonErrorsMixin,
    ],

    data() {
      return {
        eipId: this.$route.params.id,
        eip: undefined,
        isEIPLoading: false,

        VotingManagerContract: undefined,
        VotingOptionContract: undefined,
        isProposalExistsInVotingManager: undefined,
        proposalVotingInfo: undefined,
        votingResults: [],
        isAddingProposal: false,
        isAddingVote: false,
        gasvotingResults: [],
        stancesResults: [0, 0, 0],
        stancesStatsMax: {},
        isStancesLoading: false,

        chartOptions: {
          labels: ["Yea", "Nay", "Abstain"],
          colors: ['#45C299', '#F03D3D', '#B1B1B1'],
          legend: {
            show: false,
          },
          stroke: {
            width: 1
          },
          dataLabels: {
            enabled: false
          }
        },
      }
    },

    async created() {
      this.isEIPLoading = true;
      await this.loadStances();
      this.checkNetwork();
      try {
        await this.loadEIP();
        await this.initVotingManager();
        await this.loadEIPGasVoting();

      } catch (e) {
        this.setResponseErrors(e);
      }
    },

    computed: {
      w3() {
        return web3Instance
      },
      votingManagerAddress() {
        return this.$store.getters['app/contractVotingManagerAddress'];
      },
      isVotingActive() {
        if (!this.proposalVotingInfo) return undefined;
        return this.proposalVotingInfo[1];
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
      shouldDisplayCharts() {
        if (this.votingResults.length === 0) return false;
        for(let i=0; i<this.votingResults.length; i++) {
          if (this.votingResults[i] !== 0) {
            return true
          }
        }
        return false
      },
      coninvotingStats() {
        const usedVolume = this.votingResults.reduce((v,c) => v+c, 0);

        return this.votingResults.map((v, i) => ({
          "class": this.classByIndex(i),
          "percentage": 100 * v / usedVolume,
        })).sort((a, b) => b.percentage - a.percentage);
      },
      coninvotingStatsMax() {
        return this.coninvotingStats.length ? this.coninvotingStats[0] : {};
      },
      gasvotingStats() {
        const usedVolume = this.gasvotingResults.reduce((v,c) => v+c, 0);

        return this.gasvotingResults.map((v, i) => ({
          "class": this.classByIndex(i),
          "percentage": 100 * v / usedVolume,
        })).sort((a, b) => b.percentage - a.percentage);
      },
      gasvotingStatsMax() {
        return this.gasvotingStats.length ? this.gasvotingStats[0] : {};
      },
    },

    methods: {
      async loadEIP() {
        // this.isEIPLoading = true;
        // try {
        //   this.eip = await this.$store.dispatch('eip/loadEIP', this.eipId)
        // } catch (e) {
        //   this.setResponseErrors(e);
        // }
        // this.isEIPLoading = false;
      },

      async checkNetwork() {
        try {
          await this.w3.promisify.checkNetwork()
        } catch (e) {

          this.setErrors(e.message)
        }
      },

      initVotingManager() {
        if (!this.w3 && this.votingManagerAddress) return;
        const contract = truffleContract(votingManagerABI);
        contract.setProvider(this.w3.currentProvider);
        this.VotingManagerContract = contract;

        this.loadEIPCoinVotingInfo()
      },
      initVotingOptions() {
        const contract = truffleContract(votingOptionABI);
        contract.setProvider(this.w3.currentProvider);
        this.VotingOptionContract = contract;
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
            // from wai to ether
            this.votingResults.push(parseFloat(el) / parseFloat(1000000000000000000))
          })
        } catch(e) {
          this.setErrors(e.message)
        }
      },
      async loadEIPGasVoting() {
        try {
          let result = await this.$store.dispatch('eip/loadEIPGasVoting', this.eipId);
          this.gasvotingResults.push(result.yay);
          this.gasvotingResults.push(result.nay);
          this.gasvotingResults.push(result.abstain);
        } catch (e) {
          this.setErrors(e.message)
        }
      },
      async loadStances() {
        this.isStancesLoading = true;
        try {
          const stances = await this.$store.dispatch('stance/loadStances', this.eipId)
          const stancesStats = stances.reduce((c, v) => {
            const copyC = {...c};
            const choice = v.choice.key;

            if (choice === "YAY") {
              copyC['yay'] += 1;
            } else if (choice === "NAY") {
              copyC['nay'] += 1;
            } else if (choice === "ABSTAIN") {
              copyC['abstain'] += 1;
            }
            return copyC;
          }, {
            yay: 0,
            nay: 0,
            abstain: 0,
          })

          const stancesResults = [stancesStats.yay, stancesStats.nay, stancesStats.abstain]
          const volume = this.stancesResults.reduce((v,c)=>v+c, 0)
          this.stancesResults = stancesResults;

          if(stancesStats[0] > stancesStats[1] > stancesStats[2]) {
            this.stancesStatsMax = {
              "class": this.classByIndex(0),
              "percentage": volume ? stancesStats[0] / volume : 0
            }
          } else if(stancesStats[1] > stancesStats[0] > stancesStats[1]) {
            this.stancesStatsMax = {
              "class": this.classByIndex(1),
              "percentage": volume ? stancesStats[1] / volume : 0
            }
          } else {
            this.stancesStatsMax = {
              "class": this.classByIndex(2),
              "percentage": volume ? stancesStats[2] / volume : 0
            }
          }

        } catch (e) {
          this.setResponseErrors(e);
        }
        this.isStancesLoading = false;
      },
      async vote(votingAddresses) {
        this.isAddingVote = true;
        try {
          const instance = await this.VotingOptionContract.at(votingAddresses);
          const transactionInfo = await this.w3.promisify.transactionInfo();
          await instance.vote(transactionInfo);

          setTimeout(async () => {
            await this.loadEIPCoinVotingInfo();
            this.isAddingVote = false;
          }, 9000);

        } catch(e) {
          this.setErrors(e.message)
        }
      },
      classByIndex: (i) => {
        if(i === 0) {
          return "vr-chart-box__result"
        } else if (i === 1) {
          return "vr-chart-box__result vr-chart-box__result--red"
        } else if (i === 2) {
          return "vr-chart-box__result vr-chart-box__result--grey"
        }
      },
      async addProposalToVotingManager() {
        try {
          const instance = await this.VotingManagerContract.at(this.votingManagerAddress);
          const transactionInfo = await this.w3.promisify.transactionInfo()
          this.isAddingProposal = true;
          await instance.addProposal(this.eipId, true, transactionInfo);

          setTimeout(async () => {
            await this.loadEIPCoinVotingInfo()
            this.isAddingProposal = false;
          }, 9000);

        } catch(e) {
          this.isAddingProposal = false;
          this.setErrors(e.message)
        }
      },
    },

    watch: {
      w3(newValue) {
        this.initVotingManager(newValue)
      },
      votingManagerAddress(newValue) {
        this.initVotingManager(newValue)
      },
      votingAddresses() {
        this.initVotingOptions()
      },
    }
  }
</script>


<style>
  .application--wrap {
    background-color: #fff;
  }

   .voting-results {
     background-color: #fff;
     padding: 20px 40px;
     width: 100%;
     margin: 0 auto;
     border-radius: 3px;
    /*max-width: 980px;*/
    /*border: 1px solid #d1d5da;*/
    /*margin-top: 40px;*/
  }

  .vr-header {
    display: flex;
    align-items: center;
    font-size: 24px;
    opacity: .3;
    margin-bottom: 30px;
  }

  .vr-header__logo-text {
    display: inline-block;
    margin-left: 10px;
  }

  .vr-body {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
  }

  .vr-chart-box__name {
    font-size: 22px;
    margin-bottom: 10px;
  }

  .vr-chart-box__result {
    font-size: 48px;
    color: #69BE9B;
    line-height: .9;
    margin-bottom: 13px;
    font-weight: 700;
  }

  .vr-chart-box__info {
    font-size: 14px;
    opacity: .5;
  }

  .vr-chart-box__result--red {
    color: #DE4C46;
  }

  .vr-chart-box__result--grey {
    color: #ABABAB;
  }

  .vr-footer__left {
    font-size: 23px;
    font-weight: 300;
    flex: 0 30%;
  }

  .vr-footer {
    display: flex;
    align-items: center;
  }

  .vr-fox {
    display: inline-block;
    vertical-align: middle;
    margin-right: 10px;
  }

  .vr-btn {
    padding: 9px 20px;
    color: #fff;
    font-weight: 700;
    width: 100%;
  }

  .vr-btn--success {
    background-color: #69BE9B;
  }

  .vr-footer__right {
    flex: 0 70%;
  }

  .vr-btn.vr-btn--danger {
    background-color: #DE4C46;
  }

  .vr-btn--default {
    background-color: #ABABAB;
  }

  .vr-buttons {width: 100%;display: flex;justify-content: space-between;}
  .vr-loading {width: 100%;display: flex;justify-content: center; align-items: end;}

  .vr-buttons button + button {
    margin-left: 1px;
  }

  .vr-chart-box__pie {
    width: 100px;
    height: 100px;
  }

  .vr-chart-box {
    display: flex;
  }

  .vr-chart-box section {
    padding-left: 15px;
  }

  @media (max-width: 767.98px) {
    .vr-body {
      flex-direction: column;
      align-items: center;
    }

    .vr-chart-box + .vr-chart-box {
        margin-top: 30px;
    }

    .vr-footer__left {
      width: 100%;
      margin-bottom: 20px;
    }

    .vr-footer {
        flex-direction: column;
    }

    .vr-footer__right {
        width: 100%;
    }

    .vr-buttons {
        flex-direction: column;
    }

    .vr-btn {
      border-radius: 3px;
    }

    .vr-btn + .vr-btn {
        margin-top: 10px;
    }
  }

  @media (min-width: 768px) {
    .vr-btn:first-child {
      border-top-left-radius: 3px;
      border-bottom-left-radius: 3px;
    }

    .vr-btn:last-child {
      border-top-right-radius: 3px;
      border-bottom-right-radius: 3px;
    }
  }

  button:focus {
    outline: 0;
  }
</style>
