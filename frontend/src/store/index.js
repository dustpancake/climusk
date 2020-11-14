import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    current_user: "",
    uuid: ""
  },
  mutations: {
    // setters

    setCurrentUser(state, user) {
      state.current_user = user;
    },

    setUUID(state, uuid) {
      state.uuid = uuid;
    }

  },
  actions: {
    // getters
    current_user: state => state.current_user,
    uuid: state => state.uuid

  },
  modules: {
  }
})
