<template>
  <loader :color="chooseColor()"></loader>
</template>

<script>

  import Loader from 'vue-spinner/src/PulseLoader.vue';

  export default {
    name: "pulse-loader",
    props: {
      color: {
        type: String,
      }
    },
    components: {
      Loader
    },
    created() {
      this.primary()
    },
    methods: {
      primary() {
        const defaultColor = 'silver';
        if (this.$vuetify.theme) {
          return this.$vuetify.theme.theme_primary || defaultColor
        }
        return defaultColor
      },
      chooseColor() {
        if (this.color) {
          return this.color;
        } else {
          return this.primary()
        }
      }
    }
  }
</script>

<style scoped>

</style>
