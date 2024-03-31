<template>
  <a-modal v-model:open="modalStore.loginReuiqredModal.open" title="Авторизация керек" ok-text="Авторизация"
    cancel-text="Болдырмау" @ok="handleOk">
    <p>{{ `${modalStore.loginReuiqredModal.actionDescription} үшін авторизациядан өтіңіз` }}</p>
  </a-modal>
</template>

<script setup lang="ts">
// Vue Router
import { useRouter } from 'vue-router';
// Store
import { useModalStore } from '~/stores/modal';

const modalStore = useModalStore();
const router = useRouter();

const handleOk = () => {
  router.push(`/auth/login?nextUrl=${modalStore.loginReuiqredModal.nextUrl}`);
  modalStore.loginReuiqredModal.open = false;
  modalStore.loginReuiqredModal.nextUrl = '/';
  modalStore.loginReuiqredModal.actionDescription = '';
}
</script>

