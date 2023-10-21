<template>
    <div class="card-list">
        <ProductCard v-for="(product, index) in favoriteProductList" :key="index" :product="product"
            @click="$router.push(`/product/${product.id}`)" @favorite="isFavorite => product.isFavorite = isFavorite" />
    </div>

    <div v-if="!loading && favoriteProductList.length === 0" class="empty">
        <p>Сіз әлі ешқандай затты жинаған жоқсыз.</p>
        <p>Барып, заттарды шолыңыз</p>
        <Button @click="$router.push('/')">Заттарды шолу</Button>
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from 'types/product';

// API
import { API_GetFavoriteProductList } from '~/service/api/product-api';
// Hooks
import { useRequest } from 'vue-hooks-plus';
// Components
import Button from '~/components/common/Button.vue';
import ProductCard from '~/components/product/ProductCard.vue';

const favoriteProductList = ref<I_Product[]>([]);

const { loading } = useRequest(API_GetFavoriteProductList, {
    onSuccess({ data }) {
        favoriteProductList.value = data;
    }
})

</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

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

.empty {
    @include flex($direction: column, $gap: 12px);
}
</style>