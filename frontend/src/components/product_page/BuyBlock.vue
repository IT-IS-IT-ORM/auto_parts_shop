<template>
    <div class="buy-block">
        <div class="row">
            <p class="create-time">
                Жарияланды {{ dateFormatter(product.createTime, true) }}
            </p>
            <Icon name="material-symbols:favorite-outline-rounded" role="button" />
        </div>

        <div class="name">
            <div class="is-new">
                {{ product.isNew ? 'Жаңа' : 'Ескі' }}
            </div>
            <h1>
                {{ product.title }}
            </h1>
        </div>
        <span class="price">{{ product.price }} тг</span>
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

    @media screen and (max-width: 576px) {
        padding: 16px;
    }

    .row {
        width: 100%;
        @include flex($justifyContent: space-between, $alignItems: center, $gap: 8px);

        .create-time {
            font-weight: 300;
            font-size: 14px;
            color: var(--c-text-secondary);
        }
    }

    .name {
        margin: 8px 0 16px;
        @include flex($alignItems: center, $gap: 8px);

        .is-new {
            font-size: 16px;
            padding: 6px 10px;
            border-radius: var(--border-radius);
            border: 1px solid var(--c-border);
        }

        h1 {
            font-size: 18px;
            @include maxRow($rowCount: 4, $rowHeight: 24px);
        }
    }

    .price {
        font-weight: 500;
        font-size: 22px;
        margin-bottom: 16px;
    }

    .custom-button {
        margin-top: auto;
    }
}
</style>