<template>
  <div class="RegisterPage">
    <register-model>
      <template #logo>
        <img src="~assets/img/LoginRegister/logo.png" alt="logo">
      </template>
    </register-model>
  </div>
</template>

<script>
  import RegisterModel from 'components/content/LoginRegister/RegisterModel'
  export default {
      name: "RegisterPage",
      components: {
          RegisterModel
      }
  }
</script>

<style scoped>
  .RegisterPage{
    background-image: url("~assets/img/LoginRegister/RegisterBg.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    padding: 200px 740px;
  }

</style>