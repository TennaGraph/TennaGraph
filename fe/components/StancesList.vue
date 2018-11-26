<template>
      <v-layout column class="wrapper">
        <v-layout row align-center justify-start>
          <v-flex xs2>
            <span class="text-truncate">Yay ({{ yayStances.length }})</span>
          </v-flex>
          <v-flex xs10>
            <chip v-for="stance in yayStances"
                  v-bind:key="stance.id"
                  :stance="stance">
            </chip>
          </v-flex>
        </v-layout>

        <v-layout row align-center justify-start>
          <v-flex xs2>
            <span class="text-truncate">Nay ({{ nayStances.length }})</span>
          </v-flex>
          <v-flex xs10>
            <chip v-for="stance in nayStances"
                  v-bind:key="stance.id"
                  :stance="stance">
            </chip>
          </v-flex>
        </v-layout>

        <v-layout row align-center justify-start>
          <v-flex xs2>
            <span class="text-truncate">Abstain ({{ abstainStances.length }})</span>
          </v-flex>
          <v-flex xs10>
            <chip v-for="stance in abstainStances"
                  v-bind:key="stance.id"
                  :stance="stance">
            </chip>
          </v-flex>
        </v-layout>
      </v-layout>
</template>

<script>
  import Chip from "~/components/Chip";

  export default {
    name: "stances-list",
    components: {
      Chip
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
