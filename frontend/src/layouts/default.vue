<template>
  <div class="default-layout">
    <Navbar></Navbar>
    <slot></slot>
    <Footer></Footer>
  </div>
</template>

<script setup lang="ts">
// Components
import Navbar from '~/components/default_layout/Navbar.vue';
import Footer from '~/components/default_layout/Footer.vue';
</script>
<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.default-layout {
  position: relative;
  background: var(--c-background);

  :deep(>main) {
    min-height: calc(100dvh - 74px);
  }
}
</style>
