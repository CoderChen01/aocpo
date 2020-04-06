<template>
  <el-table
    :data="FalseTasksData"
    :stripe="false"
    style="width: 100%;"
    max-height="720">
    <el-table-column
      label="任务"
      min-width="200">
      <template v-slot="item">
        <i class="el-icon-data-analysis"></i>
        <span style="margin-left: 10px;">{{item.row.school}}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="创建日期"
      min-width="250">
      <template v-slot="item">
        <i class="el-icon-date"></i>
        <span style="margin-left: 10px;">{{item.row.created_date}}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="更新日期"
      min-width="250">
      <template v-slot="item">
        <span v-if="item.row.updated_date">
          <i class="el-icon-date"></i>
          <span style="margin-left: 10px;">{{item.row.updated_date}}</span>
        </span>
        <span v-else>
          <span>暂未获取数据</span>
        </span>
      </template>
    </el-table-column>
    <el-table-column
      label="操作"
      min-width="200">
      <template v-slot="item">
        <el-button
          size="mini"
          type="primary"
          @click="HandleRecover(item.$index)">恢复</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="HandleDel(item.$index)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
  import {RECOVERTASK, FALSETASKDEL} from "store/MethodsManager"
  import * as TaskBinRes from "network/TaskManager/TaskBin"

  export default {
      name: "FalseTask",
      computed: {
          FalseTasksData(){
              return this.$store.state.FalseTasksList
          }
      },
      methods: {
          HandleRecover(index){
              this.$confirm('是否恢复？', '警告', {
                  cancelButtonText: '否',
                  confirmButtonText: '是',
                  type: 'warning'
              })
                  .then(() => {
                      const _school = this.FalseTasksData[index].school
                      const _username = this.$store.state.UserInfo.username
                      const _opt = {school: _school, username: _username}
                      TaskBinRes.RecoverTask(_opt)
                          .then(res => {
                              if (res.status == 1002){
                                  this.$store.commit(RECOVERTASK, index)
                                  this.$message({
                                      type: 'success',
                                      message: '恢复成功',
                                      duration: 2000,
                                      center: true
                                  })
                              } else {
                                  this.$message({
                                      type: 'error',
                                      message: '服务器异常， 请联系管理员!',
                                      duration: 2000,
                                      center: true
                                  })
                              }
                          })
                          .catch(err => {
                              this.$message({
                                  type: 'error',
                                  message: '服务异常, 请联系管理员!',
                                  duration: 2000,
                                  center: true
                              })
                              console.log(err)
                          })
                  })
                  .catch(() => {
                      this.$message({
                          type: 'info',
                          message: '已取消恢复',
                          duration: 1000,
                          center: true
                      })
                  })
          },
          HandleDel(index){
              this.$confirm('是否删除？', '警告', {
                  cancelButtonText: '否',
                  confirmButtonText: '是',
                  type: 'warning'
              })
                  .then(() => {
                      const _school = this.FalseTasksData[index].school
                      const _username = this.$store.state.UserInfo.username
                      const _opt = {school: _school, username: _username, isDel: 1}
                      TaskBinRes.TrueDelTask(_opt)
                          .then(res => {
                              if (res.status == 1003){
                                  this.$store.commit(FALSETASKDEL, index)
                                  this.$message({
                                      type: 'success',
                                      message: '删除成功',
                                      duration: 2000,
                                      center: true
                                  })
                              } else {
                                  this.$message({
                                      type: 'error',
                                      message: '服务器异常， 请联系管理员!',
                                      duration: 2000,
                                      center: true
                                  })
                              }
                          })
                          .catch(err => {
                              this.$message({
                                  type: 'error',
                                  message: '服务异常, 请联系管理员!',
                                  duration: 2000,
                                  center: true
                              })
                              console.log(err)
                          })
                  })
                  .catch(() => {
                      this.$message({
                          type: 'info',
                          message: '已取消删除',
                          duration: 1000,
                          center: true
                      })
                  })
          }
      }
  }
</script>

<style scoped>

</style>