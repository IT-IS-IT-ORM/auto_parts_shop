<template>
  <div class="card-container">
    <div class="card">
      <div class="card-image">
        <img class="card-img" src="~/assets/image/logo.png" alt="" />
      </div>
      <div class="whole-info-card">
        <div class="price-purchase">
          <p>{{ props.itemData.price }} ₸</p>
        </div>
        <div class="type-purchase">
          <a href="#">{{ props.itemData.name }}</a>
        </div>
        <div class="info-purchase">
          <p>2020 г., 2.5 л, бензин, КПП автомат</p>
        </div>
        <div class="card-city">{{ props.itemData.city }}</div>
        <div class="time-view-icon-card">
          <span class="publish-time-card">1 окт.</span>
          <div class="card-view">
            <div class="card-view-icon-div">
              <Icon
                class="card-view-icon"
                name="ic:round-remove-red-eye"
              ></Icon>
            </div>
            <div class="card-view-numbers">3000</div>
          </div>
          <div class="card-favourite-icon-div">
            <Icon
              class="card-favourite-icon"
              name="solar:folder-favourite-star-outline"
            ></Icon>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  itemData: any;
}>();
console.log(props.itemData);
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.home-page {
  @include flex($direction: column, $gap: 40px);
  @media screen and (max-width: 576px) {
    gap: 24px;
  }
  background-color: rgb(218, 222, 226);
}
.card-container {
  margin-left: 10%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 40px;
  row-gap: 40px;
}
.type-purchase {
  margin-bottom: 12px;
}
.type-purchase a {
  color: #2a8be6;
}
.card {
  display: grid;
  grid-row: 1fr 1fr;

  width: 250px;
  background-color: #fff;
  border: 1px solid rgba(180, 180, 180, 0.692);
}
.card-view-icon {
  @include svgStyle($color: #002f34);
  width: 16px;

  padding-bottom: 10px;
}
.card-favourite-icon {
  @include svgStyle($color: #002f34);
  margin-right: 12px;
  width: 18px;
  padding-bottom: 8px;
}

.card-favourite-icon-div {
  display: flex;
  justify-content: end;
  flex: 1;
  margin-right: 10px;
}
.card-image {
  width: 100%;
}
.card-img {
  width: 100%;
  height: 100%;
}
.whole-info-card {
  @include flex($direction: column);
  height: 50%;
  padding-left: 12px;
  padding-bottom: 5px;
}
.time-view-icon-card {
  display: flex;
  width: 100%;
  column-gap: 10px;
}

.price-purchase {
  font-family: Open Sans, Arial, Helvetica, sans-serif;
  margin-bottom: 18px;
}
.card-city {
  margin-bottom: 12px;
}
.info-purchase {
  margin-bottom: 12px;
}
.publish-time-card,
.card-city,
.card-view-numbers {
  color: #888b94;
  font-size: 12px;
  font-weight: 500;
}
.publish-time-card {
  margin-right: 14px;
}
.info-purchase p {
  font-size: 16px;
  line-height: 20px;

  word-break: break-word;
}
.price-purchase p {
  font-size: 18px;
  font-weight: 600;
  line-height: 24px;
  margin-left: 12px;
}
.card-view {
  @include flex();
  column-gap: 6px;
  flex: 1;
}
@media (max-width: 580px) {
  .card-container {
    display: none;
  }
}
</style>
