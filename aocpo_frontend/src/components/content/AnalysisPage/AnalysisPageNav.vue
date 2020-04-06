<template>
  <aside-main-layout>
    <template #nav>
      <el-menu
        :default-active="$route.path"
        :router="true"
        class="AnalysisNav"
        background-color="#0d0d2b"
        text-color="#fff"
        active-text-color="#01BDD4">
        <div class="logo">
          <img src="~assets/img/AnalysisPage/logo/logo.png" alt="logo" style="width: 80px; height: 80px;">
          <div style="font-size: 25px; color: #ffffff; width: 180px; position: absolute; right: -70px; top: 80px;">校园舆情分析</div>
        </div>
        <div class="ManageTask">
          <button class="btn" @click="GoBack">
            <i class="el-icon-menu"></i>
            <span style="margin-left: 10px">任务管理</span>
          </button>
        </div>
        <span class="CurrentTask">
          <i class="el-icon-s-data" style="color: #01BDD4; font-size: 18px;"></i>
          <span style="margin-left: 7px; cursor: pointer" @click="GoToSearch(CurrentTask)">{{CurrentTask}}</span>
        </span>
        <div class="MenuItem">
          <el-menu-item
            index="/aocpo/AnalysisPage/PublicOpinionSurveys">
          <span class="item">
            <i class="el-icon-data-analysis" style="font-size: 18px;"></i>
            <span style="color: #fff">舆情总览</span>
          </span>
          </el-menu-item>
          <el-menu-item
            index="/aocpo/AnalysisPage/InfomationGather">
          <span class="item">
            <i class="el-icon-chat-dot-square" style="font-size: 19px;"></i>
            <span style="color: #fff" >信息汇总</span>
          </span>
          </el-menu-item>
        </div>
      </el-menu>
    </template>
    <template #main>
      <slot name="main"></slot>
    </template>
  </aside-main-layout>
</template>

<script>
  import AsideMainLayout from 'components/common/Layout/AnalysisPageLayout'
  export default {
      name: "AnalysisPageNav",
      props: ['CurrentTask'],
      methods: {
          GoBack(){
            this.$router.push({name: 'task_manager'})
          },
          GoToSearch(word) {
              window.open('https://www.baidu.com/s?wd=' + encodeURIComponent(word))
          }
      },
      components: {
          AsideMainLayout
      }
  }
</script>

<style scoped>

  .AnalysisNav {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    width: 200px;
  }
  .item {
    font-size: 15px;
    position: absolute;
    bottom: -2px;
  }
  .MenuItem {
    position: absolute;
    top: 35%;
  }
  .logo{
    position: absolute;
    left: 50px;
    top: 10px;
    user-select: none;
  }
  .btn {
    border: 1px solid #0095eb;
    color: #0095eb;
    background: 0;
    font-size: 15px;
    border-radius: 2px;
    padding: 10px;
    cursor: pointer;
  }
  .ManageTask {
    position: absolute;
    left: 35px;
    top: 160px;
  }
  .CurrentTask {
    position: absolute;
    top: 230px;
    left: 25px;
    display: inline-block;
    color: #ffffff;
    font-size: 18px;
    margin-left: 8px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    width: 150px;
    user-select: none;
  }
  .el-menu-item{
    margin-bottom: 70px;
    width: 200px;
    user-select: none;
  }
  .el-menu-item:hover{
    background-color: transparent !important;
  }
  .el-menu-item.is-active{
    background-image: url('~assets/img/AnalysisPage/Nav/nav.png') !important;
  }
</style>