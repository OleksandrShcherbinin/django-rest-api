<template>
  <div class="posts">
    <h1 class="posts__title">My social network</h1>
    <Post v-bind:posts="posts"/>
  </div>
</template>

<script>
import Post from "@/components/Post";
import { getAPI } from "@/api/axios";

export default {
  name: 'Posts',
  components: {
    Post
  },
  data() {
    return {
      posts: []
    }
  },
  created() {
    getAPI.get("/api/posts/",)
    .then(response => {
      console.log("Data received")
      this.posts = response.data
    })
    .catch(error => {
      console.error(error)
    })
  }
}
</script>

<style scoped lang="scss">
.posts {
  &__title {
    font-family: Sintony-Regular, sans-serif;
    font-size: 40px;
    text-align: center;
  }
}

</style>
