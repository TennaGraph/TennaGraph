<template>
  <div class="header">
    <v-toolbar dark flat color="header">
      <v-toolbar-title class="mr-4">
        <nuxt-link class="logo" to="/" d-block >
          <img src='/theme/site_logo_head.svg' alt="">
        </nuxt-link>
      </v-toolbar-title>
      <v-layout class="flex xs-10 ml-auto justify-end fill-height">
        <v-toolbar-items class="hidden-sm-and-down list ml-auto">
          <nuxt-link to="" active-class="nav__signin" class="v-btn v-btn--flat body-1 white--text" exact>PROPOSALS</nuxt-link>
          <nuxt-link to="" active-class="nav__signin" class="v-btn v-btn--flat body-1 white--text" exact>ABOUT</nuxt-link>
        </v-toolbar-items>
      </v-layout>
    </v-toolbar>
  </div>
</template>

<script>
  import commonErrorsMixin from "~/mixins/commonErrorsMixin";
  import successAlertMixin from "~/mixins/successAlertsMixin";

  export default {
    name: 'GlobalHeader',
    mixins: [
      commonErrorsMixin,
      successAlertMixin,
    ],
    data() {
      return {
      }
    },
    created() {

    },
    components: {

    },
    methods: {

    },
    computed: {

    },
  };
</script>
