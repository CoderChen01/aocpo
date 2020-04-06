<template>
  <word-cloud :SeriesData="data" :GridSize="9"></word-cloud>
</template>

<script>
  import WordCloud from 'components/common/figure/Charts/WordCloud'
  export default {
      name: "ContentHotWordsDisplayWordCloud",
      props: {
          data: {
              type: Array,
              default: []
          }
      },
      components: {
          WordCloud
      }
  }
</script>

<style scoped>

</style>