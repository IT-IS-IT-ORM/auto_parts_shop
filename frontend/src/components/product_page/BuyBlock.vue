<template>
    <div class="buy-block">
        <div class="row">
            <p class="create-time">
                Жарияланды {{ dateFormatter(product.createTime, true) }}
            </p>
            <Icon name="material-symbols:favorite-outline-rounded" role="button" />
        </div>

        <p class="name">{{ product.title }}</p>
        <p class="price">{{ product.price }} тг</p>
        <Button block>Заказ жасау</Button>
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product';

// Utils
import dateFormatter from '~/utils/formatDate';
// Components
import Button from '~/components/common/Button.vue';

defineProps<{
    product: I_Product
}>();
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.buy-block {
    padding: 24px;
    border-radius: var(--border-radius);
    background-color: #fff;
    @include flex($direction: column);

    .row {
        @include flex($justifyContent: space-between, $alignItems: center, $gap: 8px);

        .create-time {
            font-weight: 300;
            font-size: 14px;
            color: var(--c-text-secondary);
        }
    }

    .name {
        margin: 8px 0 16px;
    }

    .price {
        font-weight: 500;
        font-size: 22px;
        margin-bottom: 16px;
    }
}
</style>