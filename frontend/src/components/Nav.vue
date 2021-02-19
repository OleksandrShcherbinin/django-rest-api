<template>
  <nav class="nav">
    <button class="nav--button">
      <router-link class="nav--button__link" :to="{name: 'Posts'}" exact>Posts</router-link>
    </button>
  </nav>
</template>

<script>
export default {
name: "Nav"
}
</script>

<style scoped lang="scss">
.nav {
  margin-top: 10px;
  display: flex;
  justify-content: space-around;
  &--button {
    &__link {
      font-size: 20px;
      font-family: Sintony-Regular, sans-serif;
    }
  }
}

</style>