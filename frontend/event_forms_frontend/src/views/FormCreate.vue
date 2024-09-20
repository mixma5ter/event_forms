<template>
  <div>
    <h2>Конструктор форм</h2>
    <router-link to="/">Главная страница</router-link>
    <router-link to="/list">Список форм</router-link>
    <formly-form :model="model" :fields="fields" @submit.prevent="onSubmit">
      <button type="submit">Сохранить форму</button>
    </formly-form>
  </div>
</template>

<script>
import VueFormly from 'vue-formly'
import VueFormlyBootstrap from 'vue-formly-bootstrap'
import axios from 'axios';

export default {
  components: {
    VueFormly,
    VueFormlyBootstrap,
  },
  data() {
    return {
      model: {}, // Данные формы
      fields: [
        // Начальные поля формы
      ],
      availableFields: [
        {
          label: 'Текстовое поле',
          type: 'input',
          key: 'textField',
          props: {
            label: 'Текст',
            placeholder: 'Введите текст',
          },
        },
        {
          label: 'Числовое поле',
          type: 'number',
          key: 'numberField',
          props: {
            label: 'Число',
            placeholder: 'Введите число',
          },
        },
        // ... другие типы полей
      ],
    };
  },
  methods: {
    onSubmit() {
      // Отправка структуры формы (this.fields) на backend
      axios.post('/api/forms/', {
        title: 'Название формы',
        structure: this.fields
      })
          .then(response => {
            // Обработка ответа
            console.log('Форма сохранена:', response.data);
          })
          .catch(error => {
            // Обработка ошибки
            console.error('Ошибка при сохранении формы:', error);
          });
    },
  },
};
</script>