<template>
  <main class="content">
    <section class="desk">
      <h2>Конструктор форм</h2>
      <router-link :to="{ name: 'HomeView' }">Главная страница</router-link>
      <router-link :to="{ name: 'FormListView' }">Список форм</router-link>

      <div class="form-builder">
        <input
            v-model="formTitle"
            placeholder="Название формы"
            class="form-title-input"
        />

        <form-field
            v-for="(field, index) in formFields"
            :key="index"
            :field.sync="formFields[index]"
            :placeholder="`Поле ${index + 1}`"
            @remove="removeField(index)"
        />

        <button @click="addField">Добавить поле</button>
      </div>

      <button @click="saveForm">Сохранить форму</button>
    </section>
  </main>
</template>

<script>
import { ref } from 'vue';
import resources from "@/services/resources";
import FormField from '@/common/FormField.vue';

export default {
  components: {
    FormField
  },
  setup() {
    // Название формы
    const formTitle = ref('');

    // Поля формы
    const formFields = ref([
      { title: 'Фамилия' },
      { title: 'Имя' },
      { title: 'Отчество' }
    ]);

    // Добавление нового поля
    const addField = () => {
      formFields.value.push({ title: '' });
    };

    // Удаление поля
    const removeField = (index) => {
      formFields.value.splice(index, 1);
    };

    // Сохранение формы
    const saveForm = async () => {
      const newForm = {
        title: formTitle.value || 'Без названия',
        structure: formFields.value
      };

      try {
        const res = await resources.forms.createForm(newForm);
        if (res.__state === "success") {
          console.log('Форма успешно сохранена');
          formTitle.value = '';  // Очистка названия формы
          formFields.value = []; // Очистка полей формы
        } else {
          console.error('Ошибка сохранения формы:', res.data);
        }
      } catch (error) {
        console.error('Произошла ошибка при сохранении формы:', error);
      }
    };

    return { formTitle, formFields, addField, removeField, saveForm };
  }
};
</script>

<style scoped>
.content {
  padding: 20px;
}

.form-title-input {
  display: block;
  width: 100%;
  margin-bottom: 15px;
  padding: 10px;
  font-size: 16px;
}

.form-builder {
  margin-top: 20px;
}

button {
  display: block;
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>