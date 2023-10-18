<template>
    <div class="info-block">
        <h4 class="title">
            Сипаттама
        </h4>

        <p v-html="description" class="description"></p>
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

    .title {
        font-size: 28px;
        margin-bottom: 24px;
    }

    .description {
        word-break: break-word;
        line-height: 24px;
        font-size: 16px;
        color: var(--c-primary);

        :deep(.splitor) {
            /* 多个 \n 带来的 margin 会塌陷为 1 个 */
            margin: 12px 0;
        }
    }
}
</style>