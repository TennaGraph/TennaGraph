<template>
  <article>
  <h1 v-html="$t('pages.maintenance.coming_back_soon')"></h1>
  <div>
    <p v-html="$t('pages.maintenance.message', {'supportEmail': email})"></p>
    <br/>
    <p>&mdash; {{ $t('pages.maintenance.team') }} {{ siteName }}</p>
  </div>
</article>
</template>

<script>
  export default {
    name: "maintenance",
    computed: {
      email() {
        return "mailto:" + this.$store.getters['app/supportEmail'];
      },
      siteName() {
        return this.$store.getters['app/siteName'];
      },
    }
  }
</script>

<style scoped>
  body {
    text-align: center;
    height: 100%;
  }
  h1 { font-size: 50px; }
  body { font: 20px Helvetica, sans-serif; color: #333; }
  article { display: block; text-align: left; width: 650px; margin: 0px auto; padding-top: 200px  }
  a { color: #dc8100; text-decoration: none; }
  a:hover { color: #333; text-decoration: none; }
</style>
