<template>
  <word-cloud :SeriesData="data" :GridSize="12"></word-cloud>
</template>

<script>
  import WordCloud from 'components/common/figure/Charts/WordCloud'
  export default {
      name: "NickNameHotWordDisplayWordCloud",
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

