<template>
  <v-menu
    bottom
    origin="center center"
    :close-on-content-click="false"
  >
    <span slot="activator">
      Type / Categories <!--<v-img src="/icons/filter.svg" height="40"></v-img>-->
    </span>
    <v-list>
      <v-list-tile>
      <v-list-tile-title>
          Type / Categories
      </v-list-tile-title>
        </v-list-tile>
      <v-list-tile
        v-for="item in categories"
        :key="item.key"
      >
        <v-list-tile-action @click='toggleCategory'>
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
    name: "CategoryFilter",
    props: ['value'],
    data() {
      return {
        categories: [
          {text: 'Standard Track EIP', key: 'STANDARDS_TRACK', checkbox: true},
          {text: 'Standard Track EIP / Core', key: 'CORE', checkbox: true},
          {text: 'Standard Track EIP / Networking', key: 'NETWORKING', checkbox: true},
          {text: 'Standard Track EIP / Interface', key: 'INTERFACE', checkbox: true},
          {text: 'Standard Track EIP / ERC', key: 'ERC', checkbox: true},
          {text: 'Informational EIP', key: 'INFORMATIONAL', checkbox: true},
          {text: 'Meta EIP', key: 'META', checkbox: true},
        ],
      }
    },
    created() {
      this.setFilter()
    },
    computed: {
      isFilterEnabled() {
        const isActive = (result, curr) => !curr.checkbox || result;
        return this.categories.reduce(isActive, false)
      }
    },
    methods: {
      toggleCategory() {
        // update v-model
        this.$emit('input', this.createVModelCategories())
      },

      createVModelCategories() {
        return {
          isEnabled: this.isFilterEnabled,
          keys: this.categories.filter(item => item.checkbox).map(item => item.key),
        }
      },

      setFilter() {
        if(!this.value.isEnabled) return;
        this.categories.forEach(item => {
          item.checkbox = this.value.keys.includes(item.key)
        })
      }
    },
  }
</script>

<style scoped>

</style>
