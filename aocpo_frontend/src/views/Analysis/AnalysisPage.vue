<template>
  <analysis-page-nav :CurrentTask="school">
    <template #main>
      <router-view></router-view>
    </template>
  </analysis-page-nav>
</template>

<script>
  import AnalysisPageNav from 'components/content/AnalysisPage/AnalysisPageNav'
  export default {
      name: "AnalysisPage",
      computed: {
          school(){
              return this.$cookies.get('Task').school
          }
      },
      components: {
          AnalysisPageNav
      },
      beforeCreate() {
          if (!this.$cookies.isKey('Task')) {
              this.$router.push({name: 'task_manager'})
              this.$message({
                  type: 'warning',
                  message: '请选取任务',
                  duration: 2000,
                  center: true
              })
          }
      }
  }
</script>

<style scoped>

</style>