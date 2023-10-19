<template>
  <a-modal v-model:open="modal.loginReuiqredModal.open" title="Авторизация керек" ok-text="Авторизация"
    cancel-text="Болдырмау" @ok="handleOk">
    <p>{{ `${modal.loginReuiqredModal.actionDescription} үшін авторизациядан өтіңіз` }}</p>
  </a-modal>
</template>

<script setup lang="ts">
// Vue Router
import { useRouter } from 'vue-router';
// Store
import { useModal } from '~/stores/modal';

const modal = useModal();
const router = useRouter();

const handleOk = () => {
  router.push(`/auth/login?nextUrl=${modal.loginReuiqredModal.nextUrl}`);
  modal.loginReuiqredModal.open = false;
  modal.loginReuiqredModal.nextUrl = '/';
  modal.loginReuiqredModal.actionDescription = '';
}
</script>

