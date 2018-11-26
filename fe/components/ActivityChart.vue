<template>
  <v-container text-xs-center>
    <svg :width="width" :height="height">
      <g v-for="(cols, colIndex) in board" v-bind:key="'col' + colIndex" transform="translate(0, 0)">
        <g :transform="'translate('+ colIndex*15 +', 0)'">
          <rect
            v-for="(item, itemIndex) in cols" v-bind:key="'item'+itemIndex"
            class="day"
            width="12" height="12"
            x="0" :y="itemIndex * 15"
            rx="2" ry="2"
            :fill="item.color"
            data-count="0" data-date="2017-11-19">
          </rect>
        </g>
      </g>
    </svg>
  </v-container>
</template>

<script>
  export default {
    name: "activity-canvas",
    props: {
      yayStances: {
        type: Array,
        required: true
      },
      nayStances: {
        type: Array,
        required: true
      },
      abstainStances: {
        type: Array,
        required: true
      },
    },
    data() {
      return {
        countOfItemsOnDashboard: 300,
        board: [],
        width: 0,
        height: 0,
      }
    },
    created() {
      this.recalculateBoard()
    },
    computed: {
      colsCountPerPage () {
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return 20
          case 'sm': return 30
          case 'md': return 50
          case 'lg': return 60
          case 'xl': return 60
        }
      },
      rowsCountPerPage() {
        return this.countOfItemsOnDashboard / this.colsCountPerPage
      },
      cachedMapPositions() {
        return this.$store.getters['influencer/cachedMapPositions'];
      },
      isStancesLoaded() {
        return this.yayStances && this.nayStances && this.abstainStances;
      }
    },
    methods: {
      createBoard() {
        let vm = this;
        let yayIndexes = this.yayStances.filter(s => s.influencer).map(s => vm.cachedMapPositions[s.influencer.id])
        let nayIndexes = this.nayStances.filter(s => s.influencer).map(s => vm.cachedMapPositions[s.influencer.id])
        let abstainIndexes = this.abstainStances.filter(s => s.influencer).map(s => vm.cachedMapPositions[s.influencer.id])

        const board = [];
        for (let c=0; c<this.colsCountPerPage; c++) {
          let col = [];
          for (let r=0; r<this.rowsCountPerPage; r++) {
            let index = c * this.rowsCountPerPage + r;
            let item = {}
            if (yayIndexes.includes(index)) {
              item = { title: 'yay', color: '#45C299' }
            } else if (nayIndexes.includes(index)) {
              item = { title: 'nay', color: '#F03D3D' }
            } else if (abstainIndexes.includes(index)) {
              item = { title: 'abstain', color: '#969696' }
            } else {
              item = { title: 'not filled', color: '#E8E8E8' }
            }
            col.push(item)
          }
          board.push(col)
        }

        return board
      },
      recalculateBoard() {
        if (!this.cachedMapPositions) return;

        this.board = this.createBoard()
        this.width = this.colsCountPerPage * 15;
        this.height = this.rowsCountPerPage * 15;
      },
    },
    watch: {
      rowsCountPerPage(newValue) {
        this.recalculateBoard()
      },
      cachedMapPositions(newValue) {
        this.recalculateBoard()
      },
      cachedMapPositions(newValue) {
        this.recalculateBoard()
      },
      yayStances(newValue) {
        this.recalculateBoard()
      },
      nayStances(newValue) {
        this.recalculateBoard()
      },
      abstainStances(newValue) {
        this.recalculateBoard()
      }
    }
  }
</script>

<style scoped>

</style>
