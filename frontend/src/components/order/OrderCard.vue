<template>
  <div class="order-card">
    <Descriptions title="Заказ">
      <DescriptionsItem label="">
        <NuxtLink :to="`/product/${order.product.id}`">
          {{ order.product.title }}
        </NuxtLink>
      </DescriptionsItem>
      <DescriptionsItem label="Баға">{{ order.price }}</DescriptionsItem>
      <DescriptionsItem label="Уақыт">
        {{ dateFormatter(order.createTime, true) }}
      </DescriptionsItem>
    </Descriptions>
  </div>
</template>

<script setup lang="ts">
// Types
import type { I_Order } from "~/types/order";
import type { I_Product } from "~/types/product";

// Utils
import dateFormatter from "~/utils/formatDate";
// Components
import { Descriptions, DescriptionsItem } from "ant-design-vue";

// const $emit = defineEmits<{ (event: "favorite", value: boolean): void }>();

const route = useRoute();
const props = defineProps<{ order: I_Order }>();
const { order } = toRefs(props);
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.order-card {
  width: 100%;
  padding: 12px;
  padding-bottom: 0;
  cursor: pointer;
  border-radius: var(--border-radius);
  border: 1px solid var(--c-border);
  @include flex($direction: column);

  :deep(.ant-descriptions-header) {
    margin-bottom: 8px;
    .ant-descriptions-title {
      font-size: 20px;
      font-weight: 500;
    }
  }
}
</style>
