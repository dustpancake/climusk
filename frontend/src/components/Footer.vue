<template>
  <footer>
    <div class="footer-inner content-width" ref="footerInner">
      <div class="infos">
        <p>© {{ new Date().getFullYear() }} by Clinet · Made with <span class="heart"></span> in Zurich</p>
      </div>
      <div class="links">
        <router-link to="/impressum">Impressum</router-link>
        <router-link to="/data-policy">Data Policy</router-link>
        <router-link to="/about">About</router-link>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  mounted() {
    window.addEventListener("resize", this.onResize);
    this.setFooterHeight();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
  methods: {
    onResize() {
      this.setFooterHeight();
    },
    setFooterHeight() {
      let appPaddingBottom = document.getElementById("app").style.paddingBottom;
      let newFooterHeight = this.$refs.footerInner.clientHeight + "px";
      if (appPaddingBottom != newFooterHeight) {
        document.getElementById("app").style.paddingBottom = newFooterHeight;
      }
    }
  }
};
</script>

<style scoped lang="scss">
footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  background-color: darken($grey, 10%);
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: $grey-border;
  // Do NOT set padding -> height is being calculated manually via JS

  .footer-inner {
    padding: 50px 0;
    overflow: hidden;
    font-weight: 500;

    .infos {
      float: left;

      .heart {
        $width: 12px;
        background-image: url("../assets/heart.png");
        background-size: $width $width;
        height: $width;
        width: $width;
        display: inline-block;
      }
    }

    .links {
      float: right;

      a {
        margin-right: 15px;

        &:last-of-type {
          margin: 0;
        }
      }
    }
  }
}
</style>
