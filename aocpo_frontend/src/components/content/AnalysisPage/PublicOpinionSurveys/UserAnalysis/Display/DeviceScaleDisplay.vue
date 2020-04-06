<template>
  <display-layout>
    <template #title>
      移动设备比例
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
      name: "DeviceScaleDisplay",
      props: {
          data: {
              type: Array,
              default: []
          }
      },
      components: {
          pie,
          DisplayLayout
      }
  }
</script>

<style scoped>

</style>