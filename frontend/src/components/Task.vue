<template>
  <b-row class="text-center">
    <b-col ><b>{{name}}</b></b-col>
    <b-col cols="8" align="left">{{description}}</b-col>
  </b-row>
</template>


<script>
export default {


  props: {
    description: {
      type: String
    },
    name: {
      type: String
    }
  }
}

</script>
