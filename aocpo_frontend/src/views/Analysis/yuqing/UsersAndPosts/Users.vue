<template>
  <div class="container" v-loading="IsLoading">
    <div class="title">
      <h1><i class="el-icon-s-data" ></i>用户分析<span v-if="this.AllCount" style="font-size: 15px; font-weight: 300">(总数据量： {{this.AllCount}})</span></h1>
    </div>
    <div class="wrapper">
        <nick-name-hot-word-display :data="NickNameData"  v-if="NickNameData"></nick-name-hot-word-display>
    </div>
    <div class="wrapper">
      <el-row :gutter="50">
        <el-col :span="100">
          <active-users-display :XData="ActiveUsersData.x_data" :YData="ActiveUsersData.y_data" v-if="ActiveUsersData"></active-users-display>
        </el-col>
        <el-col :span="100">
          <famous-users-display :XData="FamousUsersData.x_data" :YData="FamousUsersData.y_data" v-if="FamousUsersData"></famous-users-display>
        </el-col>
      </el-row>
    </div>
    <div class="wrapper">
      <el-row :gutter="50">
        <el-col :span="100">
          <man-female-scale-display :data="SexScaleData" v-if="SexScaleData"></man-female-scale-display>
        </el-col>
        <el-col :span="100">
          <old-and-new-scale-display :data="NewAndOldUsersData" v-if="NewAndOldUsersData"></old-and-new-scale-display>
        </el-col>
      </el-row>
    </div>
    <div class="wrapper last">
      <el-row :gutter="50">
        <el-col :span="100">
          <device-scale-display :data="DeciveScaleData" v-if="DeciveScaleData"></device-scale-display>
        </el-col>
        <el-col :span="100">
          <vip-scale-display :data="VipUsersData" v-if="VipUsersData"></vip-scale-display>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<style scoped>
  .container {
    padding: 5px 30px 30px 30px;
    background: #fff;
    border: 1px solid #edeff2;
    user-select: none;
    margin: 0;
  }
  .title {
    text-align: center;
    margin-bottom: 20px;
    color: #409EFF;
  }
  .wrapper {
    margin-left: 35px;
    margin-bottom: 35px;
  }
  .last {
    margin-bottom: 0;
  }
</style>

<script>
  import {
      ActiveUsersDisplay,
      FamousUsersDisplay,
      ManFemaleScaleDisplay,
      VipScaleDisplay,
      DeviceScaleDisplay,
      OldAndNewScaleDisplay,
      NickNameHotWordDisplay
  } from 'components/content/AnalysisPage/PublicOpinionSurveys/UserAnalysis'
  import {UsersAnalysisData} from 'network/AnalysisPage/PublicOpinionAnalysis'
  export default {
      name: "Users",
      data() {
          return {
              IsLoading: true,
              ActiveUsersData: null,
              NewAndOldUsersData: null,
              FamousUsersData: null,
              VipUsersData: null,
              SexScaleData: null,
              NickNameData: null,
              DeciveScaleData: null,
              AllCount: null
          }
      },
      methods: {
        request() {
            let Task = this.$cookies.get('Task')
            let username = Task.username
            let school = Task.school
            const opt = {
                username,
                school
            }
            this.IsLoading = true
            UsersAnalysisData(opt)
                .then(res => {
                    if(res.status == 1000) {
                        this.IsLoading = false
                        const data = res.data
                        this.ActiveUsersData = data.active_users_data
                        this.NewAndOldUsersData = data.new_old_data
                        this.FamousUsersData = data.famous_users_data
                        this.VipUsersData = data.vips_data
                        this.SexScaleData = data.sex_data
                        this.NickNameData = data.nick_name_data
                        this.DeciveScaleData = data.device_data
                        this.AllCount = data.all_count
                    } else {
                        this.IsLoading = false
                        this.$message({
                            type: 'error',
                            message: '服务器异常， 请联系管理员',
                            duration: 2000,
                            center: true
                        })
                    }
                })
                .catch(err => {
                    this.IsLoading = false
                    this.$message({
                        type: 'error',
                        message: '服务器异常， 请联系管理员',
                        duration: 2000,
                        center: true
                    })
                    console.log(err)
                })
        }
      },
      components: {
          ActiveUsersDisplay,
          FamousUsersDisplay,
          ManFemaleScaleDisplay,
          VipScaleDisplay,
          DeviceScaleDisplay,
          OldAndNewScaleDisplay,
          NickNameHotWordDisplay
      },
      created() {
          this.request()
      }


  }
</script>

