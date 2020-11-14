<template>
  <div class="filter-dropdown" v-click-outside="hideDropdown">
    <div class="filter-btn" @click="isCollapsed = !isCollapsed">
      <p>{{ selectedOption }}</p>
      <ul v-show="isCollapsed">
        <li v-for="(option, index) in options" :key="index" @click="onOptionClicked(option)">
          {{ option }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
    name: 'FilterDropdown',
    props: {
        options: {
          type: Array,
          required: true
        },
        preSelectedOption: {
          type: Number,
          default: 0
        }
    },
    data(){
      return {
        selectedOption: this.options[this.preSelectedOption],
        isCollapsed: false
      }
    },
    methods: {
      hideDropdown() {
        this.isCollapsed = false
      },
      onOptionClicked(option) {
        this.selectedOption = option
        this.$emit('filter-selected-option-changed', option);
      }
    }
}
</script>

<style scoped lang="scss">
.filter-dropdown {
    border-radius: 5px;
    background-color: $grey;
    font-weight: 500;
    cursor: pointer;

    .filter-btn {
      padding: 10px 15px;

      ul {
        position: absolute;
        background-color: $grey;
        right: 0;
        text-align: right;
        margin-top: $base-font-size;
        padding: 5px 0;
        border-radius: 5px;
        box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;

        li {
          padding: 7px 15px;
          font-size: $base-font-size;
          cursor: pointer;

          &:hover {
            background-color: darken($grey, 20%);
          }
        }
      }
    }
}
</style>