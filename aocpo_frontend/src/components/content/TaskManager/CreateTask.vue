<template>
  <el-container>
    <el-header>
      <img src="~assets/img/CreateTask/CT_logo.png" alt="logo">
    </el-header>
    <el-main>
      <el-row>
        <el-autocomplete
          :trigger-on-focus="false"
          :fetch-suggestions="SearchSchool"
          @select="HandleSelect"
          ref="TaskInput"
          @blur="CheckWord"
          placeholder="请输入学校"
          style="width: 100%"
          v-model="school"
          clearable>
          <template v-slot="{item}">
            <span v-if="item._null">对不起没有找到您输入的院校。</span>
            <span v-else>
              <span class="school" >{{item.school}}</span>
              <span class="ranking" >{{'全国排名: ' + item.ranking}}</span>
            </span>
          </template>
        </el-autocomplete>
      </el-row>
      <el-row>
        <el-button
          type="primary"
          style="width: 100%"
          :disabled="IsDisabled"
          v-loading.fullscreen.lock="FullLoading"
          @click="HandleTask">
          提交任务
        </el-button>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
  import * as TaskRes from 'network/TaskManager/CreateTask'
  import {CREATETASK} from 'store/MethodsManager'
  export default {
      name: "CreateTask",
      data(){
          return {
              school: "",
              IsSchool: false,
              IsDisabled: true,
              FullLoading: false,
              SuggestionsRecord: "",
              SchoolSuggestions: []
          }
      },
      methods:{
          CheckWord(){
              let _re = /^[\u4e00-\u9fa5]{1,15}$/g
              let _res = _re.test(this.school)
              if (!_res) {
                  this.IsDisabled = true
                  this.$message({
                      type: 'error',
                      message: '输入内容只能包含中文/输入内容过长',
                      duration: 2000,
                      center: true
                  })
              } else {
                  this.IsDisabled = false
              }
          },
          _Requset(_data){
              this.FullLoading = true
              TaskRes.HandleTask(_data)
                  .then(_res => {
                      if (_res.status == 1001) {
                          this.$store.dispatch(CREATETASK)
                          this.FullLoading = false
                          this.$message({
                              type: 'success',
                              message: '任务提交成功',
                              duration: 1500,
                              center: true
                          })
                      } else {
                          this.FullLoading = false
                          this.$message({
                              type: 'error',
                              message: '服务异常，请联系管理员！',
                              duration: 2000,
                              center: true
                          })
                      }
                  })
                  .catch(err => {
                      this.FullLoading = false
                      this.$message({
                          type: 'error',
                          message: '服务异常，请联系管理员！',
                          duration: 2000,
                          center: true
                      })
                      console.log(err)
                  })
          },
          HandleTask(){
              if (!this.school){
                  this.$message({
                      type: 'error',
                      message: '学校名不能为空',
                      duration: 2000,
                      center: true
                  })
              } else {
                  const school1 = this.$store.state.TasksList.map(obj => obj.school)
                  const school2 = this.$store.state.FalseTasksList.map(obj => obj.school)
                  const schools = school1.concat(school2)
                  if (schools.indexOf(this.school) != -1){
                      this.$message({
                          type: 'warning',
                          message: '你已有此任务在 (我的任务 / 任务垃圾箱) 中',
                          duration: 2000,
                          center: true
                      })
                  } else{
                      let _SetObj = new Set(this.SuggestionsRecord)
                      this.IsSchool = _SetObj.has(this.school)
                      if (!this.IsSchool) {
                          this.$confirm('提交未知院校或其他无关字符，可能会造成分析结果异常，是否继续（建议取消操作）',
                              '警告', {
                                  confirmButtonText: '是',
                                  cancelButtonText: '否',
                                  type: 'warning'
                              })
                              .then(() => {
                                  //提交任务
                                  this._Requset({
                                      'username': this.$store.state.UserInfo.username,
                                      'school': this.school,
                                      'scale': 20000
                                  })
                              })
                              .catch(() => {
                                  this.$message({
                                      type: 'info',
                                      message: '取消成功',
                                      duration: 2000,
                                      center: true
                                  })
                              })
                      } else {
                          //提交任务
                          this._Requset({
                              'username': this.$store.state.UserInfo.username,
                              'school': this.school,
                              'scale': 20000
                          })
                      }
                  }
              }
          },
          SearchSchool(word, cb) {
              TaskRes.SearchSchool(word)
                  .then(res => {
                      if(res.status == 1000){
                          let _res = res.data
                          this.SuggestionsRecord = _res.map(obj => obj.school) /*记录搜索到结果之后对比，以防调皮的用户
                                                                                  瞎操作*/
                          cb(_res)
                      } else {
                          if (res.status == 2000){
                              this.IsSchool = false
                              cb([{_null: true}])
                          }
                          else {
                              this.$message({
                                  type: 'error',
                                  message: '服务器可能存在异常，请联系管理员！',
                                  duration: 2000,
                                  center: true
                              })
                          }
                      }
                  })
                  .catch(err => {
                      this.$message({
                          type: 'error',
                          message: '服务器可能存在异常，请联系管理员！',
                          duration: 2000,
                          center: true
                      })
                      console.log(err);
                  })
          },
          HandleSelect(item) {
              //有内容帮忙填
              if(item.school){
                  this.school = item.school
              }
          }
      },
      mounted() {
          this.$refs.TaskInput.focus() //增强用户体验
      }
  }
</script>

<style scoped>
  .el-container{
    width: 414px;
    height: 515px;
    background-color: rgb(255, 255, 255);
    border-radius: 3px;
    box-shadow: 0 3px 9px rgba(0,0,0,.5);
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
  }
  .el-header > img {
    margin-left: 122px;
  }
  .el-header {
    margin-top: 80px;
    margin-bottom: 100px;
  }
  .el-row {
    margin-bottom: 40px;
  }
  .school {
    text-overflow: ellipsis;
    overflow: hidden;
  }
  .ranking {
    float:right;
    font-size: 12px;
    color: #b4b4b4;
  }


</style>