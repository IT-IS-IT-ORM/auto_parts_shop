<template>
    <main class="register-page">
        <AuthTemplate without-logo title="Тіркелу">
            <a-form :model="registerForm" layout="vertical" autocomplete="off" @finish="onFinish">
                <a-form-item label="Рол" name="role" :rules="[{ required: true, message: 'Рол таңдаңыз!' }]">
                    <a-radio-group v-model:value="registerForm.role">
                        <a-radio :value="role.consumer">Тұтынушы</a-radio>
                        <a-radio :value="role.provider">Сатушы</a-radio>
                    </a-radio-group>
                </a-form-item>

                <a-form-item label="Аты-жөн" name="fullname"
                    :rules="[{ required: true, message: 'Аты-жөн нөмерді енгізіңіз!' }]">
                    <a-input v-model:value="registerForm.fullname" maxLength="30" />
                </a-form-item>

                <a-form-item label="Телефон" name="phone"
                    :rules="[{ required: true, message: 'Телефон нөмерді енгізіңіз!' }]">
                    <a-input v-model:value="registerForm.phone" type="tel" placeholder="87771234567" maxLength="11" />
                </a-form-item>

                <a-form-item label="Құпиясөз" name="password"
                    :rules="[{ required: true, message: 'Құпиясөзді енгізіңіз!' }]">
                    <a-input-password v-model:value="registerForm.password" maxLength="254" />
                </a-form-item>

                <a-form-item>
                    <a-button :loading="loading" type="primary" html-type="submit">Тіркелу</a-button>
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
import { API_Register } from '~/service/api/user-api';
// Hooks
import useRequest from 'vue-hooks-plus/es/useRequest';
// Antd Component
import { message as AntdMessage } from 'ant-design-vue';
// Component
import AuthTemplate from '~/components/common/AuthTemplate.vue';

const user = useUser();
const router = useRouter();

const registerForm = ref({
    role: role.consumer,
    fullname: '',
    phone: '',
    password: '',
});

const { runAsync, loading } = useRequest(API_Register, { manual: true });

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

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.register-page {
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