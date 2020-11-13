<template>
  <div id="app">
    <Nav />
    <router-view/>
    <Footer />
  </div>
</template>

<script>
import Nav from "./components/Nav";
import Footer from "./components/Footer";

export default {
  name: "App",
  components: {
    Nav,
    Footer
  }
};
</script>

<style scoped lang="scss">
#app {
  font-family: "Avenir Next";
  font-weight: 400;
  font-style: normal;
  color: $black;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
  overflow: hidden;
  display: block;
  position: relative;
  text-align: center;
  // padding-bottom is being added dynamically within the Footer
}
</style>
