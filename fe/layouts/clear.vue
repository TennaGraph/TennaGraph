<template>
  <v-app>

    <maintenance v-if="isMaintenance"></maintenance>
      <nuxt/>
    <notification v-for="n in notifications"
                  v-bind:key="n.identifier"
                  :dismissible="n.dismissible"
                  :value="n.message"
                  :identifier="n.identifier"
                  v-on:closeNotification="closeNotification">
    </notification>

  </v-app>
</template>

<script>

  import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
  import Maintenance from '@/components/Maintenance.vue';
  import Notification from '@/components/Notification';

  export default {
    components: {
      Maintenance,
      PulseLoader,
      Notification,
    },
    data() {
      return {
      }
    },
    mounted() {
    },
    methods: {
      closeNotification(identifier) {
        this.$store.dispatch('ntf/closeNotification', identifier);
      },
    },
    computed: {
      isMaintenance() {
        return this.$store.getters['app/isMaintenance'];
      },
      notifications() {
        return this.$store.getters['ntf/notifications'];
      },
    }
  };
</script>

<style>
  /*  #app {
      height: 100%;
    }*/
  html {
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    height: 100%;
    font-weight: 400;
    line-height: 1.27;
    font-size: 16px;
    overflow: auto;
    background-color: #EEEEEE;
  }

  .container {
    height: 100%;
  }

  [v-cloak] {
    display: none;
  }
</style>
