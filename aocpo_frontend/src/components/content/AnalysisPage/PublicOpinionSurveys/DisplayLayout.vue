<template>
  <el-card
    shadow="always">
    <template #header>
      <div class="header">
        <h2 class="title"><slot name="title"></slot></h2>
      </div>
    </template>
    <slot name="body"></slot>
  </el-card>
</template>


<style scoped>
  .title {
    padding-left: 8px;
    line-height: 1;
    border-left: 4px solid #0095eb;
  }
</style>

<script>
    export default {
        name: "DisplayLayout"
    }
</script>
