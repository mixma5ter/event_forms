<template>
  <main class="content">
    <section class="desk">
      <h2>Конструктор форм</h2>
      <div class="form-builder">
        <input
            v-model="formTitle"
            placeholder="Название формы"
            class="form-title-input"
        />
        <draggable
            v-model="formFields"
            itemKey="id"
            @end="onDragEnd"
            handle=".drag-handle"
        >
          <template #item="{ element, index }">
            <form-field
                :field.sync="formFields[index]"
                :placeholder="`Поле ${index + 1}`"
                @remove="removeField(index)"
            />
          </template>
        </draggable>
        <button @click="addField">Добавить поле</button>
      </div>
      <button @click="saveForm">Сохранить форму</button>
    </section>
  </main>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router'; // Импортируем useRouter
import { v4 as uuidv4 } from 'uuid';
import resources from "@/services/resources";
import FormField from '@/views/components/FormField.vue';
import Draggable from 'vuedraggable';

export default {
  components: {
    FormField,
    Draggable
  },
  setup() {
    const router = useRouter(); // Получаем экземпляр маршрутизатора
    const formTitle = ref('');
    const formFields = ref([
      { id: uuidv4(), title: 'Фамилия' },
      { id: uuidv4(), title: 'Имя' },
      { id: uuidv4(), title: 'Отчество' }
    ]);

    const addField = () => {
      formFields.value.push({ id: uuidv4(), title: '' });
    };

    const removeField = (index) => {
      formFields.value.splice(index, 1);
    };

    const onDragEnd = (event) => {
      console.log('Поле перемещено', formFields.value);
    };

    const saveForm = async () => {
      const newForm = {
        title: formTitle.value || 'Без названия',
        structure: formFields.value
      };

      try {
        const res = await resources.forms.createForm(newForm);
        if (res.__state === "success") {
          console.log('Форма успешно сохранена');

          // Получение ID новой формы
          const newFormId = res.data.id;
          // Переадресация на FormUpdateView
          await router.push({name: 'FormUpdateView', params: {id: newFormId}});

          // Очищаем значения формы, но это не обязательно, так как будет переход на новый маршрут
          formTitle.value = '';
          formFields.value = [];
        } else {
          console.error('Ошибка сохранения формы:', res.data);
        }
      } catch (error) {
        console.error('Произошла ошибка при сохранении формы:', error);
      }
    };

    return { formTitle, formFields, addField, removeField, saveForm, onDragEnd };
  }
};
</script>

<style scoped>
.content {
  padding: 20px;
}

.form-title-input {
  margin-bottom: 15px;
  border: 1px solid #ccc;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.form-builder {
  margin-top: 20px;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 16px;
}
</style>