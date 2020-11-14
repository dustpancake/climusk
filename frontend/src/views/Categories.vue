<template>
  <div class="categories m-4">
    <b-row class="justify-content-md-center">
      <b-col v-for="cat in categories" :key="cat.category_name">
        <Category :title="cat.category_name" :efforts="cat.efforts"/>
      </b-col>
    </b-row>
  </div>
</template>

<script>

import Category from "@/components/Category.vue"

import api from "@/plugins/api.js"

function get_category_list(callback) {
  api.get(`/category`).then(callback)
}


export default {

  components: {
    Category
  },

  data() {
    return {
      categories: [] //default
    }
  },

  mounted() {
    get_category_list((result) => {
      console.log(result.data);
      this.categories = result.data;
    });
  }

}

</script>
