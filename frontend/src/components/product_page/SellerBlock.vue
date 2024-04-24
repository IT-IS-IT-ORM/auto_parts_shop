<template>
    <div class="buy-block">
        <p class="title">Сатушы</p>

        <div class="row">
            <UserAvatar class="avatar" />

            <div class="info">
                <span class="phone">{{ product.seller.phone }}</span>
                <span class="fullname">{{ product.seller.fullname }}</span>
                <span class="create-time">Auto-parts-де {{ totalRegisterDate }} күн тіркелген</span>
            </div>
        </div>

        <Button v-if="userStore.role === role.consumer" block 
            @click="$router.push(`/?seller=${product.seller.id}`)">
            Сатушының барлық заты
        </Button>
    </div>
</template>

<script setup lang="ts">
// Types
import type { I_Product } from '~/types/product';

// Store
import { useUserStore } from "~/stores/user";
// Utils
import { role } from "~/utils/role";
// Components
import Button from '~/components/common/Button.vue';
import UserAvatar from '~/assets/image/UserAvatar.vue';

const props = defineProps<{
    product: I_Product
}>();

const userStore = useUserStore();

const totalRegisterDate = computed(() => {
    const today = new Date(Date.now());
    const sellerRegisterDate = new Date(props.product.seller.createTime);
    // @ts-ignore
    const difference = Math.floor((today - sellerRegisterDate) / (1000 * 3600 * 24));
    return difference;
})
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.buy-block {
    padding: 24px;
    border-radius: var(--border-radius);
    background-color: #fff;
    @include flex($direction: column);

    @media screen and (max-width: 576px) {
        padding: 16px;
    }

    .title {
        font-weight: 500;
        margin-bottom: 16px;
    }

    .row {
        margin-bottom: 16px;
        @include flex($justifyContent: space-between, $gap: 16px);

        .avatar {
            @include svgStyle($size: 48px);
        }

        .info {
            @include flex($direction: column, $gap: 4px);

            .phone {
                font-weight: 500;
            }

            .fullname,
            .create-time {
                font-weight: 300;
                font-size: 14px;
                color: var(--c-text-secondary);
            }
        }
    }

    .custom-button {
        margin-top: auto;
    }
}
</style>