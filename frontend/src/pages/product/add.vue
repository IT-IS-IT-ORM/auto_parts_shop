<template>
    <main class="itisit-container product-add-page">
        <AddProductForm />
    </main>
</template>

<script setup lang="ts">
// Vue
import { defineOptions } from 'vue';
// Components
import AddProductForm from '~/components/product/AddProductForm.vue';

defineOptions({ name: 'ProductAddPage' });
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.product-add-page {
    padding-top: 60px;
    padding-bottom: 80px;
    @include flex($direction: column, $gap: 40px);

    @media screen and (max-width: 576px) {
        padding-top: 40px;
        padding-bottom: 60px;
        gap: 24px;
    }

    @media screen and (max-width: 404px) {
        padding-top: 24px;
        padding-bottom: 40px;
        gap: 20px;
    }

}
</style>