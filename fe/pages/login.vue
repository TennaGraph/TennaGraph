<template>
  <v-content class="dark md-at" align-center justify-center px-1>

  </v-content>
</template>


<script>
  import PulseLoader from '~/components/PulseLoader.vue';
  import commonErrorsMixin from "~/mixins/commonErrorsMixin";

  export default {
    components: {
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
