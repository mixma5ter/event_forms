<template>
  <div>
    <app-header/>
    <app-navigation/>
    <slot/>
    <app-footer/>
  </div>
</template>

<script>
import AppHeader from "@/views/layouts/AppHeader.vue";
import AppFooter from "@/views/layouts/AppFooter.vue";
import AppNavigation from "@/views/layouts/AppNavigation.vue";

export default {
  components: {
    AppHeader,
    AppFooter,
    AppNavigation,
  },
};
</script>