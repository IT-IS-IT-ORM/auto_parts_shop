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
      <NuxtPage />
    </NuxtLayout>
  </Body>

  </Html>
</template>

<script setup lang="ts">
// Vue
import { onBeforeMount } from "vue";
// Store
import { useUser } from "~/stores/user";

// 初始化 Store
onBeforeMount(() => {
  const user = useUser();
  user.initUserFromLocal();
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