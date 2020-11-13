<template>
  <b-card
    :title="title"
    :img-src="img"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2 clinet-card"
    align="left"
  >

  <div class="clinet-card-body">
    <slot></slot>
  </div>

  </b-card>
</template>


<script>
export default {
  name: "Card",

  props: {
    title: {
      type: String
    },
    img: {
      type: String
    }
  }

}
</script>

<style scoped lang="css">

/* override for green text */
.clinet-card {
  color: green;
}

/* black for slots */
.clinet-card-body {
  color: black;
}

</style>
