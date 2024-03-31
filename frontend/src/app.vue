<template>
  <Html lang="kk">

  <Head>
    <Meta charset="UTF-8" />
    <Meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <Meta name="theme-color" content="#002F34" />
    <meta name="color-scheme" content="light" />

    <Meta httpEquiv="x-ua-compatible" content="IE=edge" />
    <Meta httpEquiv="x-ua-compatible" content="IE=7" />

    <Meta name="description" content="Auto Parts Shop" />
    <Meta name="keywords" content="Auto Parts Shop" />
    <Meta name="author" content="https://github.com/YernarT" />

    <Link rel="icon" href="/favicon.ico" />

    <Link rel="preconnect" href="https://fonts.googleapis.com" />
    <Link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
    <Link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500&display=swap" rel="stylesheet" />

    <Title>Auto Parts</Title>
  </Head>

  <Body>
    <NuxtLayout>
      <a-config-provider :locale="kk_KZ" :theme="ANTD_THEME">
        <NuxtPage />
      </a-config-provider>
    </NuxtLayout>
  </Body>

  </Html>
</template>

<script setup lang="ts">
// Antd
import kk_KZ from "ant-design-vue/locale/kk_KZ";
import { ANTD_THEME } from '~/constants/antd-theme';
// Vue
import { onBeforeMount } from "vue";
// API
import { API_FetchCategories } from '~/service/api/product-api';
// Hooks
import { useRequest } from 'vue-hooks-plus';
// Store
import { useUserStore } from "~/stores/user";
import { useProductStore } from "~/stores/product";

// 获取商品分类 (全局)
useRequest(API_FetchCategories, {
  onSuccess(response) {
    const productStore = useProductStore();
    productStore.categoryList = response.data;
  }
});

// 初始化 Store
onBeforeMount(() => {
  const userStore = useUserStore();
  userStore.initUserFromLocal();
});
</script>

<style>
.page-enter-active,
.page-leave-active {
  transition: opacity var(--transition), filter var(--transition);
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(4px);
}
</style>