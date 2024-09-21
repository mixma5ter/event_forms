<template>
  <main class="content">
    <section class="desk">
      <h2>Список форм</h2>
      <router-link to="/">Главная страница</router-link>
      <router-link to="/create">Новая форма</router-link>
      <ul v-if="forms.length">
        <li v-for="form in forms" :key="form.id">
          {{ form.title }}
        </li>
      </ul>
      <p v-else>Форм пока нет.</p>
    </section>
  </main>
</template>

<script>
import forms from '../mocks/forms.json'

export default {
  data() {
    return {
      forms
    };
  }
};
</script>

<style scoped>

</style>