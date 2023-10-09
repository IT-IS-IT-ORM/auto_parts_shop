<template>
    <main class="itisit-container profile-page">
        <h3 class="title">Жеке кабинет</h3>

        <a-tabs v-model:activeKey="tab" :onChange="handleChangeTab">
            <a-tab-pane key="settings" :disabled="!user.isAuthenticated">
                <template #tab>
                    <span>
                        <Icon name="material-symbols:settings-outline-rounded" />
                        Ақпарат
                    </span>
                </template>
                <ProfileSettings />
            </a-tab-pane>
            <a-tab-pane key="product">
                <template #tab>
                    <span>
                        <Icon name="icon-park-outline:ad-product" />
                        Объявление
                    </span>
                </template>
                <ProfileMyProduct />
            </a-tab-pane>
            <a-tab-pane key="order">
                <template #tab>
                    <span>
                        <Icon name="carbon:cics-transaction-server-zos" />
                        Заказ
                    </span>
                </template>
                <ProfileMyOrder />
            </a-tab-pane>
            <a-tab-pane key="favorite">
                <template #tab>
                    <span>
                        <Icon name="material-symbols:favorite-outline-rounded" />
                        Таңдаулылар
                    </span>
                </template>
                <ProfileMyFavorite />
            </a-tab-pane>
        </a-tabs>
    </main>
</template>
  
<script setup lang="ts">
// Router
import { useRoute, useRouter } from 'vue-router';
// Store
import { useUser } from '~/stores/user';
// Component
import ProfileSettings from '~/components/profile_page/ProfileSettings.vue'
import ProfileMyOrder from '~/components/profile_page/ProfileMyOrder.vue'
import ProfileMyFavorite from '~/components/profile_page/ProfileMyFavorite.vue'
import ProfileMyProduct from '~/components/profile_page/ProfileMyProduct.vue'

const user = useUser();
const route = useRoute();
const router = useRouter();

const tab = ref<string>(route.query.tab as string ?? 'settings');

watch(() => route.query.tab, () => {
    const quertTab = route.query.tab as string
    if (['settings', 'favorite'].includes(quertTab)) {
        tab.value = quertTab;
    }
})

const handleChangeTab = (activeKey: 'settings' | 'favorite') => {
    router.push({
        query: {
            ...route.query,
            tab: activeKey
        }
    });
}
</script>
  
<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.profile-page {
    --c-border: var(--c-primary);
    padding-top: 40px;
    padding-bottom: 24px;
    @include flex($direction: column);

    .title {
        font-size: 36px;
        margin-bottom: 32px;

        @media screen and (max-width: 576px) {
            font-size: 24px;
            margin-bottom: 12px;
        }
    }

    :deep(.ant-tabs) {
        width: 100%;

        .ant-tabs-tab-btn span {
            @include flex($alignItems: center, $gap: 8px);

            @media screen and (max-width: 576px) {
                font-size: 12px;
            }
        }
    }
}
</style>