<template>
  <v-container class="dashboard">
    <v-layout row mt-2>
      <v-flex xs12>
        <v-layout class="d-block" px-2>

          <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">
            <v-card-title class="title mb-4 mt-2 py-0 px-0">
              Core Team
            </v-card-title>

            <v-card-text class="text-xs-center">
              <label class="headline font-weight-light">James Hancock</label><br>
              <v-layout align-center justify-center row fill-height>
              <v-flex lg6 sm8>
              <label class="caption font-weight-thin">
                <a href="https://twitter.com/madeof_tin" target="_blank">@madeof_tin</a>. Germany, Berlin 🇩🇪
              </label>
              </v-flex>
              </v-layout>
            </v-card-text>

            <v-card-text class="text-xs-center">
              <label class="headline font-weight-light">Malkevych Bohdan</label><br>
              <v-layout align-center justify-center row fill-height>
              <v-flex lg6 sm8>
              <label class="caption font-weight-thin">
                <a href="https://github.com/malkevych" target="_blank">GitHub</a>. <a href="https://twitter.com/bomalkevych" target="_blank">@bomalkevych</a>, Ukraine, Kyiv 🇺🇦
              </label>
              </v-flex>
              </v-layout>
            </v-card-text>

            <v-card-text class="text-xs-center">
              <label class="headline font-weight-light">Max Semenchuk</label><br>
              <v-layout align-center justify-center row fill-height>
              <v-flex lg6 sm8>
              <label class="caption font-weight-thin">
                <a href="https://twitter.com/maxsemenchuk" target="_blank">@maxsemenchuk</a>. Ukraine, Kyiv 🇺🇦
              </label>
              </v-flex>
              </v-layout>
            </v-card-text>


          </v-card>

        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>

  export default {
    name: 'about',
    head() {
      return {
        title: "About"
      }
    },
  };
</script>

<style scoped>
  .ferror {
    color: red;
  }
  table {
    border-spacing: 10px;
    border-collapse: separate;
  }
</style>
