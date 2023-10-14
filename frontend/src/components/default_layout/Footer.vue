<template>
    <footer class="footer">
        <h3 class="site-logo">
            <img src="~/assets/image/logo.png" alt="Auto Parts" />
            <span>Auto-parts</span>
        </h3>

        <p class="footer-text">
            Қазақстандағы ең ірі автокөлік бөлшектерін сату алаңы
            <br />
            Қазақстандағы барлық автокөлік бөлшектері Auto-parts сайтында - мұнда бәрін таба аласыз!
            «Жариялау» батырмасын басу арқылы сіз жариялай аласыз
            кез келген көлікке арналған бөлшектер тез және оңай.
            <br />
            Auto-parts қызметін пайдалана отырып, қолдан қолға сатып алуға немесе сатуға болады
            барлығы дерлік.
        </p>

        <div class="social-media">
            <p>Auto-parts әлеуметтік желілердегі қауымдастықтары:</p>

            <ul class="list">
                <li class="item">
                    <a href="#">
                        <Icon name="fa6-brands:square-facebook" />
                    </a>
                </li>
                <li class="item">
                    <a href="#">
                        <Icon name="bi:instagram" />
                    </a>
                </li>
                <li class="item">
                    <a href="#">
                        <Icon name="fa6-brands:youtube" />
                    </a>
                </li>
            </ul>
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

    .social-media {
        margin-top: 40px;
        @include flex($direction: column, $alignItems: center, $gap: 12px);

        p {
            max-width: 820px;
            font-weight: 300;
            font-size: 14px;
            line-height: 20px;
            color: #fff;
            text-align: center;
        }

        .list {
            list-style: none;
            @include flex($gap: 24px);

            svg {
                @include svgStyle($color: #fff);
            }
        }
    }
}
</style>