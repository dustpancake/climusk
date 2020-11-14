<template>
  <div align="center" class="pt-4">
    <Card title="Login">
      <b-row class="mt-3">
        <b-col>
          <b-form-input
          placeholder="Username"
          v-model="username"
          validate-on-blur
          ></b-form-input>
        </b-col>
      </b-row>
      <b-row align="center" class="m-3">
        <b-col>
          <b-button variant="success" @click="submit">Login</b-button>
        </b-col>
      </b-row>
    </Card>
  </div>
</template>


<script>
import Card from '@/components/Card.vue'

import api from '@/plugins/api.js';

export default {
  name: "LoginView",
  components: {
    Card
  },

  data() {
    return {
      username: "",
      entry_state: null
    }
  },

  methods: {
    submit() {
      if(this.username) {
        api.registerUser(this.username).then((resp) => {
          // if username is okay
          if (resp.status == 200) this.$router.push('MyEfforts');
        });
      }
    }
  }

}

</script>
