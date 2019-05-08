<template>
  <v-container class="dashboard pt-0">
    <v-layout column>
      <v-layout v-if="!isAboutProjectAlertClosed" tennagraph_info align-center row fill-height class="my-4">
        <div class="breeze" style="width: 10px; height:176px;"></div>
        <v-flex>
          <v-card-text>
            <v-flex lg6 sm8>
              <label class="headline font-weight-light">App for creation/collection of network sentiment for better Ethereum governance</label><br>
            </v-flex>
            <v-layout align-center row fill-height>
              <v-flex sm8>
              <label class="caption font-weight-thin">
                Enabling more perspectives through: Coin Voting, Gas Voting & Rated influencer stances. <a href="https://ethsignals.gitbook.io/wiki/tennagraph/tennagraph-ethereum-signal-aggregator" class="breeze--text" target="_blank">Know more</a>
              </label>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-flex>
        <v-flex>
          <v-layout tennagraph_info align-start justify-end row fill-height class="my-4">
            <v-btn type="button" flat icon class="mx-3 my-3" @click="closeAboutProjectAlert">
              <v-icon color="grey" large>close</v-icon>
            </v-btn>
          </v-layout>
        </v-flex>
      </v-layout>

      <v-flex xs12 class="mt-3">
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
      closeAboutProjectAlert() {
        this.$store.dispatch("app/closeAlertAboutProject");
      }
    },
    computed: {
      isAboutProjectAlertClosed() {
        return this.$store.getters['app/isAboutProjectAlertClosed'];
      }
    },

  };
</script>

<style scoped>

  .tennagraph_info {
    background-color: #ffffff;
    color: #000000;
    height: 176px;
  }

  .left_border {
    background-color: #45C299;
    height: 176px;
    width: 5px;
  }

</style>
