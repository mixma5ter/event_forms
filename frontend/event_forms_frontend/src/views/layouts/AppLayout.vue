<template>
  <div>
    <app-header />
    <slot />
    <app-footer />
  </div>
</template>

<script setup>
import AppHeader from "./AppHeader.vue";
import AppFooter from "./AppFooter.vue";
</script>