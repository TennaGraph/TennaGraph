<template>
  <v-snackbar
      v-model="snackbar"
      left
      bottom
      :timeout="0"
      multi-line
    >
      {{ value }}
      <v-btn
        color="white"
        flat
        v-if="dismissible"
       @click="hide(identifier)"
      >
        Close
      </v-btn>
    </v-snackbar>
</template>

<script>

  export default {
    name: 'Notification',
    props: {
      identifier: {
        type: String,
        required: true,
      },
      value: {
        type: String,
        required: true,
      },
      dismissible: {
        type: Boolean,
        required: false,
        default: true,
      },
    },
    data: function () {
        return {
          snackbar: true
        }
    },
    created: function () {
      const mv = this;
      const identifier = this.identifier;

      // Automatically hide in x seconds if not dismissible
      if (!this.dismissible) {
        setTimeout(function () {
          mv.hide(identifier);
        }.bind(this), 5000);
      }
    },
    methods: {
      hide: function (identifier) {
        this.$store.dispatch('ntf/closeNotification', identifier);
      }
    },
    computed: {
      notifications() {
        return this.$store.getters['ntf/notifications'];
      }
    }
  };
</script>

<style>

</style>
