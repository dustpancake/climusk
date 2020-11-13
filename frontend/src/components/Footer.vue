<template>
  <div class="grey-bg">
    <footer class="content">
      <p class="copyright">© {{ new Date().getFullYear() }}. All rights reserved.</p>
      <p>
        <router-link :to="{ name: 'PrivacyPolicy' }">Privacy Policy</router-link>
      </p>
      <p class="made-with-love">
        Made with
        <span class="heart"></span> in Zurich
      </p>
    </footer>
  </div>
</template>