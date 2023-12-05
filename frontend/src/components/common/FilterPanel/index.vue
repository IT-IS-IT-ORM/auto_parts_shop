<template>
    <div class="filter-panel">
        <TypeBlock ref="typeBlock" class="type-block" @change="handleChangeType" />
        <PriceBlock ref="priceBlock" class="price-block" @change="handleChangePriceBlock" @search="handleSearch" />
        <CategoryBlock ref="categoryBlock" class="category-block" />
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product';

// Routes
import { useRoute, useRouter } from 'vue-router';
// Store
import { useProduct } from '~/stores/product';
// Components
import TypeBlock from './TypeBlock.vue';
import CategoryBlock from './CategoryBlock.vue';
import PriceBlock from './PriceBlock.vue';

interface I_ProductFilter {
    type: I_Product['type'] | null;
    hasImage: boolean;
    isNew: boolean;
    priceRange: [number | null, number | null];
}

const filter = ref<I_ProductFilter>({
    type: null,
    hasImage: false,
    isNew: false,
    priceRange: [null, null]
});
const typeBlock = ref();
const priceBlock = ref();
const categoryBlock = ref();

const $route = useRoute();
const $router = useRouter();
const productStore = useProduct();

const setFilterByQueryParams = (queryParams: Partial<I_ProductFilter>) => {
    // 这个成功了
    typeBlock.value.handleItemClick('md');
    // TODO:
    // 把其余组件都写成这样的 非 setup 语法糖的形式
    

    // filter.value.type = queryParams.type ?? null;
    // filter.value.hasImage = queryParams.hasImage ?? false;
    // filter.value.isNew = queryParams.isNew ?? false;
    // @ts-ignore
    // filter.value.priceRange = queryParams.priceRange.split(',').map(priceStringOrEmptyString => {
        // if (priceStringOrEmptyString === '') return null;
        // return parseInt(priceStringOrEmptyString);
    // }) ?? [null, null];
}

// watch(() => $route.query, setFilterByQueryParams, { immediate: true });
onMounted(() => setFilterByQueryParams(toRaw($route.query)));

const handleSearch = () => {
    let categories: number[] = [], subCategories: number[] = [];

    productStore.categoryList.forEach(category => {
        if (category.isSelected) {
            categories.push(category.id);
        } else {
            category.subCategories.forEach(subCategory => {
                if (subCategory.isSelected) {
                    subCategories.push(subCategory.id);
                }
            });
        }
    });

    const filterObj = toRaw(filter.value);
    // @ts-ignore
    if (categories.length) filterObj.categories = categories
    // @ts-ignore
    if (subCategories.length) filterObj.subCategories = subCategories

    $router.push(`/?${objectToUrlParams(filterObj)}`)
};

const handleChangeType = (type: I_Product['type'] | null) => {
    filter.value.type = type;
}

const handleChangePriceBlock = (form: { hasImage: boolean, isNew: boolean, minPrice: number | null, maxPrice: number | null }) => {
    filter.value.hasImage = form.hasImage;
    filter.value.isNew = form.isNew;
    filter.value.priceRange = [form.minPrice, form.maxPrice];
}
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