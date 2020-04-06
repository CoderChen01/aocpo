<template>
  <task-manager-layout>
    <template #HeaderContent>
      <el-page-header @back="goBack">
        <template #title>
          <span> 返回</span>
        </template>
        <template #content>
          <i class="el-icon-edit"></i>
          <span>任务管理</span>
        </template>
      </el-page-header>
      <slot name="nickname"></slot>
    </template>
    <template #MainContent>
      <el-tabs type="border-card" v-model="activeName">
        <el-tab-pane label="我的任务" name="MyTask"><slot name="MyTask"></slot></el-tab-pane>
        <el-tab-pane label="新建任务" name="CreateTask"><slot name="CreateTask"></slot></el-tab-pane>
        <el-tab-pane label="任务垃圾箱" name="FalseTask"><slot name="FalseTask"></slot></el-tab-pane>
      </el-tabs>
    </template>
  </task-manager-layout>
</template>

<script>
  import TaskManagerLayout from 'components/common/Layout/TaskManagerLayout'
  export default {
      name: "TaskManagerBase",
      data(){
          return {
              activeName: 'MyTask'
          }
      },
      methods: {
          goBack(){
              this.$router.go(-1)
          }
      },
      components: {
          TaskManagerLayout
      }
  }
</script>