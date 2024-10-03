<template>
  <main class="content">
    <section class="desk">
      <h2>Список форм</h2>
      <ul v-if="forms.length">
        <li v-for="form in forms" :key="form.id">
          <router-link :to="{ name: 'FormUpdateView', params: { id: form.id } }">{{ form.title }}</router-link>
        </li>
      </ul>
      <p v-else>Форм пока нет.</p>
    </section>
  </main>
</template>

<script>
import { ref, onMounted } from 'vue';
import resources from "@/services/resources";

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