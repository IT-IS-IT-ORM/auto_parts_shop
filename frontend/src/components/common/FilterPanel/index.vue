<template>
    <div class="filter-panel">
        <TypeBlock class="type-block" />
        <PriceBlock class="price-block" />
        <CategoryBlock class="category-block" />
    </div>
</template>

<script setup lang="ts">
// Components
import TypeBlock from './TypeBlock.vue';
import CategoryBlock from './CategoryBlock.vue';
import PriceBlock from './PriceBlock.vue';
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.filter-panel {
    width: 100%;
    display: grid;
    grid-template-columns: max-content;
    grid-auto-rows: max-content 1fr;
    grid-template-areas:
        'category type'
        'category price';
    align-items: start;
    gap: 8px;

    .type-block {
        grid-area: type;
    }

    .price-block {
        grid-area: price;
    }

    .category-block {
        grid-area: category;
    }


    &>:deep(.block) {
        @include flex($direction: column, $gap: 20px);

        .title {
            font-weight: 500;
            font-size: 24px;
        }
    }

    @media screen and (max-width: 768px) {
        grid-template-columns: 100%;
        grid-template-areas:
            'type'
            'category'
            'price';
        gap: 24px;
    }
}
</style>