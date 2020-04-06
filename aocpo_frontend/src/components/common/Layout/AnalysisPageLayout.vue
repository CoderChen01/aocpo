<template>
  <el-container>
    <el-aside width="210px">
      <slot name="nav"></slot>
    </el-aside>
    <el-main>
      <slot name="main"></slot>
    </el-main>
  </el-container>
</template>

<script>
    export default {
        name: "AnalysisPageLayout"
    }
</script>

<style scoped>
  .el-aside{
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
  }
  .el-main {
    margin-left: 200px;
    padding: 20px;
  }
</style>