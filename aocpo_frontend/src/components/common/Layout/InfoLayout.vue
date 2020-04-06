<template>
  <el-container>
    <el-header height="230px">
      <slot name="header"></slot>
    </el-header>
    <el-main>
      <slot name="main"></slot>
    </el-main>
  </el-container>
</template>

<script>
    export default {
        name: "InfoLayout"
    }
</script>

<style scoped>
  .el-header{
    margin: 0;
    padding: 0;
  }
  .el-main {
    margin-top: 30px;
    padding: 0;

  }
</style>