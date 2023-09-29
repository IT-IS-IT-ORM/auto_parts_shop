<template>
  <main class="home-page">
    主页
  </main>
</template>

<script setup lang="ts">
// Nuxt
import { useNuxtApp } from "nuxt/app";
// Utils
import _ from 'lodash';
// Hooks
import useRequest from 'vue-hooks-plus/es/useRequest'

</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.home-page {
  @include flex($direction: column, $gap: 40px);

  @media screen and (max-width: 576px) {
    gap: 24px;
  }
}
</style>