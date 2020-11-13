<template>
  <div class="ranking content-width">
    <div class="title">
      <h1>Ranking</h1>
      <div class="filter">Friends</div>
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
export default {
  name: "Ranking",
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
    onFilterChanged() {
      // reload data with filter properties
    }
  }
};
</script>

<style scoped lang="scss">
.ranking {
  padding: 40px 0;
}

.title {
  overflow: hidden;
  position: relative;
  h1 {
    float: left;
  }
  .filter {
    padding: 10px 15px;
    border-radius: 5px;
    background-color: $grey;
    font-weight: 500;
    cursor: pointer;
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-85%);
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
