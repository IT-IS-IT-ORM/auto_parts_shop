<template>
  <a-button
    class="custom-button"
    :class="[
      `custom-button--${variant}`,
      block && `custom-button--block`,
      loading && `custom-button--loading`,
    ]"
  >
    <slot></slot>
    <Spin v-show="loading" />
  </a-button>
</template>

<script setup lang="ts">
// Components
import { Spin } from "ant-design-vue";

export type allowedButtonVariants = "primary" | "secondary";

defineProps({
  block: {
    type: Boolean,
    default: false,
  },
  loading: {
    type: Boolean,
    default: false,
  },
  variant: {
    type: String,
    default: "primary",
  },
});
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.custom-button {
  height: auto;
  padding: 4px 16px;
  border: 4px solid transparent;
  position: relative;
  @include flexCenter;

  :deep(span) {
    font-weight: 500;
  }

  &--block {
    width: 100%;
  }

  &--primary {
    color: #fff;
    border-color: var(--c-primary);
    background-color: var(--c-primary);

    &:hover {
      color: var(--c-primary);
      border-color: var(--c-primary);
      background-color: #fff;
    }
  }

  &--secondary {
    color: var(--c-primary);
    border-color: #fff;
    background-color: #fff;

    &:hover {
      color: #fff;
      border-color: #fff;
      background-color: var(--c-primary);
    }
  }

  &--loading {
    pointer-events: none;
    background-image: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%);
  }

  .ant-spin {
    @include positionCenter;
  }
}
</style>
