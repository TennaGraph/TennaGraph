<template>
  <v-layout class="d-block" px-2>

      <v-card-title class="title mb-4 mt-2 py-0 px-0 primary--text">
        {{ isFilteringEnabled ? "Ethereum Improvement Proposals" : "Recently Voted EIPs" }}
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
          :headers="headers"
          :search="search"
          :pagination.sync="pagination"
          :headers-length="5"
          >

          <template slot="headers" slot-scope="props">
            <tr>
              <th
                class="text-xs-left"
                v-for="(header, index) in props.headers"
                v-if="index <= 1"
                :key="header.text"
                :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
                @click="changeSort(header.value)"
              >
                {{ header.text }}
                <v-icon small>arrow_upward</v-icon>
              </th>

              <th>
                <status-filter v-model="statusFilter"></status-filter>
              </th>
              <th>
                <category-filter v-model="categoryFilter"></category-filter>
              </th>

              <th
                v-for="(header, index) in props.headers"
                v-if="index >= 4"
                :key="header.text"
                :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
                @click="changeSort(header.value)"
              >
                {{ header.text }}
                <v-icon small>arrow_upward</v-icon>
              </th>
            </tr>
          </template>

          <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
          <template slot="items" slot-scope="props">
            <tr class="eip_tr" @click="$router.push({ path: '/eip/' + props.item.eip_num })">
              <td class="body-1 py-3">{{ props.item.eip_num }}</td>
              <td class="body-1 py-3">{{ props.item.eip_title }}</td>

              <td class="py-3">
                <div class="text-xs-left"
                     v-if="props.item.eip_status.key == 'DRAFT' ||
                           props.item.eip_status.key == 'OTHER'">
                  <v-btn round color="grey" small dark class="text-capitalize">
                    {{ props.item.eip_status.display }}
                  </v-btn>
                </div>

                <div class="text-xs-left"
                     v-if="props.item.eip_status.key == 'DEFERRED' ||
                           props.item.eip_status.key == 'REPLACED'">
                  <v-btn round color="red" small dark class="text-capitalize">
                    {{ props.item.eip_status.display }}
                  </v-btn>
                </div>

                <div class="text-xs-left"
                     v-if="props.item.eip_status.key == 'ACTIVE' ||
                              props.item.eip_status.key == 'LAST_CALL' ||
                              props.item.eip_status.key == 'FINAL' ||
                              props.item.eip_status.key == 'ACCEPTED'">
                  <v-btn round color="breeze" small dark class="text-capitalize">
                    {{ props.item.eip_status.display }}
                  </v-btn>
                </div>
              </td>

              <td class="py-3 text-xs-left text-truncate text-capitalize" v-if="props.item.eip_type && props.item.eip_category">
                {{ props.item.eip_type.display }}<br> {{ props.item.eip_category.display }}
              </td>
              <td class="py-3 text-xs-left text-truncate text-capitalize" v-else>{{ props.item.eip_type.display }}</td>
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
  import StatusFilter from "~/components/filtering/eipFilters/StatusFilter";
  import CategoryFilter from "~/components/filtering/eipFilters/CategoryFilter";

  export default {
    name: "eips-list",
    components: {CategoryFilter, StatusFilter},
    mixins: [
      commonErrorsMixin,
    ],
    data() {
      return {
        search: '',
        pagination: {
          sortBy: 'eip_num',
          rowsPerPage: 10
        },
        statusFilter: this.$store.getters['eip/statusFilter'],
        categoryFilter: this.$store.getters['eip/categoryFilter'],
        headers: [
          {
            text: 'EIP',
            align: 'left',
            sortable: true,
            value: 'eip_num',
            class: 'text-xs-left east&#45;&#45;text uppercase py-2'
          },
          {
            text: 'Title',
            value: 'eip_title',
            sortable: true,
            class: 'text-xs-left east&#45;&#45;text uppercase py-2',
          },
          {
            text: 'Status',
            value: 'eip_status.key',
            sortable: false,
            class: 'text-xs-left east&#45;&#45;text uppercase py-2',
          },
          {
            text: 'Type / Category',
            value: 'eip_category.key',
            sortable: false,
            class: 'text-xs-left east&#45;&#45;text uppercase py-2',
          },
          {
            text: 'Created',
            value: 'eip_created',
            sortable: false,
            class: 'text-xs-left east&#45;&#45;text uppercase py-2',
          },
        ],

      }
    },
    created() {
      this.loadEIPs()
    },
    computed: {
      EIPsList() {
        let eips = this.$store.getters['eip/EIPsList'];

        // Filter by status
        if(this.statusFilter && this.statusFilter.isEnabled) {
          const filterKeys = this.statusFilter.keys;
          const keysExceptActiveVoting = filterKeys.filter(item => item !== 'ONLY_ACTIVE_VOTING');
          if(filterKeys.length > keysExceptActiveVoting.length) {
            eips = eips.filter(item => item.is_voting_active)
          }

          eips = eips.filter(item => keysExceptActiveVoting.includes(item.eip_status.key))
        }

        // Filter by type / category
        if(this.categoryFilter && this.categoryFilter.isEnabled) {
          const filterKeys = this.categoryFilter.keys;
          eips = eips.filter(item => (item.eip_category && filterKeys.includes(item.eip_category.key)) || filterKeys.includes(item.eip_type.key))
        }

        // Show only active recent eips
        if (!this.isFilteringEnabled) {
          eips = eips.filter(item => item.voting_details && item.voting_details.is_voting_open)
        }
        return eips
      },

      isEIPsLoading() {
        return this.$store.getters['eip/isEIPsLoading']
      },

      isFilteringEnabled() {
        let isFilteredByStatus = this.statusFilter && this.statusFilter.isEnabled;
        let isFilteredByCategory = this.categoryFilter && this.categoryFilter.isEnabled;
        return isFilteredByStatus || isFilteredByCategory || this.search
      }

    },
    methods: {
      async loadEIPs() {
        try {
          await this.$store.dispatch('eip/loadEIPs')
        } catch (e) {
          this.setResponseErrors(e);
        }
      },

      changeSort (column) {
        if (this.pagination.sortBy === column) {
          this.pagination.descending = !this.pagination.descending
        } else {
          this.pagination.sortBy = column
          this.pagination.descending = false
        }
      }
    },
    watch: {
      statusFilter(newValue) {
        this.$store.dispatch('eip/setFilterStatuses', newValue)
      },

      categoryFilter(newValue) {
        this.$store.dispatch('eip/setFilterCategories', newValue)
      },
    }
  }
</script>

<style scoped>

  .eip_tr {
    cursor: pointer;
  }

</style>
