<template>
  <div>
    <h2>Список форм</h2>
    <ul>
      <li v-for="form in forms" :key="form.id">
        {{ form.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      forms: [],
    };
  },
  mounted() {
    this.fetchForms();
  },
  methods: {
    async fetchForms() {
      try {
        const response = await axios.get('http://localhost:8000/api/forms/');
        this.forms = response.data;
      } catch (error) {
        console.error('Ошибка при получении форм:', error);
      }
    },
  },
};
</script>