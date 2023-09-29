<template>
    <main class="auth-template">
        <img v-if="!withoutLogo" class="logo" src="~/assets/image/logo.png" alt="Logo" />
        <h3 v-if="title" class="title">{{ title }}</h3>
        <slot></slot>

        <div v-if="!withoutElse" class="else">
            <span>немесе</span>
            <NuxtLink :to="_else.to">
                {{ _else.text }}
            </NuxtLink>
        </div>
    </main>
</template>

<script setup lang="ts">
// Vue
import { toRefs } from 'vue';

const props = defineProps({
    title: {
        type: String,
        default: '',
    },
    withoutLogo: {
        type: Boolean,
        default: false
    },
    withoutElse: {
        type: Boolean,
        default: false
    }
});
const { title, withoutElse, withoutLogo } = toRefs(props);

const _else = computed(() => {
    if (title.value === 'Кіру') {
        return {
            to: '/auth/register',
            text: 'Тіркелу'
        }
    }

    return {
        to: '/auth/login',
        text: 'Кіру'
    }
})
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.auth-template {
    width: 300px;
    max-width: 100%;
    @include flex($direction: column, $alignItems: center);

    .logo {
        width: 128px;
        height: 102px;
        margin-bottom: 24px;
    }

    .title {
        font-size: 32px;
        margin-bottom: 24px;
    }

    :deep(.ant-form) {
        .ant-form-item-control-input-content {

            &,
            &>* {
                width: 100%;
                height: 40px;

                input {
                    @include useFont;
                }
            }

            &.ant-btn,
            &>.ant-btn {
                height: 50px;
            }

            &>.ant-btn {
                margin-top: 16px;
            }

            .ant-input-prefix {
                margin-inline-end: 8px;
            }
        }

        /* 错误信息 */
        .ant-form-item-explain-error {
            @include useFont($size: 14px, $color: var(--c-error));
        }
    }

    .else {
        margin-top: 16px;
        @include flex($direction: column, $alignItems: center, $gap: 12px);

        a {
            text-decoration: none;
            @include useFont($color: var(--c-primary));
        }
    }
}
</style>