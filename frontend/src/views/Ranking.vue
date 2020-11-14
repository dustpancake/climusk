<template>
  <div class="ranking content-width content">
    <div class="title">
      <h1>Ranking</h1>
      <FilterDropdown :options="['Friends', 'Neighbourhood', 'All citizens']" @filter-selected-option-changed="onFilterChanged"/>
    </div>

    <div v-if="isLoading">
      <div>scoreboard is loading</div>
    </div> 
    <div v-else class="scoreboard"> 
      <div v-for="(user, index) in scoreboard" :key="index" class="person">
        <p class="rank left">{{index + 1}}.</p>
        <p class="name left">{{ user.name }}</p>
        <p class="points right">{{ user.points }} pts.</p>
      </div>
    </div>
    <div class="title">
      <p>Your score is too low? You can improve your rank by accomplishing some efforts</p>
    </div>
  </div>
</template>

<script>
import FilterDropdown from "@/components/FilterDropdown.vue"

export default {
  name: "Ranking",
  components: {
    FilterDropdown
  },
  data () {
    return {
      isLoading: false,
      scoreboard: null    
    }
  },
  mounted() {
    this.isLoading = true
    // fetch data
    this.scoreboard = [{  
            "id": 1,
            "name": "Anna",   
            "points": 100,   
        },
        {  
            "id": 2,
            "name": "Michael Jordan",   
            "points": 90,   
        },
        {  
            "id": 3,
            "name": "Steve Jobs",   
            "points": 80,   
        },
        { 
            "id": 4, 
            "name": "You",   
            "points": 25,   
        }]
    this.isLoading = false
  },
  methods: {
    onFilterChanged(value) {
      console.log(value)
      // relodad data with value as new filter
    }
  }
};
</script>

<style scoped lang="scss">
.ranking {
  position: relative;
}

.title {
  overflow: hidden;
  h1 {
    float: left;
  }
  .filter-dropdown {
    float: right;
  }
}

.scoreboard {
  .person{
    padding: 10px 0;
    border-bottom: 1px solid $grey-border;
    overflow: hidden;
    .rank {
      font-weight: 500;
      margin-right: 10px;
    }
    p.left {
      float: left;
    }
    p.right {
      float: right;
    }
  }
}
</style>
