<template>
  <div class="container">
    <div class="title">
      <h1><i class="el-icon-s-data" ></i>内容分析<span v-if="this.AllCount" style="font-size: 15px; font-weight: 300" v-once>(总数据量： {{this.AllCount}})</span></h1>
    </div>
    <div class="tool">
      <res-tool @GetData="GetData"></res-tool>
    </div>
    <div class="wrapper">
      <el-row :gutter="50">
        <el-col :span="100">
          <hot-posts-display :XData="HotPostsData.x_data" :YData="HotPostsData.y_data" v-if="HotPostsData"></hot-posts-display>
        </el-col>
        <el-col :span="100">
          <content-hot-words-display :data="HotWordsData" v-if="HotWordsData"></content-hot-words-display>
        </el-col>
      </el-row>
    </div>
    <div class="wrapper last">
      <el-row :gutter="50">
        <el-col :span="100">
          <classify-display :data="ClassifyCountData" v-if="ClassifyCountData"></classify-display>
        </el-col>
        <el-col :span="100">
          <sentiment-display :data="SentimentCountData" v-if="SentimentCountData"></sentiment-display>
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
  .tool {
    width: 1539px;
    margin-left: 33px;
    margin-bottom: 30px;
  }
</style>

<script>
  import {
      ResTool,
      ContentHotWordsDisplay,
      SentimentDisplay,
      ClassifyDisplay,
      HotPostsDisplay
  } from 'components/content/AnalysisPage/PublicOpinionSurveys/PostsAnalysis'
  export default {
      name: "Posts",
      data(){
          return {
              AllCount: null,
              HotPostsData: null,
              HotWordsData: null,
              SentimentCountData: null,
              ClassifyCountData: null
          }
      },
      methods: {
          GetData(data) {
              this.AllCount = data.all_count
              this.HotWordsData = data.hot_words_data
              this.SentimentCountData = data.sent_class_data
              this.ClassifyCountData = data.class_count_data
              this.HotPostsData = data.hot_posts_data
          }
      },
      components: {
          ResTool,
          ContentHotWordsDisplay,
          SentimentDisplay,
          ClassifyDisplay,
          HotPostsDisplay
      }
  }
</script>

