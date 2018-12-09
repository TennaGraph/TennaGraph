<template>
  <v-app>

    <div class="holder" v-cloak>
      <maintenance v-if="isMaintenance"></maintenance>
      <div class="page column d-flex" v-else v-bind:class="{ 'page--has-sidebar': isSidebarOppened, 'page--has-menu': isProfileSidebarOpened }">

        <!--<offline-mode v-bind:class="{ 'pt-0': isSidebarOppened || isProfileSidebarOpened }"></offline-mode>-->
        <qr-code-sidebar :display="isQrCodeSidebarOpened"></qr-code-sidebar>
        <global-header></global-header>
        <nuxt/>
        <global-footer></global-footer>
      </div>

      <notification v-for="n in notifications"
                    v-bind:key="n.identifier"
                    :dismissible="n.dismissible"
                    :value="n.message"
                    :identifier="n.identifier"
                    v-on:closeNotification="closeNotification">
      </notification>

      <zendesk v-if="isZendeskExists" :zendeskKey="zendeskKey"></zendesk>
    </div>
  </v-app>
</template>

<script>

  import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
  import Zendesk from '@/components/frameworks/Zendesk.vue';
  import Maintenance from '@/components/Maintenance.vue';
  import GlobalFooter from '@/components/footer/GlobalFooter';
  import GlobalHeader from '@/components/header/GlobalHeader';
  import Notification from '@/components/Notification';
  import OfflineMode from "@/components/offline_mode/OfflineMode";
  import QrCodeSidebar from "@/components/menu/QrCodeSidebar";

  export default {
    components: {
      QrCodeSidebar,
      Zendesk,
      Maintenance,
      PulseLoader,
      GlobalHeader,
      GlobalFooter,
      Notification,
      OfflineMode,
    },
    data() {
      return {
      }
    },
    created() {
      this.setupStyles();
      this.cookieNotification()
    },
    mounted() {
    },
    methods: {
      setupStyles() {
        // favicon
        // const faviconElement = document.getElementById('site_favicon');
        // faviconElement.href = this.$store.getters['app/faviconLogo'];
      },
      closeNotification(identifier) {
        this.$store.dispatch('ntf/closeNotification', identifier);
      },

      cookieNotification() {
        let isCookieNotificationShowed = localStorage.getItem('isCookieNotificationShowed');
        if (isCookieNotificationShowed !== 'true') {
          localStorage.setItem('isCookieNotificationShowed', 'true');
          this.$store.dispatch("ntf/displayNotifications", ['We use cookies to provide the best site experience.']);
        }
      }
    },
    computed: {
      isMaintenance() {
        return this.$store.getters['app/isMaintenance'];
      },
      zendeskKey() {
        return this.$store.getters['app/zendeskKey'];
      },
      isZendeskExists() {
        if (this.zendeskKey == null || !this.zendeskKey || this.zendeskKey.length == 0) {
          return false;
        }
        return true;
      },
      notifications() {
        return this.$store.getters['ntf/notifications'];
      },

      /* UI Sidebars */
      isSidebarOppened() {
        return this.$store.getters['ui/isSidebarOpened'];
      },
      isProfileSidebarOpened() {
        return this.$store.getters['ui/isProfileSidebarOpened'];
      },
      isQrCodeSidebarOpened() {
        return this.$store.getters['ui/isQrCodeSidebarOpened'];
      }
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
