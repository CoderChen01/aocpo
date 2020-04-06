<template>
  <display-layout>
    <template #title>
      新老用户比例
      <el-tooltip
        class="help"
        effect="dark"
        content="吧龄低于1年的为新用户"
        placement="right">
        <i class="el-icon-question" style="color: #409EFF;font-size: 15px"></i>
      </el-tooltip>
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
      name: "OldAndNewScaleDisplay",
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