<template>
    <main class="itisit-container product-detail-page">
        <Breadcrumb class="breadcrumb" :items="bredcrumbItems" />
        <ProductGallery class="product-gallery" :gallery="product?.gallery ?? []" />
        <BuyBlock v-if="product" class="buy-block" :product="product" />
    </main>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product';
import type { I_BreadcrumbItem } from '~/components/common/Breadcrumb.vue';

// Vue
import { onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
// API
import { API_GetProduct, API_UpdateProduct } from '~/service/api/product-api';
// Hooks
import { useRequest } from 'vue-hooks-plus';
// Components
import Breadcrumb from '~/components/common/Breadcrumb.vue';
import ProductGallery from '~/components/product/ProductGallery.vue';
import BuyBlock from '~/components/product_page/BuyBlock.vue';

const route = useRoute();
const router = useRouter();

const { runAsync: getProduct } = useRequest(API_GetProduct, { manual: true });
const { runAsync: updateProduct } = useRequest(API_UpdateProduct, { manual: true });

const product = ref<I_Product | null>(null);
const bredcrumbItems = ref<I_BreadcrumbItem[]>([]);

onBeforeMount(() => {
    const productId = Number(route.params.id);
    if (Number.isNaN(productId)) return router.replace('/404');
    getProduct(productId)
        .then(({ data }) => product.value = data)
        .then(() => {
            // 初始化面包屑
            bredcrumbItems.value = product.value!.category.map(item => ({ label: item.title, link: `/?category=${item.id}` }));
            bredcrumbItems.value.push({ label: product.value!.title, link: '' })
        })
        .catch(() => router.replace('/404'))
})
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.product-detail-page {
    padding-top: 60px;
    padding-bottom: 80px;
    @include flex($direction: column);

    @media screen and (max-width: 576px) {
        padding-top: 40px;
        padding-bottom: 60px;
    }

    @media screen and (max-width: 404px) {
        padding-top: 24px;
        padding-bottom: 40px;
    }

    .breadcrumb {
        margin-bottom: 40px;
    }

    .product-gallery {
        width: 100%;
        height: 560px;
    }
}
</style>