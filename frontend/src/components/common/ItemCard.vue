<template>
  <div class="card">
    <div class="card-container">

    </div>
    <div class="card-image">
      <img class="card-img" src="~/assets/image/logo.png" alt="" />
    </div>
    <div class="whole-info-card">
      <div class="price-purchase">{{ props.itemData.price }} ₸</div>
      <div class="type-purchase"><a href="#">{{ props.itemData.name }}</a></div>
      <div class="info-purchase">2020 г., 2.5 л, бензин, КПП автомат</div>
      <div class="card-city">{{ props.itemData.city }}</div>
      <div class="time-view-icon-card">
        <span class="publish-time-card">1 окт.</span>
        <div class="card-view">
          <Icon class="card-view-icon" name="ic:round-remove-red-eye"></Icon>
          <div class="card-view-numbers">3000</div>
        </div>
        <div class="card-favourite-icon-div">
          <Icon class="card-favourite-icon" name="solar:folder-favourite-star-outline"></Icon>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


const props = defineProps<{
  itemData: any
}>();
console.log(props.itemData);
</script>


