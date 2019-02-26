<template>
  <v-menu
    bottom
    origin="center center"
    :close-on-content-click="false"
  >
    <span slot="activator">
      Status <!--<v-img src="/icons/filter.svg" height="40"></v-img>-->
    </span>
    <v-list>
      <v-list-tile>
      <v-list-tile-title>
          Status
      </v-list-tile-title>
        </v-list-tile>
      <v-list-tile
        v-for="item in statuses"
        :key="item.key"
      >
        <v-list-tile-action @click='toggleStatus'>
          <v-checkbox
            v-model="item.checkbox"
          >
          <label slot="label" @click.prevent>{{ item.text }}</label>
          </v-checkbox>
        </v-list-tile-action>
      </v-list-tile>
      <v-divider></v-divider>
      <v-list-tile
        v-for="item in statusGroups"
        :key="item.text"
      >
        <v-list-tile-action @click='toggleStatus'>
          <v-checkbox
            v-model="item.checkbox"
          >
          <label slot="label" @click.prevent>{{ item.text }}</label>
          </v-checkbox>
        </v-list-tile-action>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
  export default {
    name: "StatusFilter",
    props: ['value'],
    data() {
      return {
        statuses: [
          {text: 'Draft', key: 'DRAFT', 'checkbox': true},
          {text: 'Active', key: 'ACTIVE', 'checkbox': true},
          {text: 'Last call', key: 'LAST_CALL', 'checkbox': true},
          {text: 'Replaced', key: 'REPLACED', 'checkbox': true},
          {text: 'Accepted', key: 'ACCEPTED', 'checkbox': true},
          {text: 'Final', key: 'FINAL', 'checkbox': true},
          {text: 'Deferred', key: 'DEFERRED', 'checkbox': true},
        ],
        statusGroups: [
          {text: 'Only active voting', key: 'ONLY_ACTIVE_VOTING', 'checkbox': false},
        ],
      }
    },
    created() {
      this.setFilter()
    },
    computed: {
      isFilterEnabled() {
        const isActive = (result, curr) => !((curr.isActiveStatus && !curr.checkbox) || !result);

        return this.statuses.reduce(isActive, true) || this.statusGroups.reduce(isActive, true);
      }
    },
    methods: {

      toggleStatus() {
        // update v-model
        this.$emit('input', this.createVModelStatuses())
      },

      createVModelStatuses() {
        const options = this.statuses.concat(this.statusGroups);
        return {
          isEnabled: this.isFilterEnabled,
          keys: options.filter(item => item.checkbox).map(item => item.key),
        }
      },

      setFilter() {
        if(!this.value.isEnabled) return;
        this.statuses.forEach(item => {
          item.checkbox = this.value.keys.includes(item.key)
        })
      }
    },
  }
</script>

<style scoped>

</style>
