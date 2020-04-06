<template>
  <display-layout>
    <template #title>
      热门帖子
      <el-tooltip
        class="help"
        effect="dark"
        content="所有数据中帖子回复数量较多的前10个帖子"
        placement="right">
        <i class="el-icon-question" style="color: #409EFF;font-size: 15px"></i>
      </el-tooltip>
    </template>
    <template #body>
      <bar :XAxisData="XData" :SeriesData="YData" XName="排名" YName="帖子回复数" @click="HandleClick"></bar>
    </template>
  </display-layout>
</template>

<script>
  import bar from 'components/common/figure/Charts/bar'
  import DisplayLayout from '../../DisplayLayout'
  export default {
      name: "HotPostsDisplay",
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
              const tid = params.data.name
              window.open(`http://tieba.baidu.com/p/${tid}`)
          }
      }
  }
</script>
