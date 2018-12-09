<template>
  <aside class="py-4 d-flex justify-center" v-if="display" v-bind:class="{ 'aside--open': display }">
  <v-flex xs11 md10>

    <v-layout class="d-block text-xs-right">
      <v-btn type="button" flat icon class="mr-0" @click="hide">
        <v-icon color="label" large>close</v-icon>
      </v-btn>
    </v-layout>

    <h3 class="title m-2">QR Code</h3>
    <p class="label--text mt-5">To vote <b>{{ option }}</b>, send 0 ETH to this address</p>
    <vue-qrcode
      v-if="addressToSendTransaction"
      v-bind:value="addressToSendTransaction"
      :options="{ size: 272 }"
      class="mx-auto mt-5 d-block"></vue-qrcode>
  </v-flex>
 </aside>
</template>


<script>

  import successAlertMixin from "~/mixins/successAlertsMixin"
  import VueQrcode from '@xkeshi/vue-qrcode';

  export default {
    name: "qr-code-sidebar",
    components: {
      VueQrcode,
    },
    mixins: [
      successAlertMixin,
    ],
    props: {
      display: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      hide() {
        this.$store.dispatch("ui/closeAllMenus");
      },
    },
    computed: {
      votingInfo() {
        return this.$store.getters['ui/']
      },
      option() {
        return this.$store.getters['ui/qrCode'].option
      },
      addressToSendTransaction() {
        return this.$store.getters['ui/qrCode'].address
      }
    },
  }
</script>
