<template>
  <v-chip color="chip" style="height: 39px">
    <v-avatar>
      <img :src="avatarUrl" :alt="name">
    </v-avatar>
    <v-flex column>
      <label class="body-2 chipTitle--text">{{ name }}</label>
      <label class="caption chipSubtitle--text">{{ date }}</label>
    </v-flex>
    <img src="/icons/chip_link.svg" right/>
  </v-chip>
</template>

<script>
  export default {
    name: "Chip",
    props: {
      name: {
        type: String,
        required: true,
      },
      avatarUrl: {
        type: String,
        required: true,
      },
      date: {
        type: Date,
        required: true
      },
    }
  }
</script>

<style scoped>

</style>
