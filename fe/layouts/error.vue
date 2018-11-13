<template>
  <v-content class="dark md-at" align-center justify-center px-1>
    <div class="xs12 md12 flex d-flex fill-height align-center mt-2 px-2">
      <v-card class="d-block box py-5 flex md12 xs12 mx-auto">
        <v-flex xs11 md10 mx-auto>
          <v-card-title class="title mb-3 pa-0" v-if="error.statusCode">{{ error.statusCode }}</v-card-title>
          <div class="confirm__message label--text" v-if="error.message">{{ error.message }}</div>
          <br>
          <!--<nuxt-link :to="localePath('index')">Home page</nuxt-link>-->
        </v-flex>
      </v-card>
    </div>
  </v-content>
</template>

<script>
export default {
  props: ['error'],
  layout: 'default' // you can set a custom layout for the error page
}
</script>
