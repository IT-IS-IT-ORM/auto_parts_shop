<template>
  <div class="default-layout">
    <div class="itisit-container header">
      <div class="site-logo">
        <img class="header-logo-img" src="~/assets/image/logo.png" alt="" />
        <h3>Auto-parts</h3>
      </div>

      <div class="profile-addPurchase">
        <Icon
          class="heart-icon"
          name="material-symbols:favorite-outline-rounded"
        />

        <NuxtLink class="profile-icon-div" to="">
          <Icon
            class="profile-icon"
            name="material-symbols:person-outline-rounded"
          />
          <span class="myprofile">жекепарақша</span>
        </NuxtLink>

        <a-button class="add-purchase">объявление тапсыру</a-button>
      </div>
    </div>
    <!--电脑版的header结束，下面是手机版的header-->

    <div class="itisit-container mobile-header">
      <div class="logo-mobile">
        <img class="header-logo-mobile" src="~/assets/image/logo.png" alt="" />
        <h3>Auto-parts</h3>
      </div>
      <div class="mobile-hamburger-icon-div" @click="mobileMenuVisible=!mobileMenuVisible">
        <Icon class="mobile-hamburger-icon" name="quill:hamburger" />
      </div>
    </div>

    <div class="itisit-container mobile-menu" :class="{
      'active':mobileMenuVisible
    }">
      <div class="navbar-links">
        <div>
          <a href="#"
            ><Icon
              class="heart-icon"
              name="material-symbols:favorite-outline-rounded"
            />favourite</a
          >
        </div>
        <div>
          <a href="#">
            <Icon
              class="profile-icon"
              name="material-symbols:person-outline-rounded"
            />my profile</a
          >
        </div>

        <div>
          <a href="#"><Icon name="icon-park-outline:buy" />add purchase</a>
        </div>
      </div>
    </div>

    <slot></slot>

    <footer class="footer">
      <div class="site-logo2">
        <img src="~/assets/image/logo.png" alt="" />
      </div>
      <span class="footer-text">
        Крупнейший онлайн-сервис объявлений Казахстана
        <br />

        Все онлайн-объявления Казахстана на OLX - здесь вы найдете то, что
        искали! Нажав на кнопку "Подать объявление", вы сможете разместить
        объявление на любую тематику легко и быстро.
        <br />

        С помощью сервиса OLX вы сможете купить или продать из рук в руки
        практически все, что угодно.
      </span>
    </footer>
  </div>
</template>

<script setup lang="ts">
const mobileMenuVisible = ref(false);

</script>
<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.default-layout {
  position: relative;
  background: var(--c-background);

  .header {
    width: 100%;
    height: 74px;
    background-color: #002f34;
    @include flex($justifyContent: space-between, $alignItems: center);
    @include positioned($position: fixed);

    .site-logo {
      @include flex($alignItems: center, $gap: 10px);
    }
    .site-logo > h3 {
      color: #fff;
      font-weight: 500;
    }

    .header-logo-img {
      width: 56px;
      height: 56px;
      object-fit: cover;
    }
    .profile-addPurchase {
      @include flex($alignItems: center, $gap: 20px);
    }
    .add-purchase {
      height: 46px;
      font-weight: 400;
      color: #002f34;
      transition: background-color var(--transition);
      border: 4px solid #fff;
    }
    .add-purchase:hover {
      color: #ffffff;
      background-color: #002f34;
    }

    .profile-icon {
      @include svgStyle($color: #fff, $size: 32px);
      margin-right: 15px;
    }
    .profile-icon-div {
      @include flex($alignItems: center);
    }
    .myprofile {
      color: #ffffff;
    }
    .heart-icon {
      @include svgStyle($color: #fff, $size: 32px);
    }
    .menu-div {
      @include flex($alignItems: center);
    }
  }
  .footer {
    @include flexCenter($direction: column);
    width: 100%;
    height: 420px;
    background-color: #cbf7ee;
  }
  .footer-text {
    margin-top: 30px;
    width: 70%;
    color: #002f34;
    font-weight: 300;
    font-size: 14px;
    text-align: center;
    max-width: 820px;
  }
  @media (min-width: 580px) {
    .mobile-header,.mobile-menu {
      display: none;
    }
  }
  /*手机版-css-header*/
  @media (max-width: 580px) {
    .header,
    .footer {
      display: none;
    }
    .mobile-header {
      background-color: #002f34;
      @include flexCenter();
      height: 48px;
      @include positioned($position: fixed, $top: 0);
      width: 100%;
    }
    .mobile-menu {
      @include positioned($position: fixed);
      width: 100%;
      height: calc(100dvh - 48px);
      transform: translateY(48px);
      height: 100%;
      display: none;
      background-color: #002f34;
      padding-top: 24px;

      .navbar-links {
        width: 100%;
        background-color: #002f34;
        height: 128px;
        @include flex($direction: column, $gap: 24px);
      }

      &.active {
        display: flex;
      }
      .navbar-links div {
        width: 100%;
      }
      .navbar-links a {
        @include flex();
        text-decoration: none;
        color: #fff;
        column-gap: 8px;
      }
    }

    .mobile-hamburger-icon {
      color: #cbf7ee;
    }
    .mobile-hamburger-icon-div {
      display: flex;
      justify-content: flex-end;
      width: 50%;
    }
    .logo-mobile {
      width: 50%;
      height: 36px;
      @include flex($justifyContent: space-between, $alignItems: center);
    }
    .header-logo-mobile {
      height: 32px;
      width: 32px;
    }
    .logo-mobile > h3 {
      color: #fff;
    }
  }
}
</style>
