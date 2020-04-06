<template>
  <base-echarts :opt="options"></base-echarts>
</template>

<script>
    import BaseEcharts from 'components/common/figure/BaseEcharts'
    import * as CUSTOM from './WordCloudCustom'
    const MaskImg = new Image()
    MaskImg.src = CUSTOM.img
    export default {
        name: "WordCloud",
        components: {
            BaseEcharts
        },
        props: {
            SeriesData: {
                type: Array,
                default: () => []
            },
            GridSize: {
                type: Number
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
                        type: 'wordCloud',
                        maskImage: MaskImg,
                        sizeRange: [15, 30],
                        rotationRange: [-90, 90],
                        rotaionStep: 30,
                        gridSize: this.GridSize,
                        drawOutOfBound: false,
                        textStyle: {
                            normal: {
                                fontFamily: 'Microsoft YaHei',
                                fontWeight: 300,
                                color: () => {
                                    let index = Math.floor(Math.random() * CUSTOM.color.length)
                                    return CUSTOM.color[index]
                                }
                            }
                        },
                        data: this.SeriesData
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

<style scoped>

</style>