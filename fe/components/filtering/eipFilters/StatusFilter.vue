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
        v-for="(item, index) in statusGroups"
        :key="item.text"
      >
        <v-list-tile-action @click='toggleGroup(index)'>
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
          {text: 'Draft', key: 'DRAFT', 'checkbox': true, 'isActiveStatus': true},
          {text: 'Active', key: 'ACTIVE', 'checkbox': true, 'isActiveStatus': true},
          {text: 'Last call', key: 'LAST_CALL', 'checkbox': true, 'isActiveStatus': true},
          {text: 'Replaced', key: 'REPLACED', 'checkbox': true, 'isActiveStatus': true},
          {text: 'Accepted', key: 'ACCEPTED', 'checkbox': true, 'isActiveStatus': true},
          {text: 'Final', key: 'FINAL', 'checkbox': true, 'isActiveStatus': true},
          {text: 'Deferred', key: 'DEFERRED', 'checkbox': true, 'isActiveStatus': false},
        ],
        statusGroups: [
          {text: 'Active', 'checkbox': true},
          {text: 'Deferred', 'checkbox': true},
        ],
      }
    },
    created() {
      this.setFilter()
    },
    computed: {
      isActiveGroup() {
        const isActive = (result, curr) => !((curr.isActiveStatus && !curr.checkbox) || !result);
        return this.statuses.reduce(isActive, true)
      },

      isDeferredGroup() {
        const isActive = (result, curr) => !((!curr.isActiveStatus && !curr.checkbox) || !result);
        return this.statuses.reduce(isActive, true)
      },

      isFilterEnabled() {
        return !this.isActiveGroup || !this.isDeferredGroup;
      }
    },
    methods: {
      toggleGroup(index) {
        const isActive = index === 0;
        const newValue = this.statusGroups[index].checkbox;

        this.statuses.filter(item => item.isActiveStatus === isActive).forEach(item => item.checkbox = newValue)

        // update v-model
        this.$emit('input', this.createVModelStatuses())
      },

      toggleStatus() {
        // update v-model
        this.$emit('input', this.createVModelStatuses())
      },

      createVModelStatuses() {
        return {
          isEnabled: this.isFilterEnabled,
          keys: this.statuses.filter(item => item.checkbox).map(item => item.key),
        }
      },

      setFilter() {
        if(!this.value.isEnabled) return;
        this.statuses.forEach(item => {
          item.checkbox = this.value.keys.includes(item.key)
        })
      }
    },
    watch: {
      isActiveGroup(newValue) {
        this.statusGroups[0].checkbox = newValue
      },

      isDeferredGroup(newValue) {
        this.statusGroups[1].checkbox = newValue
      },
    }
  }
</script>

<style scoped>

</style>
