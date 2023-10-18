<template>
    <div class="info-block">
        <h4 class="title">
            Сипаттама
        </h4>

        <p class="description">
            {{ product.description }}
        </p>
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product';

// Components
import Button from '~/components/common/Button.vue';

defineProps<{
    product: I_Product
}>();
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

    .description {}


}
</style>