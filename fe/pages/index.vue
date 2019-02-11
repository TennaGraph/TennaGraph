<template>
  <v-container class="dashboard pt-0">
    <v-layout column>
      <v-layout tennagraph_info align-center justify-center row fill-height class="mb-3">
        <v-card-text class="text-xs-center">
          <label class="headline font-weight-light">Minimum bias ethereum signal aggregator</label><br>
          <v-layout align-center justify-center row fill-height>
          <v-flex lg6 sm8>
          <label class="caption font-weight-thin">
            <b>Tennagraph</b> represents consensus among stakeholders on EIPs and community issues through the collection of on-chain and off-chain signals.
          </label>
          </v-flex>
          </v-layout>
        </v-card-text>
      </v-layout>

      <v-flex xs12>
        <eips-list></eips-list>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
  import PulseLoader from '~/components/PulseLoader.vue';
  import commonErrorsMixin from "~/mixins/commonErrorsMixin";
  import EipsList from "~/components/EipsList";

  export default {
    components: {
      EipsList,
      PulseLoader,
    },
    mixins: [
      commonErrorsMixin,
    ],
    data() {
      return {
      }
    },
    head() {
      return {
        title: 'Ethereum Improvement Proposals'
      }
    },
    methods: {

    },
    computed: {

    },

  };
</script>

<style scoped>

  .tennagraph_info {
    background-color: #23005C;
    color: #ffffff;
    height: 264px;
  }

</style>
