<template>
  <div class="home">
    <h3 class="m-4">API status: {{status}}</h3>
  </div>
</template>

<script>
// @ is an alias to /src
import api from '@/plugins/api.js'

export default {
  name: 'Home',

  data() {
    return {
      status: "Down"
    }
  },

  mounted: function() {
    api.healthcheck().then((resp) => {
      console.log(resp)
      if (resp.status == 200) {
        this.status = "Up";
      }
    })
  }

}
</script>
