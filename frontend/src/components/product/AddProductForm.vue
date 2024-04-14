<template>
  <a-card class="add-product-form">
    <a-form
      :model="formState"
      layout="vertical"
      autocomplete="off"
      @finish="onFinish"
    >
      <a-flex gap="24">
        <a-flex vertical gap="24">
          <a-form-item
            name="category"
            :autoLink="false"
            :rules="[
              {
                required: true,
                message: 'Категория міндетті',
              },
            ]"
          >
            <CategoryBlock
              singleChoice
              @pick="(category) => (formState.category = category)"
            />
          </a-form-item>
          <a-form-item name="applicable" :autoLink="false">
            <CategoryBlock
              title="Жарамды категориялар"
              @change="updateApplicable"
            />
          </a-form-item>
        </a-flex>

        <a-flex vertical>
          <a-form-item
            name="title"
            label="Атау"
            :rules="[
              {
                required: true,
                message: 'Атауы міндетті',
              },
            ]"
          >
            <a-input v-model:value="formState.title" />
          </a-form-item>

          <a-form-item name="description" label="Сипаттама">
            <a-textarea
              v-model:value="formState.description"
              showCount
              maxLength="254"
            />
          </a-form-item>

          <a-row>
            <a-form-item
              name="price"
              label="Баға"
              :rules="[{ type: 'number', min: 100, max: 10_000_000 }]"
            >
              <a-input-number v-model:value="formState.price" />
            </a-form-item>

            <a-form-item name="isNew" label="Күйі">
              <a-radio-group v-model:value="formState.isNew">
                <a-radio :value="true">Жаңа</a-radio>
                <a-radio :value="false">Ескі</a-radio>
              </a-radio-group>
            </a-form-item>
          </a-row>

          <a-form-item name="type" label="Типы">
            <a-radio-group v-model:value="formState.type">
              <a-radio
                v-for="_type in TYPE_LIST"
                :key="_type.key"
                :value="_type.key"
              >
                {{ _type.label }}
              </a-radio>
            </a-radio-group>
          </a-form-item>

          <a-form-item
            name="gallery"
            class="gallery-block"
            label="Суреттер"
            extra="Әр сурет 2 МБ-тан аспауы керек"
          >
            <a-upload
              multiple
              :maxCount="10"
              accept="image/*"
              list-type="picture-card"
              :beforeUpload="beforeUpload"
              @remove="removeImage"
            >
              <Icon name="material-symbols:upload" />
              <span class="hint-text">Жүктеу</span>
            </a-upload>
          </a-form-item>

          <a-form-item>
            <a-button
              block
              size="large"
              type="primary"
              html-type="submit"
              :loading="loadingAddProduct"
            >
              Жариялау
            </a-button>
          </a-form-item>
        </a-flex>
      </a-flex>
    </a-form>
  </a-card>
</template>

<script setup lang="ts">
// Types
import type { I_CategoryFilter, I_SubCategory } from "~/types/product";

// Vue
import { defineOptions, reactive } from "vue";
// Store
import { useUserStore } from "~/stores/user";
// Hooks
import { useRequest } from "vue-hooks-plus";
// API
import { API_AddProduct } from "~/service/api/product-api";
// Constants
import { INITIAL_PRODUCT_FORMSTATE } from "~/constants/product";
import { TYPE_LIST } from "~/constants/product-type";
// Components
import CategoryBlock from "~/components/common/FilterPanel/CategoryBlock.vue";
import { message } from "ant-design-vue";

defineOptions({ name: "AddProductForm" });

const userStore = useUserStore();
const formState = reactive(INITIAL_PRODUCT_FORMSTATE);

const beforeUpload = (file: File) => {
  formState.gallery.push(file);

  return false;
};

const removeImage = (file: File) => {
  formState.gallery = formState.gallery.filter(
    // @ts-ignore
    (image) => image.uid !== file.uid
  );
};

const updateApplicable = (applicable: I_CategoryFilter[]) => {
  const selectedApplicable = [] as I_CategoryFilter["id"][];
  applicable.forEach((category) => {
    if (category.isSelected) {
      selectedApplicable.push(
        ...category.subCategories.map((subCategory) => subCategory.id)
      );
    } else {
      category.subCategories.forEach((subCategory) => {
        subCategory.isSelected && selectedApplicable.push(subCategory.id);
      });
    }
  });
  formState.applicable = selectedApplicable;
};

const { run: addProduct, loading: loadingAddProduct } = useRequest(
  API_AddProduct,
  {
    manual: true,
    onSuccess(response) {
      if (response.isOk) {
        message.success("Объявление жарияланды");
      }
    },
    onError(error) {
      message.error(error.message);
    },
  }
);

const onFinish = (values: typeof formState) => {
  addProduct({ ...values, seller: userStore.id });
};
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.add-product-form {
  .gallery-block {
    :deep(.ant-form-item-extra) {
      font-size: 16px;
    }

    :deep(.ant-upload-list-item-actions) {
      a {
        display: none;
      }
    }

    :deep(span.ant-upload) {
      @include flex($direction: column);

      .hint-text {
        font-size: 16px;
      }
    }
  }
}
</style>
