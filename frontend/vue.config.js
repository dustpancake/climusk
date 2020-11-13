module.exports = {
  publicPath: '/climusk',
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "@/scss/_main.scss";`
      }
    }
  }
};