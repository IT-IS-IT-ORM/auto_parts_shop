<template>
  <main class="itisit-container home-page">
    <FilterPanel class="filter-panel" />

    <div class="card-list">
      <ProductCard v-for="(product, index) in productList" :key="index" :product="product" />
    </div>
  </main>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from "~/types/product";

// Nuxt
import { useNuxtApp } from "nuxt/app";
// Utils
import _ from "lodash";
// Hooks
import useRequest from "vue-hooks-plus/es/useRequest";
// API
import { API_GetProductList } from "~/service/api/product-api";
// Components
import FilterPanel from '~/components/common/FilterPanel/index.vue';
import ProductCard from '~/components/product/ProductCard.vue';

const productList = ref<I_Product[]>([]);

useRequest(API_GetProductList, {
  onSuccess({ data }) {
    productList.value = data;
  }
})

</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.home-page {
  padding-top: 60px;
  padding-bottom: 80px;
  @include flex($direction: column, $gap: 40px);

  @media screen and (max-width: 576px) {
    padding-top: 40px;
    padding-bottom: 60px;
    gap: 24px;
  }

  @media screen and (max-width: 404px) {
    padding-top: 24px;
    padding-bottom: 40px;
    gap: 20px;
  }
}

.card-list {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 100%));
  gap: 40px;

  @media screen and (max-width: 1480px) {
    grid-template-columns: repeat(3, minmax(0, 100%));
    gap: 32px;
  }

  @media screen and (max-width: 768px) {
    grid-template-columns: repeat(2, minmax(0, 100%));
    gap: 24px;
  }
  @media screen and (max-width: 576px) {
    gap: 8px;
  }
}
</style>
