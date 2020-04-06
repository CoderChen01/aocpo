<template>
  <div class="Area">

    <div class="Body">

      <div class="logo">
        <slot name="logo"></slot>
      </div>

      <div class="Item">
        <slot name="item"></slot>
      </div>

    </div>

  </div>
</template>

<script>
  export default {
      name: "LoginRegisterModel",
  }
</script>

<style scoped>
  .Area{
    width: 414px;
    height: 515px;
    background-color: rgb(255, 255, 255);
    border-radius: 3px;
    box-shadow: 0 3px 9px rgba(0,0,0,.5);
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  .Body {
    padding: 24px 40px;
  }
  .logo {
    margin-top: 20px;
    margin-bottom: 80px;
  }
  .el-row{
    margin-bottom: 20px;
  }

</style>