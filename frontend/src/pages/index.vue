<template>
  <main class="home-page">
    <!--下面很长的都是card-->
    <div class="card-container">
      <template v-for="(item, itemInd) in items" :key="itemInd">
        <CommonItemCard  :item-data="item"/>
      </template>
    </div>
  </main>
</template>

<script setup lang="ts">
// Nuxt
import { useNuxtApp } from "nuxt/app";
// Utils
import _ from "lodash";
// Hooks
import useRequest from "vue-hooks-plus/es/useRequest";

const items = ref<any[]>([]);

onMounted(() => {
  // fetch items from back-end

  // now generating for test
  for(let i: number = 0; i < 2; i++) {
    items.value.push(itemsGenerator.generateItem());
  }
})

</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.home-page { @include flex($direction: column, $gap: 40px);
  @media screen and (max-width: 576px) {
    gap: 24px;
  }
  background-color: rgb(218, 222, 226);
}
.card-container {
  margin-left:25%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 40px;
  row-gap: 40px;
  border-width:1px;
  border-style: solid;
 
}
.card {
  height: 400px;
  display: grid;
  grid-row: 1fr 1fr;
  border: 1px solid rgba(28, 24, 25, 0.1);
  width: 250px; 
  background-color: aliceblue;
}
.card-view-icon {
  @include svgStyle($color: #002F34);
}
.card-favourite-icon {
  @include svgStyle($color: #002F34
  
  );
}
.card-img {
  width: 100%;
}
.whole-info-card {
  @include flex($direction: column, $justifyContent: space-between);
  height: 50%;
}
.time-view-icon-card {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 20px;
}
.publish-time-card,
.card-city,
.card-view-numbers,
.price-purchase,
.info-purchase {
  font-family: Open Sans, Arial, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: 300;
}
.card-view {
  @include flex();
  column-gap: 5px;
}
@media (max-width: 580px) {
  .card-container{
    display: none;
  }
}

</style>
