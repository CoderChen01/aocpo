<template>
  <div id="aocpoApp">
    <keep-alive :exclude="['RegisterPage', 'TaskManager', 'AnalysisPage']">
      <router-view></router-view>
    </keep-alive>
  </div>
</template>


<script>
export default {
  name: 'aocpoApp',
}
</script>

<style>
  @import "assets/css/base.css";
</style>
