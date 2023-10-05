<template>
    <header class="itisit-container navbar">
        <NuxtLink class="site-logo" to="/">
            <img src="~/assets/image/logo.png" alt="Auto Parts" />
            <h3>Auto-parts</h3>
        </NuxtLink>

        <ul class="actions">
            <Icon class="favorite-icon-btn" name="material-symbols:favorite-outline-rounded" role="button" />

            <NuxtLink class="profile" to="/profile">
                <Icon name="material-symbols:person" />
                <span>Жекепарақша</span>
            </NuxtLink>

            <a-button>Объявление шығару</a-button>
        </ul>

        <Icon class="burger-btn-open" :class="{ 'active': !mobileNavbarVisible }" name="quill:hamburger" role="button"
            @click="mobileNavbarVisible = true" />
        <Icon class="burger-btn-close" :class="{ 'active': mobileNavbarVisible }" name="mdi:close" role="button"
            @click="mobileNavbarVisible = false" />
    </header>

    <div class="mobile-navbar" :class="{ 'mobile-navbar--show': mobileNavbarVisible }">
        <ul class="menu">
            <li class="item">
                <Icon name="material-symbols:favorite-outline-rounded" />
                <span>Таңдаулылар</span>
            </li>
            <li class="item">
                <Icon class="profile-icon" name="material-symbols:person" />
                <span>Жекепарақша</span>
            </li>
            <li class="item">
                <Icon name="material-symbols:add-circle-outline-rounded" />
                <span>Объявление шығару</span>
            </li>
        </ul>
    </div>

    <div class="navbar-helper"></div>
</template>

<script setup lang="ts">
const mobileNavbarVisible = ref(false);

watch(mobileNavbarVisible, visible => {
    document.body.style.overflow = visible ? 'hidden' : 'hidden auto';
})
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.navbar {
    width: 100%;
    height: 74px;
    background-color: var(--c-primary);
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

        @media screen and (max-width: 768px) {
            display: none;
        }

        svg {
            @include svgStyle($color: #fff, $size: 28px);
        }

        .profile {
            color: #fff;
            @include flex($alignItems: center, $gap: 8px);
        }

        :deep(.ant-btn) {
            height: auto;
            padding: 4px 16px;
            border: 4px solid #fff;
            @include flexCenter;

            span {
                font-weight: 500;
            }

            &:hover {
                color: #fff;
                background-color: var(--c-primary);
            }
        }
    }

    [class*='burger-btn'] {
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