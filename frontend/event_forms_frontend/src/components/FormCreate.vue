<template>
  <div>
    <h2>Создать форму</h2>
    <form @submit.prevent="createForm">
      <div>
        <label for="title">Название:</label>
        <input type="text" id="title" v-model="form.title">
      </div>
      <button type="submit">Создать</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        title: '',
      },
    };
  },
  methods: {
    async createForm() {
      try {
        await axios.post('http://localhost:8000/api/forms/', this.form);
        // Обработка успешного создания формы, например, редирект
      } catch (error) {
        console.error('Ошибка при создании формы:', error);
      }
    },
  },
};
</script>