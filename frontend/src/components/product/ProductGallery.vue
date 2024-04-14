<template>
  <div class="product-gallery">
    <div
      v-show="hasPrev"
      class="prev-btn"
      role="button"
      @click="activeIndex -= 1"
    >
      <Icon name="ic:baseline-arrow-back-ios" />
    </div>
    <div
      v-show="hasNext"
      class="next-btn"
      role="button"
      @click="activeIndex += 1"
    >
      <Icon name="ic:baseline-arrow-forward-ios" />
    </div>

    <img
      v-for="(data, index) in gallery"
      :key="data.id"
      :src="data.image"
      class="image"
      :class="{ 'image--active': index === activeIndex }"
    />

    <img
      v-if="gallery.length === 0"
      class="image"
      :src="dynamicAsset.image('product/no-image.jpg')"
      alt="no-image"
    />
  </div>
</template>

<script setup lang="ts">
import type { I_Product } from "~/types/product";

const props = defineProps<{
  gallery: I_Product["gallery"];
}>();

const activeIndex = ref(0);
const hasPrev = computed(() => activeIndex.value !== 0);
const hasNext = computed(() => activeIndex.value < props.gallery.length - 1);
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.product-gallery {
  border-radius: var(--border-radius);
  background-color: #fff;
  position: relative;

  .image {
    width: calc(100% - calc(30px * 2));
    height: calc(100% - calc(30px * 2));
    object-fit: cover;
    border-radius: inherit;
    opacity: 0;
    transition: opacity var(--transition);
    @include positionCenter;

    &--active {
      opacity: 1;
    }
  }

  .prev-btn,
  .next-btn {
    width: 32px;
    height: 34px;
    border-radius: var(--border-radius);
    border: 1px solid #f2f4f5;
    background-color: #f2f4f5;
    transform: translateY(-50%);
    cursor: pointer;
    @include flexCenter;
    @include positioned($top: 50%, $left: 38px, $zIndex: 3);
  }

  .prev-btn {
    svg {
      transform: translateX(20%);
    }
  }

  .next-btn {
    transform: translate(-100%, -50%);
    left: calc(100% - 38px);
  }
}
</style>
