<template>
  <div class="form-field">
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
  display: flex;
  align-items: center;
}
button {
  margin-left: 8px;
}
</style>