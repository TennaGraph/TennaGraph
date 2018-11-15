<template>
  <v-container class="dashboard">
    <v-layout row mt-2>
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
        email: "",
        password: "",
      }
    },
    head() {
      return {
        title: 'Log In'
      }
    },
    methods: {

    },
    computed: {

    },

  };
</script>

<style scoped>
  .ferror {
    color: red;
  }
</style>
