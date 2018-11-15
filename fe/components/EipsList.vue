<template>
  <v-layout class="d-block" px-2>

    <v-card-title class="title mb-4 mt-2 py-0 px-0 primary--text">Ethereum Improvement Proposals</v-card-title>

    <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">

      <div class="transaction__table" v-if="EIPsList.length > 0">
        <v-data-table
          class="clear"
          hide-actions
          :items="EIPsList"
          >
          <template slot="headers" slot-scope="props">
            <tr>
              <th class="text-xs-left east--text uppercase py-2">Title</th>
              <th class="text-xs-left east--text uppercase py-2">Status</th>
              <th class="text-xs-left east--text uppercase py-2">Type / Category</th>
              <!--<th class="text-xs-left east&#45;&#45;text uppercase py-2">Authors</th>-->
              <th class="text-xs-left east--text uppercase py-2">Created</th>
            </tr>
          </template>

          <template slot="items" slot-scope="props">
            <tr>
              <td class="py-1">EIP {{ props.item.eip_num }} {{ props.item.eip_title }}</td>
              <td class="py-1">{{ props.item.eip_status }}</td>
              <td class="py-1">{{ props.item.eip_type }}<br>{{ props.item.eip_category }}</td>
              <!--<td class="py-1">{{ props.item.eip_authors }}</td>-->
              <td class="py-1">{{ props.item.eip_created }}</td>
            </tr>
          </template>

        </v-data-table>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
  export default {
    name: "eips-list",
    created() {
      this.loadEIPs()
    },
    computed: {
      EIPsList() {
        return this.$store.getters['eip/EIPsList']
      }
    },
    methods: {
      async loadEIPs() {
        try {
          await this.$store.dispatch('eip/loadEIPs')
        } catch (e) {
          this.setResponseErrors(e);
        }
      }
    }
  }
</script>

<style scoped>

</style>
