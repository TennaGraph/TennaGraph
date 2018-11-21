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
            </v-card-title>
            <activity-chart></activity-chart>
            <stances-list></stances-list>
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
        eipId: this.$route.params.id,
      }
    },
    created() {
      this.loadEIP()
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
      }
    }
  }
</script>

<style scoped>

</style>
