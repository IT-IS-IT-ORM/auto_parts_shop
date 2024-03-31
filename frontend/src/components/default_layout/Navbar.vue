<template>
  <header class="itisit-container navbar" :class="{ under80 }">
    <NuxtLink class="site-logo" to="/">
      <img src="~/assets/image/logo.png" alt="Auto Parts" />
      <h3>Auto-parts</h3>
    </NuxtLink>

    <ul class="actions">
      <Icon class="favorite-icon-btn" name="material-symbols:favorite-outline-rounded" role="button" @click.stop="handleNav('/profile?tab=favorite')
        " />

      <a class="profile" href="/profile?tab=settings" @click.prevent="handleNav('/profile?tab=settings')">
        <Icon name="material-symbols:person" />
        <span>Жекепарақша</span>
      </a>

      <Button variant="secondary" @click="handleNav('/product/add')">Объявление шығару</Button>
    </ul>

    <Icon class="burger-btn-open" :class="{ active: !mobileNavbarVisible }" name="quill:hamburger" role="button"
      @click="mobileNavbarVisible = true" />
    <Icon class="burger-btn-close" :class="{ active: mobileNavbarVisible }" name="mdi:close" role="button"
      @click="mobileNavbarVisible = false" />
  </header>

  <div class="mobile-navbar" :class="{ 'mobile-navbar--show': mobileNavbarVisible }">
    <ul class="menu">
      <li class="item" @click.stop="handleNav('/profile?tab=favorite')">
        <Icon name="material-symbols:favorite-outline-rounded" />
        <span>Таңдаулылар</span>
      </li>
      <li class="item" @click.stop="handleNav('/profile?tab=settings')">
        <Icon class="profile-icon" name="material-symbols:person" />
        <span>Жекепарақша</span>
      </li>
      <li class="item" @click.stop="handleNav('/product/add')">
        <Icon name="material-symbols:add-circle-outline-rounded" />
        <span>Объявление шығару</span>
      </li>
    </ul>
  </div>

  <div class="navbar-helper"></div>
</template>

<script setup lang="ts">
// Store
import { useUserStore } from '~/stores/user';
import { useModalStore } from '~/stores/modal';
// Componentns
import Button from '~/components/common/Button.vue';

const userStore = useUserStore();
const modalStore = useModalStore();
const router = useRouter();
import { useEventListener } from "vue-hooks-plus";

const mobileNavbarVisible = ref(false);

watch(mobileNavbarVisible, (visible) => {
  document.body.style.overflow = visible ? "hidden" : "hidden auto";
});

const under80 = ref(false);
let lastScroll = 0;

onMounted(() => {
  useEventListener("scroll", onWindowScroll);
});

function onWindowScroll() {
  const scroll = window.scrollY;
  if (scroll < lastScroll) {
    // User scrolled up
    under80.value = false;
  } else {
    under80.value = scroll > 80;
  }
  lastScroll = scroll;
}

const handleNav = (path: string) => {
  if (userStore.isAuthenticated) {
    router.push(path);
    return;
  }

  modalStore.loginReuiqredModal.open = true;
  modalStore.loginReuiqredModal.nextUrl = path;
  switch (path) {
    case '/profile?tab=settings':
      modalStore.loginReuiqredModal.actionDescription = 'Жекепарақшаға өту';
      break;
    case '/profile?tab=favorite':
      modalStore.loginReuiqredModal.actionDescription = 'Таңдауларді көру';
      break;
    case '/product/add':
      modalStore.loginReuiqredModal.actionDescription = 'Объявление шығару';
  }
};
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.navbar.under80 {
  transform: translateY(-80px);
}

.navbar {
  width: 100%;
  height: 74px;
  background-color: var(--c-primary);
  transition: 0.8s cubic-bezier(0.075, 0.82, 0.165, 1) transform;
  @include flex($alignItems: center);
  @include positioned($position: fixed, $top: 0, $left: 0, $zIndex: 90);

  .site-logo {
    margin-right: auto;
    @include flex($alignItems: center, $gap: 8px);

    img {
      width: 50px;
      height: 48px;
      object-fit: cover;
    }

    h3 {
      font-weight: 500;
      color: #fff;
    }
  }

  .actions {
    @include flex($alignItems: center, $gap: 32px);

    svg {
      @include svgStyle($color: #fff, $size: 28px);
    }

    .profile {
      color: #fff;
      @include flex($alignItems: center, $gap: 8px);
    }

    @media screen and (max-width: 880px) {
      gap: 24px;

      svg {
        @include svgStyle($color: #fff, $size: 24px);
      }

      .profile span {
        font-size: 18px;
      }

      :deep(.custom-button) {
        padding: 4px 10px;

        span {
          font-size: 18px;
        }
      }
    }

    @media screen and (max-width: 768px) {
      display: none;
    }
  }

  [class*="burger-btn"] {
    display: none;
    opacity: 0;
    transform: translateX(20px);
    pointer-events: none;
    transition: opacity var(--transition), transform var(--transition);
    @include svgStyle($color: #fff, $size: 40px);

    @media screen and (max-width: 768px) {
      display: block;
    }

    &.active {
      opacity: 1;
      transform: translateX(0);
      pointer-events: auto;
    }
  }

  .burger-btn-open {
    &.active {
      transform: translateX(40px);
    }
  }
}

.mobile-navbar {
  width: 100%;
  height: calc(100dvh - 74px);
  padding: 16px 0;
  border-top: 4px solid #fff;
  background-color: var(--c-primary);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition);
  @include positioned($position: fixed, $top: 74px, $left: 0, $zIndex: 90);

  &--show {
    opacity: 1;
    pointer-events: auto;
  }

  .menu {
    @include flex($direction: column);

    .item {
      width: 100%;
      padding: 16px;
      color: #fff;
      @include flex($alignItems: center, $gap: 8px);

      svg {
        @include svgStyle($color: #fff, $size: 28px);
      }
    }
  }
}

.navbar-helper {
  width: 100%;
  height: 74px;
}
</style>
