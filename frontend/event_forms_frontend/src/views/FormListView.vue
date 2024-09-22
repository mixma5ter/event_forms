<template>
  <main class="content">
    <section class="desk">
      <h2>Список форм</h2>
      <router-link to="/">Главная страница</router-link>
      <router-link to="/create">Новая форма</router-link>
      <ul v-if="forms.length">
        <li v-for="form in forms" :key="form.id" class="">
          <router-link to="/">{{ form.title }}</router-link>
        </li>
      </ul>
      <p v-else>Форм пока нет.</p>
    </section>
  </main>
</template>

<script>
import resources from "@/services/resources";
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const forms = ref([]); // ref для реактивности

    onMounted(async () => {
      try {
        const res = await resources.forms.getForms();
        if (res.__state === "success") {
          forms.value = res.data;
        } else {
          console.error('Ошибка загрузки данных:', res.data); // Обработка ошибки
        }
      } catch (error) {
        console.error('Произошла ошибка:', error); // Обработка ошибки
      }
    });

    return { forms };
  },
};
</script>

<style scoped>

</style>