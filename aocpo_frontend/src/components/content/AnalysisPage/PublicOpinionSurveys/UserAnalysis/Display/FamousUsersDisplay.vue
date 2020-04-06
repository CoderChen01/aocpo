<template>
  <display-layout>
    <template #title>
      受关注用户
      <el-tooltip
        class="help"
        effect="dark"
        content="在所有数据中粉丝数最多的前十位用户"
        placement="right">
        <i class="el-icon-question" style="color: #409EFF;font-size: 15px"></i>
      </el-tooltip>
    </template>
    <template #body>
      <bar :XAxisData="XData" :SeriesData="YData" XName="用户名" YName="粉丝数" @click="HandleClick"></bar>
    </template>
  </display-layout>
</template>

<style scoped>
  .title {
    padding-left: 8px;
    line-height: 1;
    border-left: 4px solid #0095eb;
  }
</style>

<script>
  import bar from 'components/common/figure/Charts/bar'
  import DisplayLayout from '../../DisplayLayout'
  export default {
      name: "FamousUsersDisplay",
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
          bar,
          DisplayLayout
      },
      methods: {
          HandleClick(params) {
              window.open('http://tieba.baidu.com/home/main?un=' + encodeURIComponent(params.name))
          }
      }
  }
</script>

