<template>
  <nav class="nav">
    <ul class="nav-menu">
      <li class="nav-menu__item" v-for="link in $router.options.routes" :key="link.path">
        <button class="nav-menu-button">
          <router-link class="nav-menu-button__link" :to="{name: link.name}" exact>{{link.name}}</router-link>
        </button>
      </li>
    </ul>
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
  &-menu {
    width: 100%;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    &-button {
      border: none;
      height: 50px;
      border-radius: 5px;
      padding: 0 10px;
      cursor: pointer;
      background-color: #e2e27e;
      &__link {
        color: black;
        font-size: 20px;
        font-family: Sintony-Regular, sans-serif;
      }
      &__link:active {
        color: black;
      }
    }
    &-button:active {
      outline: none;
      transform: translate(5px, -5px);
    }
    &-button:focus {
      outline: none;
    }
  }
}

</style>