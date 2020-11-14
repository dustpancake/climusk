<template>
  <div class="categories m-4 content-width content">
    <b-row class="justify-content-md-center">
      <b-col v-for="cat in categories" :key="cat.category_name">
        <Category
        :title="cat.category_name"
        :efforts="cat.efforts"
        :addEffort="addEffort"
        />
      </b-col>
    </b-row>

    <AddEffortDialog category="selected_category" />

  </div>
</template>

<script>

import Category from "@/components/Category.vue"
import AddEffortDialog from "@/components/AddEffortDialog.vue"

import api from "@/plugins/api.js"

function get_category_list(callback) {
  api.get(`/category`).then(callback)
}


export default {

  components: {
    Category, AddEffortDialog
  },

  data() {
    return {
      categories: [], //default
      show_add_effort: false,
      selected_category: ""
    }
  },

  mounted() {
    get_category_list((result) => {
      console.log(result.data);
      this.categories = result.data;
    });
  },

  methods: {
    addEffort(category_name) {
      console.log("DEBUG " + category_name)
      this.selected_category = category_name;
      this.show_add_effort = true;
      this.$bvModal.show("effort-modal")
    }
  }

}

</script>
