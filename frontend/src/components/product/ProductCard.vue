<template>
    <div class="product-card">
        <img class="image" :src="productCover" :alt="product.title" />

        <div class="whole-info-card">
            <div class="row-1">
                <span class="title">{{ product.title }}</span>
                <Icon class="favorite-icon-btn" name="material-symbols:favorite-outline-rounded" role="button" />
            </div>

            <span class="price">{{ product.price }} ₸</span>

            <div class="category">
                <span v-for="category in product.category" :key="category.id">
                    {{ category.title }}
                </span>
            </div>

            <div class="row-2">
                <span>9 окт.</span>
                <Icon name="ic:baseline-remove-red-eye" />
                <span>{{ product.price }}</span>
            </div>
        </div>
    </div>
</template>
  
<script setup lang="ts">
import type { I_Product } from '~/types/product'

const props = defineProps<{ product: I_Product; }>();
const { product } = toRefs(props);

const productCover = computed(() => {
    if (product.value.gallery.length > 0) {
        return product.value.gallery[0];
    }

    return dynamicAsset.image('product/no-image.jpg');
});

// 格式化 浏览量
// const formatViews = computed(()=>{
    // product.value.
// })

// 格式化 创建日期
// const formatCreateTime = computed(()=>{
    // product.value.
// })
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
  