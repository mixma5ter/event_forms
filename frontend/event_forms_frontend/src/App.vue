<template>
  <app-layout>
    <router-view class="content" />
  </app-layout>
</template>

<script setup>
import AppLayout from "@/views/layouts/AppLayout.vue";
</script>

<style>
@import "@/assets/css/libs/normalize.css";
@import "@/assets/css/fonts.css";
@import "@/assets/css/colors.css";

body {
  font-family: "Roboto", sans-serif;
  font-weight: 300;
  color: var(--text-color);
  background-color: var(--background-color);
}

a {
  color: var(--text-color);
}

button {
  cursor: pointer;
}

.content {
  padding: 20px;
}
</style>