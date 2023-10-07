<template>
    <footer class="footer">
        <h3 class="site-logo">
            <img src="~/assets/image/logo.png" alt="Auto Parts" />
            <span>Auto-parts</span>
        </h3>

        <p class="footer-text">
            Крупнейший онлайн-сервис объявлений Казахстана
            <br />
            Все онлайн-объявления Казахстана на OLX - здесь вы найдете то, что
            искали! Нажав на кнопку "Подать объявление", вы сможете разместить
            объявление на любую тематику легко и быстро.
            <br />
            С помощью сервиса OLX вы сможете купить или продать из рук в руки
            практически все, что угодно.
        </p>

        <div class="social-media">

        </div>
    </footer>
</template>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.footer {
    width: 100%;
    padding: 50px 0 64px;
    background-color: var(--c-primary);
    @include flexCenter($direction: column);

    .site-logo {
        margin-bottom: 32px;
        @include flex($direction: column, $alignItems: center, $gap: 4px);

        img {
            width: 70px;
            height: 68px;
            object-fit: cover;
        }

        span {
            font-weight: 500;
            color: #fff;
        }
    }

    .footer-text {
        width: 70%;
        max-width: 820px;
        font-weight: 300;
        font-size: 14px;
        line-height: 20px;
        color: #fff;
        text-align: center;
    }
}
</style>