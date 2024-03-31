<template>
  <div class="block">
    <span class="title">{{ props.title }}</span>

    <ul class="category-list">
      <li v-for="category in categoryList" :key="category.id" class="category">
        <div class="info">
          <a-checkbox v-model:checked="category.isSelected" />
          <span>{{ category.title }}</span>
          <Icon
            :class="{ up: !category.isCollapsed }"
            name="material-symbols:keyboard-arrow-down"
            @click.stop="category.isCollapsed = !category.isCollapsed"
          />
        </div>

        <ul
          class="sub-category-list"
          :class="{ 'sub-category-list--collapsed': category.isCollapsed }"
          :style="{
            '--height': `calc(32px * ${category.subCategories.length})`,
          }"
        >
          <li
            v-for="subCategory in category.subCategories"
            :key="subCategory.id"
            class="sub-category"
          >
            <a-checkbox v-model:checked="subCategory.isSelected" />
            <span>{{ subCategory.title }}</span>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
// Types
import type { I_CategoryFilter } from "~/types/product";

// Vue
import { reactive, watch } from "vue";
// Store
import { useProductStore } from "~/stores/product";

const props = defineProps({
  title: {
    type: String,
    default: "Категория",
  },
  singleChoice: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits<{
  (event: "change", value: I_CategoryFilter[]): void;
}>();

const toRawByJSON = (variable: unknown) => {
  return JSON.parse(JSON.stringify(variable));
};

const productStore = useProductStore();
const categoryList = reactive<I_CategoryFilter[]>(
  toRawByJSON(productStore.categoryList).map((category: any) => {
    const isParentCategory = category.parentId !== null;
    category.isSelected = false;
    if (isParentCategory) {
      category.isCollapsed = false;
    } else {
      category.subCategories.map((category: any) => ({
        ...category,
        isSelected: false,
      }));
    }
    return category;
  })
);

watch(
  () => categoryList,
  (newVal, oldVal) => {
    console.log(newVal, oldVal);

    // emit("change", toRawByJSON(newVal))
  },
  { deep: true }
);
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.block > .title {
  display: block;
  margin-bottom: 4px;
}

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

      & > span {
        font-weight: 500;
      }

      & > svg {
        margin-left: auto;
        transition: transform var(--transition);
        @include svgStyle($size: 28px);
      }

      & > .up {
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

  @media screen and (max-width: 768px) {
    max-width: 100%;
    width: 100%;
    padding: 16px;
    flex-direction: row;
    flex-wrap: wrap;

    .category {
      width: max-content;
    }
  }
}
</style>
