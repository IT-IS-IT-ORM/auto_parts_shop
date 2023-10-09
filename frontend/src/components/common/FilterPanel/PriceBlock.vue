<template>
    <div class="block">
        <div class="row">
            <div class="field" @click="form.hasPhoto = !form.hasPhoto">
                <a-checkbox v-model:checked="form.hasPhoto" />
                Сурет
            </div>
            <div class="field" @click="form.isNew = !form.isNew">
                <a-checkbox v-model:checked="form.isNew" />
                Жаңа
            </div>
        </div>

        <div class="field">
            Баға аралық
            <div class="inputs">
                <a-input-number v-model="form.minPrice" :controls="false"
                    :formatter="(value: string) => `₸ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
                    :parser="(value: string) => value.replace(/\$\s?|(,*)/g, '')" />
                <span class="spliter"></span>
                <a-input-number v-model="form.maxPrice" :controls="false"
                    :formatter="(value: string) => `₸ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
                    :parser="(value: string) => value.replace(/\$\s?|(,*)/g, '')" />
            </div>
        </div>

        <Button>17 объявление көрсету</Button>
    </div>
</template>

<script setup lang="ts">
// Components
import Button from '~/components/common/Button.vue';

const form = ref({
    hasPhoto: false,
    isNew: false,
    minPrice: null as number | null,
    maxPrice: null as number | null,
})

const $emit = defineEmits<{ (event: 'change', value: typeof form.value): void }>();

watch(form, (val) => $emit('change', val));
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.block {
    padding: 16px 24px;
    border-radius: var(--border-radius);
    border: 1px solid var(--c-border);
    background-color: #fff;



    .row {
        @include flex($justifyContent: space-between, $alignItems: center, $gap: 24px);

        .field {
            cursor: pointer;
            @include flex($alignItems: center, $gap: 8px);
        }
    }

    &>.field {
        @include flex($direction: column, $gap: 10px);

        .inputs {
            @include flex($alignItems: center, $gap: 8px);

            .spliter {
                width: 8px;
                height: 2px;
                background-color: var(--c-text-secondary);
            }

            input {
                &::first-letter {
                    font-size: 12px;
                }
            }
        }
    }

    :deep(.ant-checkbox-inner) {
        width: 24px;
        height: 24px;

        &::after {
            width: 8px;
            height: 14px;
            top: 45%;
            left: 24%;
        }
    }

    :deep(.ant-input-number) {
        width: 145px;
    }

    @media screen and (max-width: 768px) {
        padding: 16px;

        .inputs {
            .ant-input-number {
                width: auto;
                flex: 1 1 auto;
            }

            .spliter {
                flex: 0 0 8px;
            }
        }

        .custom-button {
            width: 100%;
        }
    }
}
</style>