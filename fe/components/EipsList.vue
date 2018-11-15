<template>
  <v-layout class="d-block" px-2>

    <v-card-title class="title mb-4 mt-2 py-0 px-0 primary--text">Ethereum Improvement Proposals</v-card-title>

    <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">

      <div class="transaction__table" v-if="eips.length > 0">
        <v-data-table
          class="clear"
          hide-actions
          :items="eips"
          >
          <template slot="headers" slot-scope="props">
            <tr>
              <th class="text-xs-left east--text uppercase py-2">Title</th>
              <th class="text-xs-left east--text uppercase py-2">Status</th>
              <th class="text-xs-left east--text uppercase py-2">Component</th>
              <th class="text-xs-left east--text uppercase py-2">Authors</th>
              <th class="text-xs-left east--text uppercase py-2">Created</th>
            </tr>
          </template>

          <template slot="items" slot-scope="props">
            <tr>
              <td class="py-1"></td>
              <td class="py-1"></td>
              <td class="py-1"></td>
              <td class="py-1"></td>
              <td class="py-1"></td>
            </tr>
          </template>

        </v-data-table>
        <v-card class="secondary pa-0 primary--text secondary_light mt-4 br-5 shadow-none">
          <v-card-text  class="secondary text-xs-center py-2 px-2 noresult">
            ыаыар лоыарфы а фыр
          </v-card-text>
        </v-card>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
  export default {
    name: "eips-list",
    computed: {
      eips() {
        return [1,2]
      }
    }
  }
</script>

<style scoped>

</style>
