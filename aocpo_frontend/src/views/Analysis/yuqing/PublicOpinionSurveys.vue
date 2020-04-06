<template>
  <div>
    <div class="posts">
      <posts-analysis></posts-analysis>
    </div>
    <div class="users">
      <users-analysis></users-analysis>
    </div>
  </div>
</template>

<script>
  import UsersAnalysis from './UsersAndPosts/Users'
  import PostsAnalysis from './UsersAndPosts/Posts'
  export default {
      name: "PublicOpinionSurveys",
      components: {
          UsersAnalysis,
          PostsAnalysis
      }
  }
</script>

<style scoped>
  .posts {
    margin-bottom: 50px;
  }
</style>