<template>
  <div class="InfoItem">
    <div class="Info">
      <h2 :title="title" class="article-title ovhidden">
        <span class="sent" style="position: relative; bottom: 0.5mm">
          <span class="sen0" v-if="sentiment === 0">消极</span>
          <span class="sen1" v-else-if="sentiment === 1">中性</span>
          <span class="sen2" v-else>积极</span>
        </span>
        <span>{{title}}</span>
      </h2>
      <p :title="content"
         class="ovhidden2 color-8a8a99 content"
         :class="{'negative': sentiment===0}">
        {{content}}
      </p>
      <p class="field color-8a8a99 mt10">
        <span class="mr20">
          <span style="margin: 0;">发布人：</span>
          <span style="margin: 0;position: relative;bottom: 0.5mm;" v-if="AuthorUrl && AuthorName">
             <el-link
               :href="AuthorUrl"
               :type="Class"
               target="_blank"
               :underline="false">
               <span>{{AuthorName}}</span>
             </el-link>
          </span>
          <span v-else>未知发布人</span>
        </span>
        <span class="mr20">时间：{{date}}</span>
        <span class="mr20">学校：{{school}}</span>
        <span class="mr20" style="position: relative;bottom: 0.4mm;">
           <el-link
             :underline="false"
             target="_blank"
             type="primary"
             :href="url">原文链接</el-link>
        </span>
      </p>
    </div>
  </div>
</template>

<script>
  export default {
      name: "InfoItem",
      props: ['title', 'content', 'date', 'AuthorName', 'school', 'sentiment', 'url', 'AuthorUrl'],
      computed: {
          Class(){
              if(this.sentiment === 0) {
                  return 'danger'
              } else if(this.sentiment === 1) {
                  return 'warning'
              } else {
                  return 'primary'
              }
          }
      }
  }
</script>

<style scoped>
  .InfoItem {
    margin-bottom: 10px;
    background-color: #fff;
    overflow: hidden;
    border-radius: 2px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    box-shadow: 0 1px 3px rgba(26,26,26,.1);
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .ovhidden {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: block;
  }
  .ovhidden2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    overflow: hidden;
    -webkit-box-orient: vertical;
  }
  .color-8a8a99 {
    color: #8a8a99;
  }
  .mt10 {
    margin-top: 10px !important;
  }
  .sent{
    font-size: 15px;
    margin-right: 10px;
  }
  .sen0 {
    color: #F56C6C;
    border: 1px solid #F56C6C;
  }
  .negative {
    color: #F56C6C;
  }
  .sen1 {
    color: #E6A23C;
    border: 1px solid #E6A23C;
  }
  .sen2 {
    color: #67C23A;;
    border: 1px solid #67C23A;
  }
  .article-title {
    font-weight: 300;
  }
  .Info {
    padding: 5px 25px 5px 25px;
  }
  .InfoItem {
    padding: 3px;
  }
  .field .mr20 {
    margin-right: 30px;
  }
  .content {
    margin-top: 8px;
  }
  p {
    list-style: none;
    margin: 0;
  }
</style>