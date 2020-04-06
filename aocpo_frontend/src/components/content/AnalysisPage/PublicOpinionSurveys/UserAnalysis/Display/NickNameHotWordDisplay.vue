<template>
  <el-card style="width: 1530px" :body-style="{marginLeft: '380px'}">
    <template #header>
      <div class="header">
        <h2 class="title">
          昵称常用字词
          <el-tooltip
            class="help"
            effect="dark"
            content="所有数据中所有用户昵称中出现次数较多的字词"
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
    <nick-name-hot-word-display-word-cloud :data="data" v-if="IsShow"></nick-name-hot-word-display-word-cloud>
    <nick-name-hot-word-display-pie :data="data" v-else></nick-name-hot-word-display-pie>
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
  import NickNameHotWordDisplayPie from './NickNameHotWordDisplayPie'
  import NickNameHotWordDisplayWordCloud from './NickNameHotWordDisplayWordCloud'
  export default {
      name: "NickNameHotWordDisplay",
      components: {NickNameHotWordDisplayPie, NickNameHotWordDisplayWordCloud},
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
