<template>
  <v-chip color="breeze" style="height: 40px" @click="onChangeShowMore()">
    <label v-if="!value" class="body-1 white--text">+ {{ stances.length - 4 }} more</label>
    <label v-else class="body-1 white--text">close</label>
  </v-chip>
</template>

<script>
  export default {
    name: "ChipMoreStances",
    props: {
      stances: {
        type: Array,
        required: true
      },
      // is show more opened
      value: {
        type: Boolean,
        required: true
      }
    },
    // props: ['value', 'stances'],
    methods: {
      onChangeShowMore() {
        this.$emit('input', !this.value)
      }
    }
  }
</script>

<style scoped>

</style>
