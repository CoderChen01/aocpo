<template>
  <login-register-layout>

    <template #logo>
      <slot name="logo"></slot>
    </template>

    <template #item>
      <el-row>
        <el-input
          placeholder="请输入手机号"
          v-model.lazy="username"
          minlength="6"
          maxlength="11"
          ref="UnInput"
          :disabled="isInputDisabled"
          @blur="CheckUnData"
          clearable>
        </el-input>
      </el-row>

      <el-row>
        <el-input
          placeholder="请输入密码"
          v-model.lazy="pwd"
          minlength="6"
          maxlength="16"
          :disabled="isInputDisabled"
          show-password>
        </el-input>
      </el-row>

      <el-row>
        <el-button
          type="primary"
          ref="LoginBtn"
          style="width: 100%"
          :disabled="isLoginBtnDisabled"
          v-loading.fullscreen.loc="fullscreenLoading"
          @click="Login">{{IsLoginText}}</el-button>
      </el-row>

      <el-row>
        <el-button
          type="primary"
          style="width: 100%"
          @click="Register">注册</el-button>
      </el-row>
    </template>

  </login-register-layout>
</template>

<script>
  import LoginRegisterLayout from 'components/common/Layout/LoginRegisterLayout'
  import LoginApi from 'network/LoginRegister/LoginApi'
  import {
      GET_USER_INFO,
      LOGIN} from 'store/MethodsManager'

  export default {
      name: "LoginModel",
      components: {
          LoginRegisterLayout
      },
      data(){
        return{
            username: "",
            pwd: "",
            isLoginBtnDisabled: this.IsLogin,
            isInputDisabled: this.IsLogin,
            fullscreenLoading: false
        }
      },
      computed: {
        IsLogin(){
            return this.$store.state.IsLogin
        },
       IsLoginText(){
            if(!this.IsLogin){
                return '登录'
            } else {
                return '你已登录'
            }
        }
      },
      methods:{
          _CheckUn(value){
              let re = /^1[3|5|7|8]\d{9}/g
              return re.test(value)
          },
          _CheckPw(value){
           return value.length >= 6 && value.length <= 16
          },
          CheckUnData(){
              if(!this._CheckUn(this.username)){
                  this.$message({
                      type: 'error',
                      message: '手机号输入有误！',
                      duration: 1500,
                      center: true
                  })
                  this.isLoginBtnDisabled = true
              } else {
                  this.isLoginBtnDisabled = false
              }
          },
          Login(){
              if(!this._CheckPw(this.pwd)){
                  this.$message({
                      type: 'error',
                      message: '密码不合法！',
                      duration: 1500,
                      center: true
                  })
              } else{
                  this.fullscreenLoading = true //打开loading
                  LoginApi({
                      username: this.username,
                      pwd: this.pwd
                  }).then(res => {
                      if(res.status == 1000){
                          //cookies设置
                          const _UserInfo = {
                              'username': res.username,
                              'nickname': res.nickname,
                              'aocpo_token': res.aocpo_token
                          }
                          this.$cookies.set('aocpo_cookies', _UserInfo) //设置cookie
                          this.$store.commit(GET_USER_INFO, _UserInfo) //保存用户信息到vuex
                          this.$store.commit(LOGIN) //改变登录状态
                          this.fullscreenLoading = false //关闭loading
                          this.$router.push({
                              name: 'task_manager',
                          }) //跳转到任务管理界面
                          this.$message({
                              type: 'success',
                              message: '登录成功',
                              duration: 1000,
                              center: true
                          })
                      } else if(res.status == 2000){
                          this.fullscreenLoading = false
                          this.$message({
                              type: 'error',
                              message: '验证失败，请检查用户名/密码是否正确！',
                              duration: 1500,
                              center: true
                          })
                      } else {
                          this.fullscreenLoading = false
                          this.$message({
                              type: 'warning',
                              message: '未知错误，请联系管理员！',
                              duration: 3000,
                              center: true
                          })
                      }
                  }).catch((err) => {
                      this.fullscreenLoading = false
                      this.$message({
                          type: 'warning',
                          message: '未知错误，请联系管理员！',
                          duration: 3000,
                          center: true
                      })
                      console.log(err)
                  })
              }
          },
          Register(){
              this.$router.push({name: 'register'})
          },
      },
      mounted() {
          this.$refs.UnInput.focus()
      },
      activated() {
          this.isInputDisabled = this.IsLogin
          this.isLoginBtnDisabled = this.IsLogin
      }
  }
</script>


