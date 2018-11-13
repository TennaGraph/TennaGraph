<template>
  <div class="offline_mode">
    <v-card v-if="!isOnline" color="#8C8E98">
      <v-card-title class="white--text justify-center pa-1">{{ $t('header.offline_mode') }}</v-card-title>
    </v-card>
  </div>
</template>

<script>
  export default {
    name: "OfflineMode",
    computed: {
      isOnline() {
        return this.$store.getters['app/isOnline'];
      }
    }
  }
</script>

<style scoped>

</style>
