<template>
  <div class="default-layout">
    <slot></slot>
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.default-layout {
  position: relative;
  background: var(--c-background);
}
</style>
