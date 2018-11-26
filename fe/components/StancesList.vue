<template>
      <v-layout column class="wrapper">
        <v-layout row align-center justify-start>
          <v-flex xs2>
            <span class="text-truncate">Yay ({{ yayStances.length }})</span>
          </v-flex>
          <v-flex xs10>
            <chip-stance v-for="(stance, index) in yayStances"
                  v-bind:key="stance.id"
                  :stance="stance"
                  v-if="index <4">
            </chip-stance>
            <chip-more-stances v-if="yayStances.length > 4" :stances="yayStances"></chip-more-stances>
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
                  v-if="index <3">
            </chip-stance>
            <chip-more-stances v-if="nayStances.length > 4" :stances="nayStances"></chip-more-stances>
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
                  v-if="index <3">
            </chip-stance>
            <chip-more-stances v-if="abstainStances.length > 4" :stances="abstainStances"></chip-more-stances>
          </v-flex>
        </v-layout>

        <span class="mt-5 mb-0">Something wrong in the stances? DM us at <a href="https://twitter.com/tennagraph" target="_blank">@tennagraph</a> to edit or remove stances</span>
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
  }
</script>

<style scoped>
  .wrapper {
    min-height: 150px;
  }
</style>
