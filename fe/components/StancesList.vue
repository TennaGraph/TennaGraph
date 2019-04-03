<template>
  <v-layout column class="wrapper">

    <v-layout row align-center justify-start>
      <v-flex xs2>
        <span class="text-truncate">Yea ({{ yayStances.length }})</span>
      </v-flex>
      <v-flex xs10>
        <chip-stance v-for="(stance, index) in yayStances"
              v-bind:key="stance.id"
              :stance="stance"
              v-if="index <4 || isDisplayAllYayStances">
        </chip-stance>
        <chip-more-stances v-model="isDisplayAllYayStances" v-if="yayStances.length > 4" :stances="yayStances"></chip-more-stances>
      </v-flex>
    </v-layout>

    <v-layout row align-center justify-start>
      <v-flex xs2>
        <span class="text-truncate">Nay ({{ nayStances.length }})</span>
      </v-flex>
      <v-flex xs10>
        <chip-stance v-for="(stance, index) in nayStances"
              v-bind:key="stance.id"
              :stance="stance"
              v-if="index <4 || isDisplayAllNayStances">
        </chip-stance>
        <chip-more-stances v-model="isDisplayAllNayStances" v-if="nayStances.length > 4" :stances="nayStances"></chip-more-stances>
      </v-flex>
    </v-layout>

    <v-layout row align-center justify-start>
      <v-flex xs2>
        <span class="text-truncate">Abstain ({{ abstainStances.length }})</span>
      </v-flex>
      <v-flex xs10>
        <chip-stance v-for="(stance, index) in abstainStances"
              v-bind:key="stance.id"
              :stance="stance"
              v-if="index <4 || isDisplayAllAbstainStances">
        </chip-stance>
        <chip-more-stances v-model="isDisplayAllAbstainStances" v-if="abstainStances.length > 4" :stances="abstainStances"></chip-more-stances>
      </v-flex>
    </v-layout>

    <label class="body-1 chipTitle--text mt-4">
      Something wrong in the stances? DM us at <a href="https://twitter.com/tennagraph" target="_blank">@tennagraph</a> to request an edit or remove a stance. Also, join <a href="https://riot.tennagraph.com" target="_blank">riot.tennagraph.com</a> or our <a href="https://t.me/tennagraph" target="_blank">telegram group</a> for updates and answers to any questions.
    </label>
  </v-layout>
</template>

<script>
  import ChipStance from "~/components/ChipStance";
  import ChipMoreStances from "~/components/ChipMoreStances";

  export default {
    name: "stances-list",
    components: {
      ChipMoreStances,
      ChipStance
    },
    props: {
      yayStances: {
        type: Array,
        required: true
      },
      nayStances: {
        type: Array,
        required: true
      },
      abstainStances: {
        type: Array,
        required: true
      },
    },
    data() {
      return {
        isDisplayAllYayStances: false,
        isDisplayAllNayStances: false,
        isDisplayAllAbstainStances: false,
      }
    }
  }
</script>

<style scoped>
  .wrapper {
    min-height: 150px;
  }
</style>
