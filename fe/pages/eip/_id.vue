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
          </v-card>

          <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">
            <v-card-title class="title mb-4 mt-2 py-0 px-0">
              Add a stance
            </v-card-title>
            <add-stance></add-stance>
          </v-card>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

  import AddStance from "~/components/AddStance";
  import commonErrorsMixin from "~/mixins/commonErrorsMixin";

  export default {
    components: {AddStance},
    name: "eip-details",
    mixins: [
      commonErrorsMixin,
    ],
    data() {
      return {
        eip: undefined,
        isEIPLoading: false,
      }
    },
    created() {
      this.loadEIP()
    },
    methods: {
      async loadEIP() {
        let eipId = this.$route.params.id;
        this.isEIPLoading = true;
        try {
          this.eip = await this.$store.dispatch('eip/loadEIP', eipId)
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
