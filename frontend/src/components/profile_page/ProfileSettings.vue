<template>
    <div class="profile-settings">
        <AuthTemplate without-logo without-else>
            <div class="block">
                <p class="head">Негізгі ақпарат</p>

                <a-form :model="basicInfoForm" layout="vertical" autocomplete="off" @finish="handleChangeInfo">
                    <a-form-item label="Аты-жөн" name="fullname"
                        :rules="[{ required: true, message: 'Аты-жөн нөмерді енгізіңіз!' }]">
                        <a-input v-model:value="basicInfoForm.fullname" maxLength="30" />
                    </a-form-item>

                    <a-form-item label="Телефон" name="phone"
                        :rules="[{ required: true, message: 'Телефон нөмерді енгізіңіз!' }]">
                        <a-input v-model:value="basicInfoForm.phone" type="tel" placeholder="87771234567" maxLength="11" />
                    </a-form-item>

                    <a-form-item>
                        <Button block html-type="submit" :loading="updateInfoLoading">Сақтау</Button>
                    </a-form-item>
                </a-form>
            </div>

            <div class="block">
                <p class="head">Құпиясөз өзгерту</p>

                <a-form :model="changePasswordForm" layout="vertical" autocomplete="off" @finish="handleChangePassword">
                    <a-form-item label="Ескі құпиясөз" name="password"
                        :rules="[{ required: true, message: 'Құпиясөзді енгізіңіз!' }]">
                        <a-input-password v-model:value="changePasswordForm.password" maxLength="254" />
                    </a-form-item>

                    <a-form-item label="Жаңа құпиясөз" name="newPassword"
                        :rules="[{ required: true, message: 'Құпиясөзді енгізіңіз!' }]">
                        <a-input-password v-model:value="changePasswordForm.newPassword" maxLength="254" />
                    </a-form-item>

                    <a-form-item>
                        <Button block html-type="submit" :loading="changePasswordLoading">Сақтау</Button>
                    </a-form-item>
                </a-form>
            </div>

            <a-button block danger type="primary" class="logout-btn" @click="handleLogout">
                Шығу
                <Icon name="octicon:sign-out" />
            </a-button>
        </AuthTemplate>
    </div>
</template>

<script setup lang="ts">
// Vue
import { ref } from 'vue';
// Vue Router
import { useRouter } from 'vue-router';
// Store
import { useUser } from '~/stores/user';
// API
import { API_UpdateInfo, API_ChangePassword } from '~/service/api/user-api';
// Utils
import { defaultUserState } from '~/stores/user';
// Hooks
import useRequest from 'vue-hooks-plus/es/useRequest';
// Antd Component
import { message as AntdMessage } from 'ant-design-vue';
// Component
import AuthTemplate from '~/components/common/AuthTemplate.vue';
import Button from '~/components/common/Button.vue';

const user = useUser();
const router = useRouter();

const basicInfoForm = ref({
    fullname: user.fullname,
    phone: user.phone,
});

const changePasswordForm = ref({
    password: '',
    newPassword: '',
})

const { runAsync: updateInfo, loading: updateInfoLoading } = useRequest(API_UpdateInfo, { manual: true });
const { runAsync: changePassword, loading: changePasswordLoading } = useRequest(API_ChangePassword, { manual: true });

const handleChangeInfo = (values: any) => {
    updateInfo(user.id, values).then(({ data }) => {
        localStorage.set('user', data);
        user.$state = data;
        AntdMessage.success('Өзгеріс сақталды!');
    }).catch(error => {
        AntdMessage.error(error.message);
    })
}

const handleChangePassword = (values: any) => {
    changePassword(values).then(() => {
        AntdMessage.success('Өзгеріс сақталды!');
    }).catch(error => {
        AntdMessage.error(error.message);
    })
}

const handleLogout = () => {
    localStorage.set('user', defaultUserState);
    user.$state = defaultUserState;
    router.replace('/auth/login');
}
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.profile-settings {
    :deep(.auth-template) {
        width: 100%;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 24px;

        .block {
            flex: 0 1 320px;
        }
    }
}

.block {
    max-width: 100%;
    padding: 8px 16px 16px;
    border-radius: var(--border-radius);
    border: 1px solid var(--c-border);

    .head {
        margin-bottom: 8px;
    }
}

.logout-btn {
    height: 50px;
    @include flexCenter($gap: 8px);

    svg {
        @include svgStyle($color: #fff);
    }
}
</style>