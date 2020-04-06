<template>
  <el-table
    :data="TaskData"
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
      label="当前状态"
      min-width="200">
      <template v-slot="item">
        <span class="LoadingState" v-if="item.row.running == 1">
          <i class="el-icon-loading"></i>
          <span style="margin-left: 10px;">数据获取中</span>
        </span>
        <span class="SuccessState" v-else-if="item.row.state == 1">
          <i class="el-icon-finished"></i>
          <span style="margin-left: 10px">任务已完成</span>
        </span>
        <span v-else>
          <i class="el-icon-top Times"></i>
          <span style="margin-left: 10px;"><span class="di">第 </span><span class="Times">{{item.row.state - 1}}</span> <span class="cigengxin">次更新</span></span>
        </span>
      </template>
    </el-table-column>
    <el-table-column
      label="操作"
      min-width="200">
      <template v-slot="item">
        <el-button
          size="mini"
          type="success"
          @click="HandleAnalyse(item.row)">分析</el-button>
        <el-button
          size="mini"
          type="primary"
          @click="HandleUpdate(item.$index, item.row)">更新</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="HandleDel(item.$index, item.row.running)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
  import * as MyTaskRes from 'network/TaskManager/MyTask'
  import {MYTASKDEL,UPDATETASK} from 'store/MethodsManager'
  export default {
      name: "MyTask",
      methods: {
          HandleAnalyse(ItemObj){
              if (!ItemObj.running) {
                  const _payload = {
                      username: this.$store.state.UserInfo.username,
                      school: ItemObj.school
                  }
                  this.$cookies.set('Task', _payload)
                  this.$router.push({name: 'yuqing'})
              } else {
                  this.$message({
                      type: 'warning',
                      message: '任务还未完成',
                      duration: 2000,
                      center: true
                  })
              }
          },
          HandleUpdate(index, ItemObj){
              this.$confirm('是否更新任务？', '警告', {
                  cancelButtonText: '否',
                  confirmButtonText: '是',
                  type: 'warning'
              })
                  .then(() => {
                      if(ItemObj.running){
                          this.$message({
                              type: 'warning',
                              message: '任务正在进行中, 请耐心等待',
                              duration: 2000,
                              center: true
                          })
                      } else {
                          const username = this.$store.state.UserInfo.username
                          const school = ItemObj.school
                          const scale = 1000
                          const opt = {username, school, scale}
                          MyTaskRes.UpdateTask(opt)
                              .then(res => {
                                  if (res.status == 1002) {
                                      this.$store.commit(UPDATETASK, index)
                                      this.$message({
                                          type: 'success',
                                          message: '提交更新任务成功',
                                          duration: 1500,
                                          center: true
                                      })
                                  } else {
                                      this.$message({
                                          type: 'error',
                                          message: '服务器错误， 请联系管理员',
                                          duration: 2000,
                                          center: true
                                      })
                                  }
                              })
                              .catch(err => {
                                  this.$message({
                                      type: 'error',
                                      message: '服务器错误， 请联系管理员',
                                      duration: 2000,
                                      center: true
                                  })
                                  console.log(err)
                              })
                      }
                  })
                  .catch(() => {
                      this.$message({
                          type: 'info',
                          message: '已取消更新任务',
                          duration: 1000,
                          center: true
                      })
                  })
          },
          HandleDel(index, flag){
              if(!flag){
                  this.$confirm('是否删除？', '警告', {
                      cancelButtonText: '否',
                      confirmButtonText: '是',
                      type: 'warning'
                  })
                      .then(() => {
                          const _school = this.TaskData[index].school
                          const _username = this.$store.state.UserInfo.username
                          const _opt = {school: _school, username: _username, isDel: 0}
                          MyTaskRes.FalseDelTask(_opt)
                              .then(res => {
                                  if (res.status == 1003){
                                      this.$store.commit(MYTASKDEL, index)
                                      this.$cookies.remove('Task')
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
              } else {
                  this.$message({
                      type: 'warning',
                      message: '任务正在进行中',
                      duration: 2000,
                      center: true
                  })
              }
          }
      },
      computed: {
          TaskData(){
              return this.$store.state.TasksList
          }
      }
  }
</script>

<style scoped>
  .Times{
    color: #F56C6C;
  }
  .LoadingState {
    color: #409EFF;
  }
  .SuccessState {
    color: #67C23A;
  }
  .di,.cigengxin {
    color:  #67C23A;
  }
</style>