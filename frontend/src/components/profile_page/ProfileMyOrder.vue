<template>
  <div class="card-list">
    <OrderCard v-for="order in myOrderList" :key="order.id" :order="order" />
  </div>

  <div v-if="!loading && myOrderList.length === 0" class="empty">
    <p>Сіз әлі ешқандай затты стаып алмағансыз.</p>
    <p>Барып, заттарды затып алыңыз</p>
    <Button @click="$router.push('/')">Заттарды шолу</Button>
  </div>
</template>

<script setup lang="ts">
// Types
import type { I_Order } from "~/types/order";

// API
import { API_GetOrderList } from "~/service/api/order-api";
// Hooks
import { useRequest } from "vue-hooks-plus";
// Components
import Button from "~/components/common/Button.vue";
import OrderCard from "~/components/order/OrderCard.vue";

const myOrderList = ref<I_Order[]>([]);

const { loading } = useRequest(API_GetOrderList, {
  onSuccess({ data }) {
    myOrderList.value = data;
  },
});
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.card-list {
  @include flex($direction: column, $gap: 16px);
}

.empty {
  @include flex($direction: column, $gap: 12px);
}
</style>
