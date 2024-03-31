<template>
    <main class="login-page">
        <AuthTemplate without-logo title="Кіру">
            <a-form :model="loginForm" layout="vertical" autocomplete="off" @finish="onFinish">
                <a-form-item label="Телефон" name="phone"
                    :rules="[{ required: true, message: 'Телефон нөмерді енгізіңіз!' }]">
                    <a-input v-model:value="loginForm.phone" type="tel" placeholder="87771234567" maxLength="11" />
                </a-form-item>

                <a-form-item label="Құпиясөз" name="password"
                    :rules="[{ required: true, message: 'Құпиясөзді енгізіңіз!' }]">
                    <a-input-password v-model:value="loginForm.password" maxLength="254" />
                </a-form-item>

                <a-form-item>
                    <a-button :loading="loading" type="primary" html-type="submit">Кіру</a-button>
                </a-form-item>
            </a-form>
        </AuthTemplate>
    </main>
</template>

<script setup lang="ts">
// Vue
import { ref } from 'vue';
// Vue Router
import { useRouter } from 'vue-router';
// Store
import { useUserStore } from '~/stores/user';
// API
import { API_Login } from '~/service/api/user-api';
// Hooks
import useRequest from 'vue-hooks-plus/es/useRequest';
// Antd Component
import { message as AntdMessage } from 'ant-design-vue';
// Component
import AuthTemplate from '~/components/common/AuthTemplate.vue';

const userStore = useUserStore();
const router = useRouter();

const loginForm = ref({
    phone: '',
    password: '',
});

const { runAsync, loading } = useRequest(API_Login, { manual: true });

const onFinish = (values: any) => {
    runAsync(values).then(({ data }) => {
        localStorage.set('user', data);
        userStore.$state = data;
        AntdMessage.success('Қош келдіңіз!');
        router.replace('/profile');
    }).catch(error => {
        AntdMessage.error(error.message);
    })
};
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.login-page {
    @include flexCenter;

    .auth-template {
        width: 365px;
        padding: 24px;
        border-radius: var(--border-radius);
        box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;

        @media screen and (max-width: 576px) {
            padding: 16px;
            box-shadow: none;
        }
    }
}
</style>