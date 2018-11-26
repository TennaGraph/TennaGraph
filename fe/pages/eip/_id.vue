<template>
  <v-container class="dashboard">
    <v-layout row mt-2>
      <v-flex xs12>
        <v-layout class="d-block" px-2>
          <v-card-title v-if="eip" class="headline mb-4 mt-2 py-0 px-0 primary--text">
            {{ eip.eip_title }}
          </v-card-title>

          <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">
            <v-card-title class="title mb-4 mt-2 py-0 px-0 primary--text">
              Influencer Stances
              <!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->
              <!--<v-btn-toggle v-model="viewType">-->
                <!--<v-btn flat value="0">-->
                  <!--<span>By stance</span>-->
                <!--</v-btn>-->
                <!--<v-btn flat value="1">-->
                  <!--<span>By rank</span>-->
                <!--</v-btn>-->
              <!--</v-btn-toggle>-->
            </v-card-title>
            <activity-chart
              v-if="isStancesLoaded"
              :yayStances="yayStances"
              :nayStances="nayStances"
              :abstainStances="abstainStances">
            </activity-chart>
            <stances-list
              v-if="isStancesLoaded"
              :yayStances="yayStances"
              :nayStances="nayStances"
              :abstainStances="abstainStances">
            </stances-list>
          </v-card>

          <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">
            <v-card-title class="title mb-4 mt-2 py-0 px-0">
              Add a stance
            </v-card-title>
            <add-stance :eipId="eipId"></add-stance>
          </v-card>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

  import AddStance from "~/components/AddStance";
  import commonErrorsMixin from "~/mixins/commonErrorsMixin";
  import ActivityChart from "~/components/ActivityChart";
  import StancesList from "~/components/StancesList";

  export default {
    components: {
      StancesList,
      ActivityChart,
      AddStance
    },
    name: "eip-details",
    mixins: [
      commonErrorsMixin,
    ],
    data() {
      return {
        eip: undefined,
        isEIPLoading: false,
        isStancesLoading: false,
        stances: [],
        eipId: this.$route.params.id,
        viewType: "0",

        yayStances: undefined,
        nayStances: undefined,
        abstainStances: undefined,
      }
    },
    created() {
      this.isEIPLoading = true;
      try {
        this.loadEIP()
        this.loadInfluencers()
        this.loadStances()
      } catch (e) {
        this.setResponseErrors(e);
      }
    },
    methods: {
      async loadEIP() {
        this.isEIPLoading = true;
        try {
          this.eip = await this.$store.dispatch('eip/loadEIP', this.eipId)
        } catch (e) {
          this.setResponseErrors(e);
        }
        this.isEIPLoading = false;
      },

      async loadStances() {
        this.isStancesLoading = true;
        try {
          if (!this.isInfluencersLoaded) {
            await this.$store.dispatch('influencer/loadInfluencers')
          }
          this.stances = await this.$store.dispatch('stance/loadStances', this.eipId)
        } catch (e) {
          this.setResponseErrors(e);
        }
        this.isStancesLoading = false;
      },

      async loadInfluencers() {
        try {
          await this.$store.dispatch('influencer/loadInfluencers')
        } catch (e) {
          this.setResponseErrors(e);
        }
      },

      filterStances(stances, status) {
        return stances.filter(function (stance) {
          return stance.choice.key === status;
        })
      },
    },
    computed: {
      isInfluencersLoaded() {
        return this.$store.getters['influencer/']
      },
      isStancesLoaded() {
        return this.yayStances && this.nayStances && this.abstainStances;
      }
    },
    watch: {
      stances(newValue) {
        this.yayStances = this.filterStances(newValue, 'YAY')
        this.nayStances = this.filterStances(newValue, 'NAY')
        this.abstainStances = this.filterStances(newValue, 'ABSTAIN')
      }
    }
  }
</script>

<style scoped>

</style>
