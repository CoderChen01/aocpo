<template>
  <div class="container">
    <img src="~assets/img/404.png" alt="404" class="img404">
    <div class="text">页面走丢啦...</div>
  </div>
</template>

<script>
  export default {
      name: "NotFound"
  }
</script>

<style scoped>
  .container {
    position: absolute;
    left: 38%;
  }
  .img404 {
    width: 500px;
    height: 500px;
  }
  .text {
    font-size: 20px;
    font-weight: 400;
    text-align: center;
  }
</style>