<template>
  <div class="posts">
    <h1 class="posts__title">My social network</h1>
    <Post v-bind:posts="posts"/>
  </div>
</template>

<script>
import Post from "@/components/Post";
import { getAPI } from "@/api/axios";
import { mapState } from 'vuex';

export default {
  name: 'Posts',
  components: {
    Post
  },
  computed: mapState(['posts']),
  created() {
    getAPI.get("/api/posts/", {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
    .then(response => {
      console.log("Data received")
      this.$store.state.posts = response.data
    })
    .catch(error => {
      console.error(error)
    })
  }
}
</script>

<style scoped lang="scss">
.posts {
  display: flex;
  flex-direction: column;
  justify-content: center;
  &__title {
    font-family: Sintony-Regular, sans-serif;
    font-size: 40px;
    text-align: center;
  }
}

</style>
