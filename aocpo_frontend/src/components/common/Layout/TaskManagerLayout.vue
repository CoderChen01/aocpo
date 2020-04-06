<template>
  <el-container>
    <el-header>
      <slot name="HeaderContent"></slot>
    </el-header>
    <el-main>
      <slot name="MainContent"></slot>
    </el-main>
  </el-container>
</template>

<script>
    export default {
        name: "TaskMangerLayout"
    }
</script>

<style scoped>
  .el-container {
    padding: 25px;
    user-select: none;
  }
  .el-header {
    background-color: #fff;
    border: 1px solid #edeff2;
    padding: 13px 20px;
    margin-bottom: 20px;
  }
  .el-main {
    background-color: #fff;
    border: 1px solid #edeff2;
    padding: 0;
  }
</style>