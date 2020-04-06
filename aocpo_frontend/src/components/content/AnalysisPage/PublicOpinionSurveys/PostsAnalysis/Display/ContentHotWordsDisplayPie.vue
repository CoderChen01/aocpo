<template>
  <pie :SeriesData="data.slice(0, 20)"></pie>
</template>

<script>
  import pie from 'components/common/figure/Charts/pie'
  export default {
      name: "ContentHotWordsDisplay",
      props: {
          data: {
              type: Array,
              default: []
          }
      },
      components: {
          pie
      }
  }
</script>
