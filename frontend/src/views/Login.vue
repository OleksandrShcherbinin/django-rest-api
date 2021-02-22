<template>
  <section class="login">
    <p v-if="incorrectAuth" class="login__warning">Incorrect username or password entered. Please try again!</p>
    <form v-on:submit.prevent="login" class="login-form" method="post">
        <label class="login-form__label" for="username">Username</label>
        <input class="login-form__input" id="username" type="text" name="username" v-model="username">
        <label class="login-form__label" for="pass">Password</label>
        <input class="login-form__input" id="pass" type="password" name="password" v-model="password">
        <button class="login-form__button" type="submit">Log in</button>
    </form>
    <ul class="login-form__signup">
        <li><router-link class="nav--button__link" :to="{name: 'Signup'}" exact>Don't have an account. Sign Up</router-link></li>
    </ul>
  </section>
</template>

<script>
export default {
name: "Login",
  data() {
    return {
      username: '',
      password: '',
      incorrectAuth: false
    }
  },
  methods: {
    login() {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      })
      .then(() => {
        this.$router.push({name: 'Posts'})
      })
      .catch(error => {
        console.error(error)
        this.incorrectAuth = true
      })
    }
  }
}
</script>

<style lang="scss">
.login {
  width: 90%;
  margin: 50px auto;
  box-shadow: 5px 5px 15px 5px #000000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  &-form {
    padding: 50px 0;
    width: 80%;
    display: flex;
    flex-direction: column;
    &__input {
      width: 90%;
      height: 30px;
      margin-bottom: 20px;
      border: 1px solid #d2cece;
      border-radius: 5px;
      cursor: pointer;
    }
    &__input:focus {
      outline: none;
    }
    &__button {
      width: 50%;
      align-self: center;
      height: 40px;
      background-color: #f6ad52;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    &__button:active {
      outline: none;
    }
  }
}
</style>