<template>
  <el-card>
    <template #header>
      <div class="header">
        <h2 class="title">
          文章热词
          <el-tooltip
            class="help"
            effect="dark"
            content="所有数据中所有帖子中出现次数较多的字词"
            placement="right">
            <i class="el-icon-question" style="color: #409EFF;font-size: 15px"></i>
          </el-tooltip>
        </h2>
        <span class="DropDown">
          <el-dropdown @command="HandleCommand" trigger="click">
            <span class="ChartClass">
              图标类型<i class="el-icon-arrow-down"></i>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item :command="0">词云图</el-dropdown-item>
                <el-dropdown-item :command="1">饼图</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </span>
      </div>
    </template>
    <content-hot-words-display-word-cloud :data="data" v-if="IsShow"></content-hot-words-display-word-cloud>
    <content-hot-words-display-pie :data="data" v-else></content-hot-words-display-pie>
  </el-card>
</template>

<style scoped>
  .title {
    display: inline-block;
    padding-left: 8px;
    line-height: 1;
    border-left: 4px solid #0095eb;
  }
  .DropDown {
    margin-left: 40px;
  }
  .ChartClass {
    font-size: 15px;
    color: #409EFF;
    cursor: pointer;
  }
</style>

<script>
  import ContentHotWordsDisplayPie from './ContentHotWordsDisplayPie'
  import ContentHotWordsDisplayWordCloud from './ContentHotWordsDisplayWordCloud'
  export default {
      name: "ContentHotWordsDisplay",
      components: {
          ContentHotWordsDisplayWordCloud,
          ContentHotWordsDisplayPie
      },
      props: {
          data: {
              type: Array,
              default: []
          }
      },
      data(){
          return {
              IsShow: true
          }
      },
      methods: {
          HandleCommand(command) {
              if(command === 0) {
                  this.IsShow = true
              } else {
                  this.IsShow = false
              }
          }
      }
  }
</script>

