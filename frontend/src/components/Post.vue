<template>
  <section class="main">
    <div class="post" v-for="post in posts" :key="post.id">
      <h2 class="post__title">{{post.title}}</h2>
      <p class="post__text">{{post.content}}</p>
      <p class="post_like"><img src="../assets/like.svg" alt="like" class="post__icon">  {{post.like}}</p>
      <p class="post__dislike"><img src="../assets/dislike.svg" alt="dislike" class="post__icon">  -{{post.dislike}}</p>
    </div>
  </section>
</template>

<script>
export default {
  name: "Post",
  props: ['posts']
}
</script>

<style scoped lang="scss">
.post {
  cursor: pointer;
  width: 90%;
  box-shadow: 3px 3px 5px 1px #898989;
  margin: 10px auto;
  padding: 30px;
  &__icon {
    width: 20px;
    height: 20px;
  }
}
.post:hover {
  transform: scale(0.9);
}

</style>