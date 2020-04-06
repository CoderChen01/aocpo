<template>
  <display-layout>
    <template #title>
      文章类型
    </template>
    <template #body>
      <pie :SeriesData="data"></pie>
    </template>
  </display-layout>
</template>

<script>
  import DisplayLayout from '../../DisplayLayout'
  import pie from 'components/common/figure/Charts/pie'
  export default {
      name: "ClassifyDIsplay",
      props: {
          data: {
              type: Array,
              default: []
          }
      },
      components: {
          DisplayLayout,
          pie
      }
  }
</script>

<style scoped>

</style>