<template>
  <v-layout row class="wrapper" wrap>

    <v-flex xs9>
      <v-layout row align-center justify-start>
        <v-flex xs2>
          <span class="text-truncate">Yay</span>
        </v-flex>
        <v-layout align-center fill-height wrap>
          <v-flex xs8>
            <v-text-field placeholder="Placeholder" v-model="yayAddress"></v-text-field>
          </v-flex>
          <v-layout xs1>
            <v-btn icon>
              <v-avatar size="18px" tile>
                <v-img src="/icons/qr_code_mini.svg"></v-img>
              </v-avatar>
            </v-btn>
            <v-btn icon>
              <v-avatar size="18px" tile>
                <v-img src="/icons/chip_link.svg"></v-img>
              </v-avatar>
            </v-btn>
          </v-layout>
        </v-layout>
      </v-layout>

      <v-layout row align-center justify-start>
        <v-flex xs2>
          <span class="text-truncate">Nay</span>
        </v-flex>
        <v-layout align-center fill-height wrap>
          <v-flex xs8>
            <v-text-field placeholder="Placeholder" v-model="yayAddress"></v-text-field>
          </v-flex>
          <v-layout xs1>
            <v-btn icon>
              <v-avatar size="18px" tile>
                <v-img src="/icons/qr_code_mini.svg"></v-img>
              </v-avatar>
            </v-btn>
            <v-btn icon>
              <v-avatar size="18px" tile>
                <v-img src="/icons/chip_link.svg"></v-img>
              </v-avatar>
            </v-btn>
          </v-layout>
        </v-layout>
      </v-layout>

      <v-layout row align-center justify-start>
        <v-flex xs2>
          <span class="text-truncate">Abstain</span>
        </v-flex>
        <v-layout align-center fill-height wrap>
          <v-flex xs8>
            <v-text-field placeholder="Placeholder" v-model="yayAddress"></v-text-field>
          </v-flex>
          <v-layout xs1>
            <v-btn icon>
              <v-avatar size="18px" tile>
                <v-img src="/icons/qr_code_mini.svg"></v-img>
              </v-avatar>
            </v-btn>
            <v-btn icon>
              <v-avatar size="18px" tile>
                <v-img src="/icons/chip_link.svg"></v-img>
              </v-avatar>
            </v-btn>
          </v-layout>
        </v-layout>
      </v-layout>
    </v-flex>

    <v-flex xs3>
      <apexchart type=donut :options="chartOptions" :series="series"/>
    </v-flex>
  </v-layout>
</template>

<script>

  import commonErrorsMixin from "~/mixins/commonErrorsMixin";
  import successAlertsMixin from "~/mixins/successAlertsMixin";
  import VueApexCharts from 'vue-apexcharts'

  export default {
    name: "coinvoting",
    mixins: [
      commonErrorsMixin,
      successAlertsMixin,
    ],
    components: {
      apexchart: VueApexCharts,
    },
    props: {
      eipId: {
        type: [String, Number],
        required: true
      },
    },
    data() {
      return {
        yayAddress: "0x0ca1328ba92c5ad1d51c81bd6c0c458c8cc8a650",
        series: [44, 55, 41],
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
        }
      }
    },
    methods: {
      async loadCoinVotingDetails() {
        // if (!this.$refs.form.validate()) { return; }
        //
        // let data = {
        //   'author':    this.author,
        //   'proof_url': this.link,
        //   'choice':    this.choice,
        //   'eip_id':    this.eipId,
        // };
        // this.isStanceSending = true;
        // try {
        //   await this.$store.dispatch('stance/createStance', data);
        //   this.$refs.form.reset();
        //   this.setSuccessAlerts(["The stance was successfully added on review!"])
        // } catch (e) {
        //   this.setResponseErrors(e, ['author', 'post_url', 'choice']);
        // }
        // this.isStanceSending = false;
      }
    }
  }
</script>

<style scoped>

</style>
