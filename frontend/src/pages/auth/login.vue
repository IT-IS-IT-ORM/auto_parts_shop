<template>
    <main class="login-page">
        <AuthTemplate title="Кіру">
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
import { useUser } from '~/stores/user';
// API
import { API_Login } from '~/service/api/user-api';
// Hooks
import useRequest from 'vue-hooks-plus/es/useRequest';
// Antd Component
import { message as AntdMessage } from 'ant-design-vue';
// Component
import AuthTemplate from '~/components/common/AuthTemplate.vue';

const user = useUser();
const router = useRouter();

const loginForm = ref({
    phone: '',
    password: '',
});

const { runAsync, loading } = useRequest(API_Login, { manual: true });

const onFinish = (values: any) => {
    runAsync(values).then(({ data }) => {
        localStorage.set('user', data);
        user.$state = data;
        AntdMessage.success('Қош келдіңіз!');
        router.replace('/profile');
    }).catch(error => {
        AntdMessage.error(error.message);
    })
};
</script>