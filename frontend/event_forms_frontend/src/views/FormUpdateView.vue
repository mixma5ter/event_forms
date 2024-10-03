<template>
  <main class="content">
    <section class="desk">
      <h2>{{ form.title }}</h2>
      <form @submit.prevent="updateForm">
        <div>
          <label for="title">Название формы:</label>
          <input
              type="text"
              id="title"
              v-model="form.title"
              required
          />
        </div>

        <div>
          <label for="structure">Описание:</label>
          <textarea
              id="structure"
              v-model="form.structure"
          ></textarea>
        </div>

        <button type="submit">Сохранить</button>
      </form>
      <router-link :to="{ name: 'FormListView' }">Отмена</router-link>
    </section>
  </main>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import resources from "@/services/resources";

export default {
  setup() {
    const form = ref({ title: '', description: '' });
    const route = useRoute();
    const router = useRouter();

    const formId = route.params.id; // Получение ID формы из параметров маршрута

    onMounted(async () => {
      try {
        const res = await resources.forms.getFormById(formId);

        if (res.__state === "success") {
          form.value = res.data; // Присваиваем данные формы
        } else {
          console.error('Ошибка загрузки данных:', res.data); // Обработка ошибки
        }
      } catch (error) {
        console.error('Произошла ошибка:', error); // Обработка ошибки
      }
    });

    const updateForm = async () => {
      try {
        const res = await resources.forms.updateForm(form.value); // Метод обновления формы

        if (res.__state === "success") {
          await router.push({name: 'FormListView'}); // Переадресация после успешного обновления
        } else {
          console.error('Ошибка при обновлении:', res.data); // Обработка ошибки
        }
      } catch (error) {
        console.error('Произошла ошибка:', error); // Обработка ошибки
      }
    };

    return { form, updateForm };
  },
};
</script>

<style scoped>

</style>