<template>
      <v-layout column class="wrapper">
          <v-layout row align-center justify-start>
            <v-flex xs2>
              <span class="text-truncate">Yay (35)</span>
            </v-flex>
            <v-flex xs10>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
              <chip></chip>
            </v-flex>
          </v-layout>

        <v-layout row align-center justify-start>
          <v-flex xs2>
            <span class="text-truncate">Nay (35)</span>
          </v-flex>
          <v-flex xs10>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
          </v-flex>
        </v-layout>

        <v-layout row align-center justify-start>
          <v-flex xs2>
            <span class="text-truncate">Abstain (35)</span>
          </v-flex>
          <v-flex xs10>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
            <chip></chip>
          </v-flex>
        </v-layout>
      </v-layout>
</template>

<script>
  import Chip from "~/components/Chip";

  export default {
    name: "stances-list",
    components: {Chip}
  }
</script>

<style scoped>
  .wrapper {
    min-height: 150px;
  }
</style>
