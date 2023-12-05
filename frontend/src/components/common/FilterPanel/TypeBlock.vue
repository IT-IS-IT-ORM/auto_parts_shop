<template>
    <div class="block">
        <span class="title">Тип</span>

        <ul class="type-list">
            <li v-for="_type in typeList" :key="_type.key" class="item" :class="{ 'item--active': _type.isActive }"
                @click="handleItemClick(_type.key as I_Product['type'])">
                <div class="type-photo">
                    <img :src="dynamicAsset.image(`product/filter_type_${_type.key}.png`)" />
                </div>
                <span>{{ _type.label }}</span>
            </li>
        </ul>
    </div>
</template>

<script lang="ts">
// Types
import type { I_Product } from '~/types/product';

// Vue
import { defineEmits } from 'vue';
// Constants
import { TYPE_LIST } from '~/constants/product-type';

export default {
    emits: {
        change: (value: I_Product['type'] | null) => true
    },

    setup(_, { emit }) {
        const typeList = ref(TYPE_LIST.map(type => ({ ...type, isActive: false })));

        const handleItemClick = (key: I_Product['type']) => {
            typeList.value.forEach(_type => {
                if (_type.key === key) {
                    _type.isActive = !_type.isActive;
                    emit('change', _type.isActive ? key : null);
                } else {
                    _type.isActive = _type.key === key;
                }
            });
        }

        return {
            typeList,
            handleItemClick,
        }
    }
}
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.type-list {
    width: 100%;
    padding: 8px;
    border-radius: var(--border-radius);
    border: 1px solid var(--c-border);
    background-color: #fff;
    @include flex($alignItems: center, $wrap: wrap);

    .item {
        flex: 0 0 132px;
        padding: 8px;
        border-radius: var(--border-radius);
        border: 1px solid transparent;
        cursor: pointer;
        transition: border-color var(--transition);
        @include flex($direction: column, $alignItems: center, $gap: 4px);

        img {
            width: 62px;
            height: 60px;
            object-fit: cover;
            transform: scale(0.9);
            transition: transform var(--transition);
        }

        span {
            font-weight: 300;
            font-size: 14px;
            color: var(--c-text-secondary);
        }

        &--active {
            img {
                transform: scale(1.1);
            }

            span {
                color: var(--c-primary);
            }
        }
    }
}
</style>