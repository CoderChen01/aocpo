<template>
  <div class="tool">
    <div class="class  item">
      <span class="sentiment">
        <span class="Label">情感类型</span>
        <el-radio-group v-model="sentiment"  @change="GetData">
          <el-radio-button :label="-1" >全部</el-radio-button>
          <el-radio-button :label="2">积极</el-radio-button>
          <el-radio-button :label="1">中性</el-radio-button>
          <el-radio-button :label="0">消极</el-radio-button>
        </el-radio-group>
      </span>
    </div>
    <div class="TimeRange item">
      <span class="Label">可选时间范围</span>
      <el-date-picker
        v-model="TimeRange"
        value-format="yyyy-MM-dd HH:mm:ss"
        :picker-options="PickerOptions"
        @change="GetData"
        type="datetimerange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期">
      </el-date-picker>
    </div>
    <div class="order">
      <span class="Label">排序</span>
      <el-radio v-model="order" :label="-1" @change="GetData">时间降序</el-radio>
      <el-radio v-model="order" :label="1" @change="GetData">时间升序</el-radio>
    </div>
    <div class="AllCount fr">
      <span class="text" v-if="AllCount">
        <span>
          <i class="el-icon-s-comment" style="margin-right: 5px; color: #409EFF;"></i>
          当前信息量：
        </span>
        <span>{{AllCount}}</span>
      </span>
    </div>
  </div>
</template>

<script>
  import {HANDLEOPT} from 'store/MethodsManager'
  import * as InfoRes from 'network/AnalysisPage/InfoAggregation'
  export default {
      name: "InfoTools",
      data(){
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
              AllCount: null,
              classify: -1,
              sentiment: -1,
              order: -1,
              TimeRange: null
          }
      },
      computed: {
        Task(){
            return this.$cookies.get('Task')
        }
      },
      methods: {
          GetData(){
              const opt = {
                  username: this.Task.username,
                  school: this.Task.school,
                  limit: 20,
                  offset: 0,
                  order: this.order
              }
              if(this.classify != -1) {
                  opt.classify = this.classify
              }
              if(this.sentiment != -1) {
                  opt.sentiment = this.sentiment
              }
              if(this.TimeRange) {
                  opt.date_start = this.TimeRange[0]
                  opt.date_end = this.TimeRange[1]
              }
              const Loading = this.$loading({
                  lock: true,
                  text: '数据加载中...'
              })
              InfoRes.GetData(opt)
                  .then(res => {
                      if(res.status == 1000) {
                          const data = res.data
                          this.MaxDate = data.max_date
                          this.MinDate = data.min_date
                          this.AllCount = data.all_count
                          this.$emit('GetData', data)
                          this.$store.commit(HANDLEOPT, opt)
                          setTimeout(() => {
                              Loading.close()
                          }, 500)
                      } else {
                          setTimeout(() => {
                              Loading.close()
                          }, 500)
                          this.$message({
                              type: 'error',
                              message: '服务器错误, 请联系管理员',
                              duration: 2000,
                              center: true
                          })
                      }
                  })
                  .catch(err => {
                      console.log(err);
                      setTimeout(() => {
                          Loading.close()
                      }, 500)
                      this.$message({
                          type: 'error',
                          message: '服务器错误, 请联系管理员',
                          duration: 2000,
                          center: true
                      })
                  })
          }
      },
      created(){
          const opt = {
              username: this.Task.username,
              school: this.Task.school,
              limit: 20,
              offset: 0,
              order: -1
          }
          const Loading = this.$loading({
              lock: true,
              text: '数据加载中...'
          })
          InfoRes.GetData(opt)
              .then(res => {
                  if(res.status == 1000) {
                    const data = res.data
                    this.MaxDate = data.max_date
                    this.MinDate = data.min_date
                    this.AllCount = data.all_count
                    this.$emit('GetData', data)
                    this.$store.commit(HANDLEOPT, opt)
                    setTimeout(() => {
                        Loading.close()
                    }, 500)
                  } else {
                      setTimeout(() => {
                          Loading.close()
                      }, 500)
                      this.$message({
                          type: 'error',
                          message: '服务器错误, 请联系管理员',
                          duration: 2000,
                          center: true
                      })
                  }
              })
              .catch(err => {
                  console.log(err);
                  setTimeout(() => {
                      Loading.close()
                  }, 500)
                  this.$message({
                      type: 'error',
                      message: '服务器错误, 请联系管理员',
                      duration: 2000,
                      center: true
                  })
              })
      }
  }
</script>

<style scoped>
  .tool{
    padding: 30px;
    background: #fff;
    border: 1px solid #edeff2;
    height: 170px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  .Label {
    font-size: 15px;
    margin-right: 15px;
  }
  .item {
    margin-bottom: 30px;
  }
  .fr {
    float: right;
  }
  .AllCount{
    position: relative;
    bottom: 60%;
    right: 5%;
  }
  .text{
    font-size: 28px;
    font-weight: 300;
  }
</style>