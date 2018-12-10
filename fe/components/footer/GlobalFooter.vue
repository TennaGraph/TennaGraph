<template>
  <v-footer height="auto" class="clear pl-3 pr-5 mt-2 align-center justify-between" color="white">
    <v-layout class="pr-5 mr-5">
      <v-layout class=" align-center justify-between mr-5 wrap">
          <img class="logo mr-auto" src='/theme/site_logo_footer.svg' alt="">
        <nuxt-link to="/" class="mr-3 label--text body-1">Proposals</nuxt-link>
        <nuxt-link to="/about" class="mr-3 label--text body-1">About</nuxt-link>
      </v-layout>
    </v-layout>
  </v-footer>
</template>

<script>
  export default {
    name: 'GlobalFooter',
    components: {

    },
    data() {
      return {};
    },
    computed: {

    },
  };
</script>
