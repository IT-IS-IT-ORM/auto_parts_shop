<template>
    <div class="block">
        <span class="title">Категория</span>

        <ul class="category-list">
            <li v-for="category in categoryList" :key="category.id" class="category">
                <div class="info" @click="toggleSelectedState(category, false)">
                    <a-checkbox :checked="category.isSelected" />
                    <span>{{ category.title }}</span>
                    <Icon :class="{ up: !category.isCollapsed }" name="material-symbols:keyboard-arrow-down"
                        @click.stop="category.isCollapsed = !category.isCollapsed" />
                </div>

                <ul class="sub-category-list" :class="{ 'sub-category-list--collapsed': category.isCollapsed }"
                    :style="{ '--height': `calc(32px * ${category.subCategories.length})` }">
                    <li v-for="subCategory in category.subCategories" :key="subCategory.id" class="sub-category"
                        @click="toggleSelectedState(subCategory, true)">
                        <a-checkbox :checked="subCategory.isSelected" />
                        <span>{{ subCategory.title }}</span>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Category, I_SubCategory } from '~/types/product';

// Store
import { useProduct } from '~/stores/product';

const productStore = useProduct();
const { categoryList } = toRefs(productStore);

const toggleSelectedState = (category: any, isSubCategory: boolean) => {
    const checkedState = !category.isSelected
    category.isSelected = checkedState;

    if (!isSubCategory) {
        category.subCategories.forEach((subCategory: any) => {
            subCategory.isSelected = checkedState;
        })
    }
}

</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.category-list {
    max-width: 240px;
    padding: 16px 24px;
    border-radius: var(--border-radius);
    border: 1px solid var(--c-border);
    background-color: #fff;
    @include flex($direction: column, $gap: 8px);

    .category {
        width: 100%;
        margin-bottom: 20px;
        @include flex($direction: column, $gap: 4px);

        .info {
            width: 100%;
            height: 32px;
            cursor: pointer;
            @include flex($alignItems: center, $gap: 8px);

            &>span {
                font-weight: 500;
            }

            &>svg {
                margin-left: auto;
                transition: transform var(--transition);
                @include svgStyle($size: 28px);
            }

            &>.up {
                transform: rotate(180deg);
            }
        }

        .sub-category-list {
            width: 100%;
            margin-left: 32px;
            height: 0;
            transform-origin: top center;
            transform: scaleY(0);
            transition: height var(--transition), transform var(--transition);
            @include flex($direction: column, $gap: 4px);

            &--collapsed {
                height: var(--height);
                transform: scaleY(1);
            }

            .sub-category {
                width: 100%;
                height: 32px;
                cursor: pointer;
                @include flex($alignItems: center, $gap: 8px);
            }
        }
    }

    :deep(.ant-checkbox-inner) {
        width: 24px;
        height: 24px;

        &::after {
            width: 8px;
            height: 14px;
            top: 45%;
            left: 24%;
        }
    }
}
</style>