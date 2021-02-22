import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from "@/api/axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    posts: ''
  },
  mutations: {
    updateStorage(state, {access, refresh}) {
      state.accessToken = access
      state.refreshToken = refresh
    },
  },
  actions: {
    userLogin(context, userCredentials) {
      return new Promise((resolve, reject) => {
        getAPI.post('/auth/login/', {
          username: userCredentials.username,
          password: userCredentials.password
        }).then(response => {
          localStorage.setItem('token', response.data.access)
          context.commit('updateStorage',
              {
                access: response.data.access,
                refresh: response.data.refresh
              })
          resolve()
        })
        .catch(error => {
            reject(error)
          })
      })
    },
    userSignup(context, userCredentials) {
      return new Promise((resolve, reject) => {
        getAPI.post('/auth/signup/', {
          username: userCredentials.username,
          password: userCredentials.password,
          password2: userCredentials.password2,
          email: userCredentials.email,
          first_name: userCredentials.first_name,
          last_name: userCredentials.last_name
        }).then(response => {
          console.log("Success!!!")
          resolve()
        })
        .catch(error => {
            reject(error)
          })
      })
    }
  },
  modules: {
  }
})
