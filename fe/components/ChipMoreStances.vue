<template>
  <v-chip color="breeze" style="height: 40px">
    <label class="body-1 white--text">+ {{ stances.length - 4 }} more</label>
  </v-chip>
</template>

<script>
  export default {
    name: "ChipMoreStances",
    props: {
      stances: {
        type: Array,
        required: true
      }
    }
  }
</script>

<style scoped>

</style>
