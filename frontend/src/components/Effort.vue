<template>

  <Card>

  <b-row>

    <b-col>
      <h3 class="clinet-title">
        {{title}}
      </h3>
    </b-col>

    <b-col align="right">
      <small class="text-muted">Authored by </small><br>
      {{author}}
    </b-col>

  </b-row>

  <div class="m-2">
    {{description}}
  </div>

  <hr>
  <Task v-for="task in tasks" :key="task.name" :name="task.name" :description="task.description" />
  <hr>

  <b-row align="center" justify="center" class="mt-2">

  <b-col>
    <b-btn variant="outline">
      <router-link :to="effort_uri">See More</router-link>
    </b-btn>
  </b-col>

  <b-col>
    <b-btn variant="outline">
      <router-link :to="effort_uri">Join</router-link>
    </b-btn>
  </b-col>

  </b-row>

  </Card>

</template>


<script>
import Card from "./Card.vue"
import Task from "./Task.vue"

export default {

  components: {
    Card, Task
  },

  props: {
    title: {
      type: String
    },
    tasks: {
      type: Object,
    },
    author: {
      type: String,
      default: "TestAuthor"
    },
    e_id: { // effort id
      type: String,
      default: "0"
    },
    description: {
      type: String,
      default: "sample description"
    }
  },

  computed: {
    effort_uri: function () {
      return "/effort/" + this.e_id;
    }
  }

}

</script>

<style>

.clinet-title {
  color: green;
}

</style>
