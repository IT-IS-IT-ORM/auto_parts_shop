<template>
  <div class="bredcrumb">
    <div class="back-btn" @click="$router.go(-1)">
      <Icon name="ic:outline-arrow-back-ios" />
      Артқа
    </div>

    <ul class="links">
      <NuxtLink
        v-for="(item, index) in items"
        :key="index"
        :class="{ disabled: index === items.length - 1 }"
        :disabled="index === items.length"
        :to="item.link"
      >
        <span>{{ item.label }}</span>
      </NuxtLink>
    </ul>
  </div>
</template>

<script setup lang="ts">
export interface I_BreadcrumbItem {
  label: string;
  link: string;
}

defineProps<{
  items: I_BreadcrumbItem[];
}>();
</script>

<style scoped lang="scss">
@import "~/assets/style/mixins.scss";

.bredcrumb {
  @include flex($alignItems: center, $gap: 24px);

  .back-btn {
    color: var(--c-primary);
    cursor: pointer;
    @include flex($alignItems: center, $gap: 4px);

    svg {
      @include svgStyle($size: 36px);
    }
  }

  .links {
    @include flex($alignItems: center, $gap: 8px 24px, $wrap: wrap);

    a {
      position: relative;

      &:not(:last-child)::after {
        content: "/";
        transform: translateX(50%);
        @include positioned($top: 0, $right: -12px);
      }

      span {
        display: block;

        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        font-size: 18px;
      }
    }

    .disabled {
      cursor: not-allowed;

      span {
        max-width: 200px;
      }
    }
  }
}
</style>
