<template>
  <login-register-layout>

    <template #logo>

      <slot name="logo"></slot>

    </template>

    <template #item>

      <el-row>
        <el-input
          placeholder="手机号"
          v-model="username"
          minlength="6"
          maxlength="11"
          ref="UnInput"
          @blur="CheckUnData"
          clearable>
        </el-input>
      </el-row>

      <el-row>
        <el-input
          placeholder="昵称"
          v-model="nickname"
          maxlength="20"
          clearable>
        </el-input>
      </el-row>

      <el-row>
        <el-input
          placeholder="密码"
          v-model="pwd"
          minlength="6"
          maxlength="16"
          show-password>
        </el-input>
      </el-row>

      <el-row>
        <el-button
          type="primary"
          style="width: 100%"
          @click="Register"
          :disabled="isRegisterBtnDisabled">注册</el-button>
      </el-row>

    </template>

  </login-register-layout>
</template>

<script>
  import LoginRegisterLayout from 'components/common/Layout/LoginRegisterLayout'
  import * as Register from 'network/LoginRegister/RegisterApi'
  export default {
      name: "RegisterModel",
      components: {
          LoginRegisterLayout
      },
      data(){
        return{
            username: "",
            pwd: "",
            nickname: "",
            isRegisterBtnDisabled: true
        }
      },
      methods: {
          _CheckUn(value){
              let re = /^1[3|5|7|8]\d{9}/g
              return re.test(value)
          },
          _CheckNickname(value){
              let re = /^[0-9a-zA-Z\u4e00-\u9fa5]{1,10}$/g
              return re.test(value)
          },
          _CheckPw(value){
              let re = /[^\u4e00-\u9fa5]{6,16}/g
              return re.test(value)
          },
          CheckUnData(){
              if(!this._CheckUn(this.username)){
                  this.isRegisterBtnDisabled = true
                  this.$message({
                      type: 'error',
                      message: '手机号输入有误！',
                      duration: 1500,
                      center: true
                  }) //检查手机号码是否正确
              } else {
                  //检查手机号是否注册
                  Register.CheckRegisteredApi(this.username)
                      .then(res => {
                          if(res.status == 2000){
                              this.isRegisterBtnDisabled = true
                              this.$message({
                                  type: 'error',
                                  message: '手机号已注册',
                                  duration: 2000
                              })
                          } else {
                              this.$message({
                                  type: 'success',
                                  message: '手机号可用',
                                  duration: 1500
                              })
                              this.isRegisterBtnDisabled = false
                          }
                      })
                      .catch(err => {
                          this.isRegisterBtnDisabled = true
                          this.$message({
                              type: 'error',
                              message: '未知错误，请联系管理员',
                          })
                          console.log(err)
                      })
              }
          },
          Register(){
              if(this.nickname === "" || this.pwd === ""){
                  this.$message({
                      type: "error",
                      message: "昵称/密码不能为空！",
                      duration: 2000,
                      center: true
                  })
              } else {
                 if(!this._CheckNickname(this.nickname)){
                     this.$message({
                         type: "warning",
                         message: "昵称只能是1到10位的数字/字母/汉字！",
                         duration: 2000,
                         center: true
                     })
                 } else if(!this._CheckPw(this.pwd)){
                     this.$message({
                         type: "warning",
                         message: "密码须6-16位，不能包含汉字！",
                         duration: 2000,
                         center: true
                     })
                 } else {
                     //验证全部通过，发送注册请求
                     const _data = {
                         username: this.username,
                         nickname: this.nickname,
                         pwd: this.pwd
                     }
                     Register.RegisterApi(_data)
                         .then(res => {
                             if(res.status == 1001){
                                 //注册成功
                                 //提示信息
                                 this.$message({
                                     type: "success",
                                     message: "注册成功！",
                                     duration: 1500,
                                     center: true
                                 })
                                 //跳转登录页面
                                 this.$router.push({name: 'login'})
                             } else{
                                 this.$message({
                                     type: "error",
                                     message: "注册失败， 请联系管理员或重新尝试！",
                                     duration: 3000,
                                     center: true
                                 })
                             }
                         })
                         .catch(err => {
                             this.$message({
                                 type: "error",
                                 messasge: "注册失败， 请联系管理员或重新尝试！",
                                 duration: 3000,
                                 center: true
                             })
                             console.log(err)
                         })
                 }
              }
          }
      },
      mounted() {
          this.$refs.UnInput.focus()
      }
  }
</script>

