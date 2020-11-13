<template>
  <div class="header">
      <div class="navi content-width">
        <div class="navi-inner">
          <router-link class="logo-wrapper" to="/">
            <div class="logo"></div>
          </router-link>
          <ul>
              <li>
                <router-link to="/">Home</router-link>
              </li>
              <li>
                <router-link to="/categories">Categories</router-link>
              </li>
              <li>
                <router-link to="/my-efforts">My Efforts</router-link>
              </li>
              <li>
                <router-link to="/ranking">Ranking</router-link>
              </li>
              <li>
                <router-link to="/account">Account</router-link>
              </li>
          </ul>
        </div>
      </div>
    </div>
</template>

<style scoped lang="scss">
$logo-translateY: 37px;
$logo-height: 22px;
$logo-width: 80px;

.header {
  width: 100%;
  padding: 16px 0;
  background: rgb(26,147,107);
  background: linear-gradient(227deg, rgba(26,147,107,1) 0%, rgba(13,123,103,1) 39%, rgba(15,120,103,1) 61%, rgba(0,92,98,1) 100%);
  box-shadow: rgba(0, 0, 0, 0.08) 0px 1px 12px !important;

  .navi {
    position: relative;

    .navi-inner {
      overflow: hidden;

      .logo-wrapper {
        float: left;
        overflow: hidden;

        &:hover {
          .logo {
            transform: translateY($logo-translateY);
          }
        }

        .logo {
          height: $logo-height;
          width: $logo-width;
          background: url("../assets/clinet-logo.png");
          background-size: 100% 100%;
          background-repeat: no-repeat;
          margin: 8px 0 4px 0;
          display: inline-block;
          transition: transform 0.2s ease-in-out 0s;
          position: relative;

          &:after {
            content: "";
            height: $logo-height;
            width: $logo-width;
            background: url("../assets/clinet-logo.png");
            background-size: 100% 100%;
            background-repeat: no-repeat;
            font-weight: 700;
            position: absolute;
            bottom: $logo-translateY;
            left: 0;
            transform: translate3d(0px, 0px, 0px);
          }
        }
      }

      ul {
        float: right;

        li {
          float: left;
          margin: 0.65em 0 0 1.75em;

          a {
            display: block;
            color: $white;
            width: 100%;
          }
        }
      }
    }
  }
}
</style>
