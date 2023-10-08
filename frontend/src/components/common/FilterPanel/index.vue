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
    /* padding: 16px; */
    padding: 16px 24px;
    border: 1px solid var(--c-border);
    border-radius: var(--border-radius);
    box-shadow: rgba(60, 64, 67, 0.3) 0 1px 2px 0, rgba(60, 64, 67, 0.15) 0 1px 3px 1px;
    
    display: grid;
    grid-template-columns: max-content;
    grid-template-areas: 'category type'
        'category price';

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
        @include flex($direction: column, $gap: 12px);

        .title {
            font-weight: 500;
            font-size: 24px;
        }
    }
}
</style>