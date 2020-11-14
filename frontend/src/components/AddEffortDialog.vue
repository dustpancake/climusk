<template>
  <b-modal id="effort-modal" :title="modal_title">

    <b-row class="mt-3">
      <b-col>
        Name:
        <b-form-input class="mt-2"
        placeholder="Effort name"
        v-model="username"
        validate-on-blur
        ></b-form-input>
      </b-col>
    </b-row>

    <b-row class="mt-3">
      <b-col>
        Description:
        <b-form-input class="mt-2"
        placeholder="Short description"
        v-model="username"
        validate-on-blur
        ></b-form-input>
      </b-col>
    </b-row>

  </b-modal>
</template>

<script>

export default {
  props: {
    category: {
      type: String
    }
  },
  computed: {
    modal_title: () => {
      return "Add Effort"
    }
  }
}

</script>
