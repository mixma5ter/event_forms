<template>
  <main class="content">
    <section class="desk">
      <h2>Главная страница</h2>
      <router-link :to="{ name: 'FormListView' }">Список форм</router-link>
      <router-link :to="{ name: 'FormCreateView' }">Новая форма</router-link>
    </section>
  </main>
</template>

<script>

</script>

<style scoped>

</style>