<template>
  <v-chip color="chip" style="height: 44px">
    <!--<v-avatar>-->
      <!--<img :src="avatarUrl" :alt="name">-->
    <!--</v-avatar>-->
    <v-flex column class="mx-2">
      <label class="body-1 chipTitle--text">{{ stance.author }}</label>
      <label class="caption chipSubtitle--text">{{ stance.created_at | formatDate }}</label>
    </v-flex>
    <a :href="stance.proof_url" target="_blank">
      <img src="/icons/chip_link.svg" right/>
    </a>
  </v-chip>
</template>

<script>
  export default {
    name: "ChipStance",
    props: {
      stance: {
        type: Object,
        required: true
      }
    }
  }
</script>

<style scoped>

</style>
