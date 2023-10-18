<template>
    <div class="info-block">
        <div class="applicable">
            <span>Келесі категорияларғада қолдануға болады:</span>
            <ul class="applicable-list">
                <li v-for="subCategory in product.applicable" :key="subCategory.id" class="sub-category">
                    {{ subCategory.title }}
                </li>
            </ul>
        </div>

        <h4 class="title">
            Сипаттама
        </h4>

        <p v-html="description" class="description"></p>

        <span class="views">Көрулер саны: {{ product.views }}</span>
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product';

const props = defineProps<{
    product: I_Product
}>();

// 多个 \n 带来的 margin 会塌陷为 1 个
const description = computed(() => props.product.description.replaceAll('\\n', '<div class="splitor"></div>'));
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.info-block {
    width: 100%;
    padding: 24px;
    border-radius: var(--border-radius);
    background-color: #fff;
    @include flex($direction: column);

    @media screen and (max-width: 576px) {
        padding: 16px;
    }

    .applicable {
        margin-bottom: 24px;
        @include flex($direction: column, $gap: 16px);

        .applicable-list {
            list-style: none;
            @include flex($alignItems: center, $gap: 8px, $wrap: wrap);

            .sub-category {
                padding: 8px 12px;
                border-radius: var(--border-radius);
                border: 1px solid var(--c-border);
            }
        }
    }

    .title {
        font-size: 28px;
        margin-bottom: 24px;
    }

    .description {
        word-break: break-word;
        line-height: 24px;
        font-size: 16px;
        color: var(--c-primary);
        padding-bottom: 24px;
        margin-bottom: 16px;
        border-bottom: 1px solid var(--c-border);

        :deep(.splitor) {
            /* 多个 \n 带来的 margin 会塌陷为 1 个 */
            margin: 12px 0;
        }
    }

    .views {
        font-weight: 300;
        font-size: 16px;
        color: var(--c-text-secondary);
    }
}
</style>