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
            fill="#ebedf0"
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
    data() {
      return {
        countOfItemsOnDashboard: 300,
        board: [],
        width: 0,
        height: 0
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
      }
    },
    methods: {
      createBoard() {
        const board = [];
        for (let c=0; c<this.colsCountPerPage; c++) {
          let col = [];
          for (let r=0; r<this.rowsCountPerPage; r++) {
            col.push({
              title: 'nana'
            })
          }
          board.push(col)
        }
        return board
      },
      recalculateBoard() {
        this.board = this.createBoard()

        this.width = this.colsCountPerPage * 15;
        this.height = this.rowsCountPerPage * 15;

        console.log("Naaa width " + this.width)
        console.log("Naaa height " + this.height)
      }
    },
    watch: {
      rowsCountPerPage(newValue) {
        this.recalculateBoard()
      }
    }
  }
</script>

<style scoped>

</style>
