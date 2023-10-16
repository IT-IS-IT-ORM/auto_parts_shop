<template>
    <div class="modal">
     
      <a-modal v-model:open="settings.showModal" title="Basic Modal" @ok="handleOk">
        <p>to do this ,you have to log in</p>
       
      </a-modal>
    </div>
  </template>
  <script lang="ts" setup>
  const props = defineProps<{settings: {showModal: boolean}, closeModal: any}>();

  const handleOk = (e: MouseEvent) => {
    props.closeModal();
  };

  </script>
  
  