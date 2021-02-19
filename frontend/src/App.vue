<template>
  <div id="app">
      <Nav/>
    <router-view/>
  </div>
</template>
<script>
import Nav from "@/components/Nav";
export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>

<style lang="scss">
@import "scss/normalize";
@import "scss/fonts";
body {
  display: flex;
  justify-content: center;
}
#app {
  width: 50%;
  margin: 20px 0;
  box-shadow: 5px 5px 15px 5px #000000;
}
</style>
