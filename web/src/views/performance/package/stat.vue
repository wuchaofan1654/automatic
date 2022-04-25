<template>
  <line-chart v-if="xAsia.length > 0" :x-axis="xAsia" :y-axis="yAsia" height="1000px"></line-chart>
</template>

<script>
import LineChart from "../../dashboard/LineChart";
import {get_module_stat} from "@/api/performance/module"
export default {
name: "stat",
  components: {LineChart},
  data() {
    return {
      loading: false,
      xAsia: [],
      yAsia: {}
    }
  },
  created() {
    this.$nextTick(function () {
      this.statData()
    })
  },
  methods: {
    statData() {
      this.loading = true
      get_module_stat().then(res => {
        this.loading = false
        this.xAsia = res.data.xAsia
        this.yAsia = res.data.yAsia
        console.log(this.xAsia)
      })
    }
  }
}
</script>

<style scoped>

</style>
