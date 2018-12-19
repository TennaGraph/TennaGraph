<template>
  <v-layout>
    <v-flex class="px-2">
      <vue-markdown>{{ eipDescription }}</vue-markdown>
    </v-flex>
  </v-layout>
</template>

<script>
  import VueMarkdown from 'vue-markdown'

  export default {
    name: "EipDescription",
    props: {
      eipDescription: {
        type: String,
        required: true
      }
    },
    components: {
      VueMarkdown
    }
  }
</script>

<style scoped>
  
</style>
