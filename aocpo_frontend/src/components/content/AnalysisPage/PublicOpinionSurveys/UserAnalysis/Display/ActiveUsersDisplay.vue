<template>
  <display-layout>
    <template #title>
      活跃用户
      <el-tooltip
        class="help"
        effect="dark"
        content="在所有数据中发帖数最多的前十位用户"
        placement="right">
        <i class="el-icon-question" style="color: #409EFF;font-size: 15px"></i>
      </el-tooltip>
    </template>
    <template #body>
      <bar :XAxisData="XData" :SeriesData="YData" XName="用户名" YName="总发帖数" @click="HandleClick"></bar>
    </template>
  </display-layout>
</template>

<style scoped>
</style>

<script>
  import bar from 'components/common/figure/Charts/bar'
  import DisplayLayout from '../../DisplayLayout'
  export default {
      name: "ActiveUsersDisplay",
      props: {
          XData: {
              type: Array,
              default: []
          },
          YData: {
              type: Array,
              default: []
          }
      },
      components: {
          DisplayLayout,
          bar
      },
      methods: {
          HandleClick(params) {
              window.open('http://tieba.baidu.com/home/main?un=' + encodeURIComponent(params.name))
          }
      }
  }
</script>
