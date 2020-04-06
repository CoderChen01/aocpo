<template>
  <div class="LoginPage">
    <login-model>
      <template #logo>
        <img src="~assets/img/LoginRegister/logo.png" alt="logo">
      </template>
    </login-model>
    </div>
</template>

<script>
    import LoginModel from 'components/content/LoginRegister/LoginModel'

    export default {
        name: "LoginPage",
        components: {
            LoginModel
        }
    }
</script>

<style scoped>
  .LoginPage{
    background-image: url("~assets/img/LoginRegister/LoginBg.png");
    background-repeat: no-repeat;
    background-size: cover;
    padding: 200px 740px;
    position: relative;
   }
</style>