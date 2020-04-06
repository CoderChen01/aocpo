<template>
  <base-echarts :opt="options" v-on="$listeners"></base-echarts>
</template>


<style scoped>

</style>

<script>
  import BaseEcharts from 'components/common/figure/BaseEcharts'
  export default {
      name: "bar",
      components: {
          BaseEcharts
      },
      props: {
          SeriesData: {
              type: Array,
              default: []
          },
          XAxisData: {
              type: Array,
              default: []
          },
          XName: {
              type: String,
              default: null
          },
          YName: {
              type: String,
              default: null
          }
      },
      data(){
          return {
              options: {
                  tooltip: {
                      show: true,
                      trigger: 'axis',
                      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                          type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                      }
                  },
                  toolbox: {
                      show: true,
                      showTitle: false,
                      feature: {
                          saveAsImage: {
                              show: true,
                              title: '保存图片'
                          }
                      }
                  },
                  xAxis: {
                      type: 'category',
                      data: this.XAxisData,
                      name: this.XName,
                      axisTick: {
                          alignWithLabel: true
                      },
                      axisLabel: {
                          fontSize: 15
                      }
                  },
                  yAxis: {
                      type: 'value',
                      name: this.YName
                  },
                  series: {
                      data: this.SeriesData,
                      type: 'bar',
                  }
              }
      }
      },
      watch: {
          'SeriesData': function (val, oldVal) {
              if(val !== oldVal) {
                  this.options.series.data = val
              }
          },
          'XAxisData': function (val, oldVal) {
              if(val !== oldVal) {
                  this.options.xAxis.data = val
              }
          }
      }
  }
</script>
