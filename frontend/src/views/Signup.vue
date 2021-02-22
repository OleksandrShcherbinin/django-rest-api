<template>
  <section class="login">
    <p v-if="incorrectAuth" class="login__warning">Incorrect username or password entered. Please try again!</p>
    <form v-on:submit.prevent="signup" class="login-form" method="post">
        <label class="login-form__label" for="username">Username</label>
        <input class="login-form__input" id="username" type="text" name="username" v-model="username" maxlength="150" required>
        <label class="login-form__label" for="pass">Password</label>
        <input class="login-form__input" id="pass" type="password" name="password" v-model="password" required>
        <label class="login-form__label" for="pass2">Confirm password</label>
        <input class="login-form__input" id="pass2" type="password" name="password2" v-model="password2" required>
        <label class="login-form__label" for="email">Email</label>
        <input class="login-form__input" id="email" type="email" name="email" v-model="email" required>
        <label class="login-form__label" for="first_name">First name</label>
        <input class="login-form__input" id="first_name" type="text" name="first_name" v-model="first_name">
        <label class="login-form__label" for="last_name">Last name</label>
        <input class="login-form__input" id="last_name" type="text" name="last)_name" v-model="last_name">
        <button class="login-form__button" type="submit">Sign up</button>
    </form>
  </section>
</template>

<script>
export default {
name: "Signup",
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      email: '',
      first_name: '',
      last_name: '',
      incorrectAuth: false
    }
  },
  methods: {
    signup() {
      this.$store.dispatch('userSignup', {
        username: this.username,
        password: this.password,
        password2: this.password2,
        email: this.email,
        fist_name: this.first_name,
        last_name: this.last_name
      })
      .then(() => {
        this.$router.push({name: 'Login'})
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

</style>