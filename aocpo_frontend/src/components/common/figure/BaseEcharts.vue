<template>
  <div class="container" ref="container" style="width: 700px; height: 300px;"></div>
</template>

<style scoped>
</style>

<script>
  import echarts from '@/echarts'
  import mytheme from 'assets/js/mytheme'
  export default {
      name: "BaseEcharts",
      props: {
          opt: Object
      },
      methods: {
          InitChart(){
              const Chart = echarts.init(this.$refs.container, 'mytheme')
              Chart.setOption(this.opt || {})
              Object.keys(this.$listeners).forEach(event => {
                  const handler = this.$listeners[event]
                  Chart.on(event, handler)
              })
              this.Chart = Chart
          }
      },
      watch: {
        opt: {
            handler(newVal) {
                this.Chart.setOption(newVal)
            },
            deep: true
        }
      },
      mounted() {
          this.InitChart()
      },
      destroyed() {
          this.Chart.dispose()
      }
  }
</script>

