<template>
  <div class="posts">
    <h1 class="posts__title">My social network</h1>
    <h3 class="posts__warning" v-if="!posts.length && fresh">You are not authorized. Please <router-link class="posts__link" :to="{name: 'Login'}" exact>Login </router-link>or <router-link class="posts__link" :to="{name: 'Signup'}" exact>Sign up!</router-link></h3>
    <h3 class="posts__warning" v-if="!fresh">Your token has been expired. Please <router-link class="posts__link" :to="{name: 'Login'}" exact>Login </router-link></h3>
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
  data() {
    return {
      fresh: true
    }
  },
  computed: mapState(['posts']),
  created() {
    let token;
    let localToken = localStorage.getItem('token');
    if (localToken && this.fresh) {
      token = localToken;
    } else {
      token = this.$store.state.accessToken;
    }
    getAPI.get("/api/posts/", {headers: {Authorization: `Bearer ${token}`}})
    .then(response => {
      console.log("Data received")
      this.$store.state.posts = response.data
    })
    .catch(error => {
      this.fresh = false
      console.error(error, 'Token expired')
    })
  }
}
</script>

<style scoped lang="scss">
.posts {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-family: Sintony-Regular, sans-serif;
  &__title {
    font-size: 40px;
    text-align: center;
  }
  &__warning {
    padding: 20px;
    font-size: 20px;
    color: deeppink;
    text-align: center;
  }
}

</style>
