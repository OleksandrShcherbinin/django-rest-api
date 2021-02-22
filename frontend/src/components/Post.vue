<template>
  <section class="main">
    <div class="post" v-for="post in posts" :key="post.id">
      <h2 class="post__title">{{post.title}}</h2>
      <h3 class="post__author"><span>author</span> - {{post.username}}</h3>
      <p class="post__text">{{post.content}}</p>
      <div class="post-likes">
        <p class="post-likes__like"><svg class="post-likes__icon"><use xlink:href="../assets/like.svg#like"></use></svg>  {{post.like}}</p>
        <p class="post-likes__dislike"><svg class="post-likes__icon"><use xlink:href="../assets/dislike.svg#dislike"></use></svg>  -{{post.dislike}}</p>
      </div>
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
  &__title {
    text-transform: uppercase;
    font-family: Sintony-Regular, sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #1e347b;
  }
  &__author {
    font-family: Sintony-Regular, sans-serif;
    font-size: 20px;
    font-style: italic;
    font-weight: 700;
    color: green;
    span {
      font-size: 14px;
      color: deeppink;
    }
  }
  &__text {
    font-family: Sintony-Regular, sans-serif;
    font-size: 14px;
    font-weight: 400;
    color: #5170d2;
    border: 1px solid #a1a3aa;
    border-radius: 5px;
  }
  &-likes {
    display: flex;
    justify-content: space-between;
    &__icon {
      width: 20px;
      height: 20px;
    }
    &__like, &__dislike {
      font-weight: 900;
    }
    &__like {
      color: green;
    }
    &__dislike {
      color: red;
    }
    &__like &__icon:active {
      transform: scale(1.4);
      fill: forestgreen;
    }

    &__dislike &__icon:active {
      transform: scale(1.4);
      fill: red;
    }
  }
}
.post:hover {
  transform: scale(0.95);
}

</style>