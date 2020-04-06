<template>
  <el-card>
    <span class="title">时间范围：</span>
    <span class="button">
      <el-radio-group v-model="days"  @change="GetData">
        <el-radio-button :label="10" >近10天</el-radio-button>
        <el-radio-button :label="20">近20天</el-radio-button>
        <el-radio-button :label="30">近30天</el-radio-button>
        <el-radio-button :label="0">自定义</el-radio-button>
      </el-radio-group>
    </span>
    <span class="time">
       <el-date-picker
           v-show="!days"
           v-model="TimeRange"
           value-format="timestamp"
           :picker-options="PickerOptions"
           @change="GetCustomedData"
           type="datetimerange"
           range-separator="至"
           start-placeholder="开始日期"
           end-placeholder="结束日期">
         </el-date-picker>
    </span>
    <span class="CurrentAllCount" v-if="CurrentAllCount">
      <i class="el-icon-s-comment" style="font-size: 20px; color: #409EFF; margin-right: 5px"></i>当前数据量：{{CurrentAllCount}}
    </span>
  </el-card>
</template>

<style scoped>
  .CurrentAllCount {
    font-size: 20px;
    font-weight: 300;
    float: right;
    position: relative;
    top: 3px;
    right: 30px;
  }
  .time {
    margin-left: 20px;
  }
  .title {
    font-size: 15px;
    margin-right: 5px;
    margin-left: 5px;
  }
</style>

<script>
  import {PostsAnalysisData} from 'network/AnalysisPage/PublicOpinionAnalysis'
  export default {
      name: "ResTool",
      data() {
        return {
            PickerOptions: {
                disabledDate: (time) => {
                    let _time = time.getTime() / 1000
                    if (this.MaxDate === null || this.MinDate === null) {
                        return _time > Date.now() / 1000
                    } else {
                        return _time < this.MinDate || _time > this.MaxDate
                    }
                }
            },
            MaxDate: null,
            MinDate: null,
            days: 10,
            TimeRange: null,
            CurrentAllCount: null
        }
      },
      methods: {
          GetData() {
              const Task = this.$cookies.get('Task')
              let opt = {}
              opt.username = Task.username
              opt.school = Task.school
              if(this.days) {
                  const Loading = this.$loading({
                      lock: true,
                      text: '数据加载中...'
                  })
                  opt.days = this.days
                  PostsAnalysisData(opt)
                      .then(res => {
                          if(res.status == 1000) {
                              this.MaxDate = res.data.max_date
                              this.MinDate = res.data.min_date
                              this.CurrentAllCount = res.data.current_all_count
                              this.$emit('GetData', res.data)
                              setTimeout(() => {
                                  Loading.close()
                              }, 500)
                          } else {
                              this.$message({
                                  type: 'error',
                                  message: '服务器异常， 请联系管理员',
                                  duration: 3000,
                                  center:true
                              })
                              setTimeout(() => {
                                  Loading.close()
                              }, 500)
                          }
                      })
                      .catch(err => {
                          this.$message({
                              type: 'error',
                              message: '服务器异常， 请联系管理员',
                              duration: 3000,
                              center:true
                          })
                          setTimeout(() => {
                              Loading.close()
                          }, 500)
                          console.log(err)
                      })
              }

          },
          GetCustomedData() {
              const Task = this.$cookies.get('Task')
              let Loading = null
              let opt = {}
              opt.username = Task.username
              opt.school = Task.school
              if(this.TimeRange) {
                  const date_start = this.TimeRange[0] / 1000
                  const date_end = this.TimeRange[1] / 1000
                  const deference = date_end - date_start
                  if(deference > 30 * 24 * 60 * 60){
                      Loading = this.$loading({
                          lock: true,
                          text: '时间间隔过大， 会导致加载时间增加， 请耐心等待...'
                      })
                  } else {
                     Loading = this.$loading({
                          lock: true,
                          text: '数据加载中...'
                      })
                  }
                  opt.date_start = date_start
                  opt.date_end = date_end
              }
              PostsAnalysisData(opt)
                  .then(res => {
                      if(res.status == 1000) {
                          this.CurrentAllCount = res.data.current_all_count
                          this.$emit('GetData', res.data)
                          setTimeout(() => {
                              Loading.close()
                          }, 500)
                      } else {
                          this.$message({
                              type: 'error',
                              message: '服务器异常， 请联系管理员',
                              duration: 3000,
                              center:true
                          })
                          setTimeout(() => {
                              Loading.close()
                          }, 500)
                      }
                  })
                  .catch(err => {
                      this.$message({
                          type: 'error',
                          message: '服务器异常， 请联系管理员',
                          duration: 3000,
                          center:true
                      })
                      setTimeout(() => {
                          Loading.close()
                      }, 500)
                      console.log(err)
                  })
          }
      },
      created() {
          this.GetData()
      }
  }
</script>