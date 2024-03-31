<template>
    <div class="product-card">
        <img class="image" :src="productCover" :alt="product.title" />

        <div class="whole-info-card">
            <div class="row-1">
                <span class="title">{{ product.title }}</span>
                <Icon v-if="!product.isFavorite" class="favorite-icon-btn" name="material-symbols:favorite-outline-rounded"
                    role="button" @click.stop="handleFavorite" />
                <Icon v-if="product.isFavorite" class="favorite-icon-btn" name="material-symbols:favorite-rounded"
                    role="button" @click.stop="handleFavorite" />
            </div>

            <span class="price">{{ product.price }} ₸</span>

            <div class="category">
                <span v-for="category in product.category" :key="category.id">
                    {{ category.title }}
                </span>
            </div>

            <div class="row-2">
                <span>{{ dateFormatter(product.createTime, false) }}</span>
                <Icon name="ic:baseline-remove-red-eye" />
                <span>{{ product.views }}</span>
            </div>
        </div>
    </div>
</template>
  
<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product'

// Store
import { useUserStore } from '~/stores/user';
import { useModalStore } from '~/stores/modal';
// Hooks
import { useRequest } from 'vue-hooks-plus';
// API
import { API_SetFavorite } from '~/service/api/product-api';
// Utils
import dateFormatter from '~/utils/formatDate';

const $emit = defineEmits<{ (event: 'favorite', value: boolean): void }>();

const userStore = useUserStore();
const modalStore = useModalStore();
const route = useRoute();
const props = defineProps<{ product: I_Product; }>();
const { product } = toRefs(props);

const productCover = computed(() => {
    if (product.value.gallery.length > 0) {
        return product.value.gallery[0].image;
    }

    return dynamicAsset.image('product/no-image.jpg');
});

const { loading, runAsync } = useRequest(API_SetFavorite, { manual: true });

const handleFavorite = () => {
    if (!userStore.isAuthenticated) {
        modalStore.loginReuiqredModal.open = true;
        modalStore.loginReuiqredModal.nextUrl = route.path;
        modalStore.loginReuiqredModal.actionDescription = 'Таңдауларға қосу';
        return;
    }

    const newState = !product.value.isFavorite;
    runAsync({ productId: product.value.id, isFavorite: newState }).then(() => {
        $emit('favorite', newState);
    });
}
</script>
  
<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.product-card {
    height: max-content;
    cursor: pointer;
    border-radius: var(--border-radius);
    border: 1px solid var(--c-border);
    @include flex($direction: column);

    .image {
        width: 100%;
        border-radius: var(--border-radius) var(--border-radius) 0 0;
        aspect-ratio: 4 / 3;
        object-fit: cover;
    }

    .whole-info-card {
        width: 100%;
        padding: 16px;
        border-radius: 0 0 var(--border-radius) var(--border-radius);
        background-color: #fff;

        .row-1 {
            @include flex($justifyContent: space-between, $gap: 4px);

            .title {
                font-size: 16px;
            }

            .favorite-icon-btn {
                flex-shrink: 0;
            }
        }

        .price {
            font-weight: 500;
            font-size: 16px;
            display: block;
            margin: 8px 0 12px;
        }

        .category {
            width: 100%;
            overflow: auto hidden;
            @include flex($alignItems: center, $gap: 8px);

            span {
                padding: 2px 8px;
                border-radius: var(--border-radius);
                border: 1px solid var(--c-border);
                font-size: 16px;
                color: var(--c-primary);
                transition: color var(--transition), background-color var(--transition);

                &:hover {
                    color: #fff;
                    background-color: var(--c-primary);
                }
            }
        }

        .row-2 {
            margin-top: 12px;
            @include flex($alignItems: center, $gap: 4px);

            span {
                font-weight: 300;
                font-size: 14px;
                color: var(--c-text-secondary);
            }

            svg {
                margin-left: 10px;
                @include svgStyle($color: var(--c-text-secondary), $size: 16px);
            }
        }
    }
}
</style>
  