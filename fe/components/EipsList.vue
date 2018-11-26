<template>
  <v-layout class="d-block" px-2>

      <v-card-title class="title mb-4 mt-2 py-0 px-0 primary--text">
        Ethereum Improvement Proposals
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          single-line
          hide-details
          solo
        ></v-text-field>
      </v-card-title>

    <v-card class="pt-4 pb-5 px-4 primary--text secondary_light mt-4 br-5">

      <div class="transaction__table">
        <v-data-table
          class="clear"
          :loading="isEIPsLoading"
          no-results-text="No any proposal yet"
          :items="EIPsList"
          :search="search"
          :pagination.sync="pagination"
          >
          <template slot="headers" slot-scope="props">
            <tr>
              <th class="text-xs-left east--text uppercase py-2">EIP</th>
              <th class="text-xs-left east--text uppercase py-2">Title</th>
              <th class="text-xs-left east--text uppercase py-2">Status</th>
              <th class="text-xs-left east--text uppercase py-2">Type / Category</th>
              <th class="text-xs-left east--text uppercase py-2">Created</th>
            </tr>
          </template>

          <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
          <template slot="items" slot-scope="props">
            <tr @click="$router.push({ path: '/eip/' + props.item.id });">
              <td class="body-1 py-3">{{ props.item.eip_num }}</td>
              <td class="body-1 py-3">{{ props.item.eip_title }}</td>

              <td class="py-3">
                <v-card flat dark class="text-xs-center"
                        color="grey"
                        v-if="props.item.eip_status.key == 'DRAFT' ||
                              props.item.eip_status.key == 'OTHER'">
                  <v-card-text class="py-1 px-2 caption white--text text-capitalize">
                    {{ props.item.eip_status.display }}
                  </v-card-text>
                </v-card>

                <v-card flat dark class="text-xs-center"
                        color="red"
                        v-if="props.item.eip_status.key == 'DEFERRED' ||
                              props.item.eip_status.key == 'REPLACED'">
                  <v-card-text class="py-1 px-2 caption white--text text-capitalize">
                    {{ props.item.eip_status.display }}
                  </v-card-text>
                </v-card>

                <v-card flat dark class="text-xs-center"
                        color="breeze"
                        v-if="props.item.eip_status.key == 'ACTIVE' ||
                              props.item.eip_status.key == 'LAST_CALL' ||
                              props.item.eip_status.key == 'FINAL' ||
                              props.item.eip_status.key == 'ACCEPTED'">
                  <v-card-text class="py-1 px-2 caption white--text text-capitalize">
                    {{ props.item.eip_status.display }}
                  </v-card-text>
                </v-card>
              </td>

              <td class="py-3 text-xs-left text-truncate" v-if="props.item.eip_category">
                {{ props.item.eip_type.display }} / {{ props.item.eip_category.display }}
              </td>
              <td class="py-3 text-xs-left text-truncate" v-else>{{ props.item.eip_type.display }}</td>
              <td class="py-3 text-xs-left text-truncate">{{ props.item.eip_created }}</td>
            </tr>
          </template>

        </v-data-table>
      </div>
    </v-card>
  </v-layout>
</template>

<script>

  import commonErrorsMixin from "~/mixins/commonErrorsMixin";

  export default {
    name: "eips-list",
    mixins: [
      commonErrorsMixin,
    ],
    data() {
      return {
        search: '',
        pagination: {
          rowsPerPage: 10
        },
      }
    },
    created() {
      this.loadEIPs()
    },
    computed: {
      EIPsList() {
        return this.$store.getters['eip/EIPsList']
      },
      isEIPsLoading() {
        return this.$store.getters['eip/isEIPsLoading']
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
