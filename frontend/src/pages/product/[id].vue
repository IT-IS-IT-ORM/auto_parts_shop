<template>
  <main class="itisit-container product-detail-page">
    <Breadcrumb class="breadcrumb" :items="bredcrumbItems" />
    <div class="row">
      <ProductGallery
        class="product-gallery"
        :gallery="product?.gallery ?? []"
      />
      <div class="col">
        <BuyBlock v-if="product" class="buy-block" :product="product" />
        <SellerBlock v-if="product" class="seller-block" :product="product" />
      </div>
    </div>
    <InfoBlock v-if="product" class="info-block" :product="product" />
  </main>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from "~/types/product";
import type { I_BreadcrumbItem } from "~/components/common/Breadcrumb.vue";

// Vue
import { onBeforeMount } from "vue";
import { useRoute, useRouter } from "vue-router";
// API
import { API_GetProduct, API_UpdateProduct } from "~/service/api/product-api";
// Hooks
import { useRequest } from "vue-hooks-plus";
// Components
import Breadcrumb from "~/components/common/Breadcrumb.vue";
import ProductGallery from "~/components/product/ProductGallery.vue";
import BuyBlock from "~/components/product_page/BuyBlock.vue";
import SellerBlock from "~/components/product_page/SellerBlock.vue";
import InfoBlock from "~/components/product_page/InfoBlock.vue";

const route = useRoute();
const router = useRouter();

const { runAsync: getProduct } = useRequest(API_GetProduct, { manual: true });
const { runAsync: updateProduct } = useRequest(API_UpdateProduct, {
  manual: true,
});

const product = ref<I_Product | null>(null);
const bredcrumbItems = ref<I_BreadcrumbItem[]>([]);

onBeforeMount(() => {
  const productId = Number(route.params.id);
  if (Number.isNaN(productId)) return router.replace("/404");
  getProduct(productId)
    .then(({ data }) => (product.value = data))
    .then(() => {
      // 初始化面包屑
      bredcrumbItems.value = product.value!.category.map((item) => ({
        label: item.title,
        link: `/?category=${item.id}`,
      }));
      bredcrumbItems.value.push({ label: product.value!.title, link: "" });
    })
    .catch(() => router.replace("/404"));
});
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.product-detail-page {
  padding-top: 60px;
  padding-bottom: 80px;
  @include flex($direction: column);

  .breadcrumb {
    margin-bottom: 24px;
  }

  & > .row {
    width: 100%;
    margin-bottom: 24px;
    @include flex;

    & > .col {
      flex: 0 1 max-content;
      @include flex($direction: column, $gap: 8px);

      & > * {
        width: 100%;
      }
    }
  }

  .product-gallery {
    flex: 1 1 auto;
    aspect-ratio: 4 / 3.3;
    max-width: 660px;
    min-height: 430px;
    margin-right: 8px;
    margin-bottom: 24px;
  }

  @media screen and (max-width: 1144px) {
    & > .row {
      flex-direction: column;

      & > .col {
        width: 100%;
        flex: 1 1 100%;
        flex-direction: row;
        gap: 16px;

        & > * {
          flex: 1 1 auto;
          width: calc(50% - 16px);
          min-height: 212px;
        }
      }
    }

    .product-gallery {
      width: 100%;
      max-width: 100%;
      margin-right: 0;
    }
  }

  @media screen and (max-width: 870px) {
    & > .row {
      & > .col {
        flex-direction: column;

        & > * {
          flex: 1 1 auto;
          width: 100%;
        }
      }
    }
  }

  @media screen and (max-width: 576px) {
    padding-top: 40px;
    padding-bottom: 60px;

    .product-gallery {
      aspect-ratio: 3.3 / 4;
      max-height: 365px;
    }
  }

  @media screen and (max-width: 404px) {
    padding-top: 24px;
    padding-bottom: 40px;
  }
}
</style>
