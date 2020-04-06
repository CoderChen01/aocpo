<template>
  <display-layout>
    <template #title>
      男女比例
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
      name: "ManFemaleScaleDisplay",
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

