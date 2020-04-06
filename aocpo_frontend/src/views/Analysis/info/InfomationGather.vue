<template>
  <info-layout>
    <template #header>
      <info-tools @GetData="HandleData" ></info-tools>
    </template>
    <template #main>
      <p v-if="!HasData" class="center">没有更多了</p>
      <div v-else>
        <el-backtop ref="ToTop" target=".el-scrollbar .wrap" :visibility-height="300"></el-backtop>
        <el-scrollbar
          style="height: 620px;"
          ref="ScrollBar"
          :wrap-class="['wrap']"
          wrap-style="overflow: auto;">
          <ul
            v-if="data"
            v-infinite-scroll="load"
            :infinite-scroll-disabled="disabled">
            <li
              v-for="item in data"
              :key="item.id">
              <info-item
                :title="item.title"
                :content="item.content"
                :date="item.date"
                :AuthorName="item.author_name"
                :school="item.school"
                :sentiment="item.sentiment"
                :AuthorUrl="item.author_url"
                :url="item.url"></info-item>
            </li>
          </ul>
          <p v-if="loading" class="center"><i class="el-icon-loading"></i>加载中...</p>
          <p v-if="IsEnd" class="center">没有更多了</p>
        </el-scrollbar>
      </div>
    </template>
  </info-layout>
</template>
<script>
  import InfoLayout from 'components/common/Layout/InfoLayout'
  import InfoTools from 'components/content/AnalysisPage/InfoGather/InfoTools'
  import InfoItem from 'components/content/AnalysisPage/InfoGather/InfoItem'
  import * as InfoRes from 'network/AnalysisPage/InfoAggregation'
  //'title', 'content', 'date', 'author_name', 'school', 'sentiment', 'classify', 'url'
  export default {
      name: "InfomationGather",
      data(){
          return {
              data: null,
              NextOffset: 0,
              IsEnd: false,
              loading: false,
              HasData: true
          }
      },
      computed: {
          disabled(){
              return this.loading || this.IsEnd
          }
      },
      methods: {
          //处理表单加载传来的数据
          HandleData(data){
              //初始化操作
              this.data = null
              this.IsEnd = false
              this.NextOffset = 0
              try {
                  let step = 0
                  let interval = setInterval(() => {
                      try {
                          if(this.$refs.ScrollBar.wrap.scrollTop <= 0) {
                              clearInterval(interval)
                              return
                          }
                          step += 10;
                          this.$refs.ScrollBar.wrap.scrollTop -= step
                      } catch (e) {
                          clearInterval(interval)
                      }
                  }, 30)//请求的时候跳到顶部
              } catch{} //el-scrollbar未渲染时会报错
              if(!data.is_end) {
                  this.NextOffset = data.next_offset //保存state用于下次请求
                  this.data = data.posts_data
                  this.HasData = true //第一次请求有没有数据？
              } else {
                  this.HasData = false
              }
          },
          //无限滑动加载
          load(){
              let opt = this.$store.state.Opt
              opt.offset = this.NextOffset
              this.loading = true
              InfoRes.GetData(opt)
                  .then(res => {
                      if (res.status == 1000) {
                          Array.prototype.push.apply(this.data, res.data.posts_data) //添加数据
                          this.IsEnd = res.data.is_end //数据为空时不加载了
                          this.NextOffset = res.data.next_offset //下一次的请求offset
                          this.loading = false
                      } else {
                          this.$message({
                              type: 'error',
                              message: '服务器错误, 请联系管理员',
                              duration: 2000,
                              center: true
                          })
                          this.loading = false
                      }
                  })
                  .catch(err => {
                      console.log(err);
                      this.$message({
                          type: 'error',
                          message: '服务器错误, 请联系管理员',
                          duration: 2000,
                          center: true
                      })
                      this.loading = false
                  })
          }
      },
      components: {
          InfoItem,
          InfoLayout,
          InfoTools
      }
  }
</script>

<style scoped>
  .center {
    text-align: center;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
</style>