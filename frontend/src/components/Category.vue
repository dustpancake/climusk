<template>
  <b-jumbotron class="p-3" fluid>
    <h3>{{title}}</h3>
    <div align="left" class="mb-2">
      {{description}}
    </div>

    <Effort v-for="effort in efforts" :key="effort.title" />

  </b-jumbotron>
</template>


<script>
import Effort from "./Effort.vue"

import api from "@/plugins/api.js"

function get_efforts_for(category, callback) {
  api.get(`/category/${category}`).then(callback)
}

export default {
  components: {
    Effort
  },
  props: {
    title: {
      type: String
    },
    description: {
      type: String,
      default: "This is a category."
    }
  },

  data() {
    return {
      efforts: [] // default value
    }
  },

  mounted: function(){
    get_efforts_for(this.title, (result)=>{
      this.efforts = result.data;
    });
  }
}

</script>
