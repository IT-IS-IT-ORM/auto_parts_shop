<template>
    <a-button class="custom-button" :class="[`custom-button--${variant}`]">
        <slot></slot>
    </a-button>
</template>

<script setup lang="ts">
// Vue
import { PropType } from 'vue';

export type allowedButtonVariants = 'primary' | 'secondary';

const props = defineProps({
    variant: {
        type: String as PropType<allowedButtonVariants>,
        default: 'primary'
    }
});
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.custom-button {
    height: auto;
    padding: 4px 16px;
    border: 4px solid transparent;
    @include flexCenter;

    :deep(span) {
        font-weight: 500;
    }

    &--primary {
        color: #fff;
        border-color: var(--c-primary);
        background-color: var(--c-primary);

        &:hover {
            color: var(--c-primary);
            border-color: var(--c-primary);
            background-color: #fff;
        }
    }

    &--secondary {
        color: var(--c-primary);
        border-color: #fff;
        background-color: #fff;

        &:hover {
            color: #fff;
            border-color: #fff;
            background-color: var(--c-primary);
        }
    }
}
</style>