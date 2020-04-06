<template>
<base-echarts :opt="options"></base-echarts>
</template>


<style scoped>
</style>

<script>
  import BaseEcharts from 'components/common/figure/BaseEcharts'
  export default {
      name: "pie",
      components: {
          BaseEcharts
      },
      props: {
          SeriesData: {
              type: Array,
              default: []
          }
      },
      data(){
          return {
              options: {
                  tooltip: {
                      show: true
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
                  series: {
                      data: this.SeriesData,
                      type: 'pie',
                      radius: ['40%', '60%'],
                      itemStyle: {
                          shadowBlur: 30,
                          shadowOffsetX: 0,
                          shadowOffsetY: 0,
                          shadowColor: 'rgba(0,0,0,0.2)'
                      },
                      tooltip: {
                          formatter: '{b}: {c} ({d}%)'
                      },
                      label: {
                          fontSize: 15,
                          formatter: '{b}: {d}%'
                      }
                  }
              }
          }
      },
      watch: {
          'SeriesData': function (val, oldVal) {
              if(val !== oldVal) {
                  this.options.series.data = val
              }
          }
      }
  }
</script>

