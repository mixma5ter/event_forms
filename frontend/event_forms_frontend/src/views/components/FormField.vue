<template>
  <div class="form-field">
    <span class="drag-handle">☰</span>
    <input
        v-model="field.title"
        :placeholder="placeholder"
        @input="$emit('update:field', field)"
    />
    <button @click="$emit('remove')">Удалить</button>
  </div>
</template>

<script>
export default {
  props: {
    field: {
      type: Object,
      required: true
    },
    placeholder: {
      type: String,
      default: 'Название поля',
    }
  }
};
</script>

<style scoped>
.form-field {
  margin-bottom: 8px;
  border: 1px solid #ccc;
  padding: 8px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.drag-handle {
  cursor: pointer;
  margin-right: 8px;
}

button {
  margin-left: 8px;
}
</style>