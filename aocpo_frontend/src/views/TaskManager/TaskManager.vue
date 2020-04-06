<template>
  <task-manager-base>
    <template #nickname>
      <span class="nickname">
        <i class="el-icon-user-solid"></i>
        <span class="placeholder"></span>
        <span>{{'欢迎您：' + nickname}}</span>
        <el-link type="danger"
                 :underline="false"
                 class="layout"
                 @click="Layout">[ 退出 ]</el-link>
      </span>
    </template>
    <template #MyTask>
      <div class="MyTask">
        <my-task></my-task>
      </div>
    </template>
    <template #CreateTask>
      <div class="CTWrapper">
          <create-task></create-task>
      </div>
    </template>
    <template #FalseTask>
      <div class="FalseTask">
        <false-task></false-task>
      </div>
    </template>
  </task-manager-base>
</template>

<script>
  import TaskManagerBase from 'components/content/TaskManager/TaskManagerBase'
  import CreateTask from 'components/content/TaskManager/CreateTask'
  import MyTask from 'components/content/TaskManager/MyTask'
  import FalseTask from 'components/content/TaskManager/FalseTask'
  import {GetTasks} from 'network/TaskManager/MyTask'
  import {LOGOUT, GETTASKSLIST, GETTASKSFALSELIST} from 'store/MethodsManager'
  export default {
      name: "TaskManager",
      components: {
          FalseTask,
          TaskManagerBase,
          CreateTask,
          MyTask
      },
      data(){
        return {
            Monitor: null
        }
      },
      methods: {
          Layout() {
              this.$confirm('确认退出？', '警告', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
              })
                  .then(() => {
                      this.$cookies.keys().forEach(cookie => this.$cookies.remove(cookie))
                      this.$store.commit(LOGOUT)
                      this.$router.push({name: 'login'})
                  })
                  .catch(() => {
                      this.$message({
                          type: 'info',
                          message: '您已取消退出',
                          duration: 1500,
                          center: true
                      })
                  })
          },
          _GetTask() {
              const _username = this.$store.state.UserInfo.username
              GetTasks(_username)
                  .then(res => {
                      if(res.status == 1000) {
                          this.$store.commit(GETTASKSLIST, res.data.true_data)
                          this.$store.commit(GETTASKSFALSELIST, res.data.false_data)
                      } else {
                          if (res.status != 2000) {
                              this.$message({
                                  type: 'error',
                                  message: '服务器异常， 请联系管理员！',
                                  duration: 2000,
                                  center: true
                              })
                          }
                      }
                  })
                  .catch(err => {
                      console.log(err)
                  })
          }
      },
      computed: {
          nickname() {
              return this.$store.state.UserInfo.nickname
          }
      },
      created() {
          this._GetTask()
          this.Monitor = setInterval(this._GetTask, 600000)
      },
      beforeDestroy() {
          clearInterval(this.Monitor)
      }
  }
</script>

<style scoped>
  .CTWrapper {
    background-image: url("~assets/img/CreateTask/CreateTask.png");
    background-position: 0 722px;
    padding: 103px 710px;
  }
  .nickname {
    float: right;
    position: relative;
    bottom: 20px;
    font-size: 15px;
  }
  .layout {
    display: inline-block;
    margin-bottom: 2px;
    margin-left: 15px;
  }
  .placeholder {
    display: inline-block;
    width: 10px;
  }

</style>