<template>
  <router-link :to="{ name: 'FormUpdateView', params: { id: form.id } }">
    <div class="form-item">
      <h3>{{ form.title }}</h3>
      <p v-if="form.description">{{ form.description }}</p>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'FormCard',
  props: {
    form: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.form-item {
  border: 1px solid var(--border-color);
  padding: 1rem;
  border-radius: 4px;
  background-color: var(--primary-color-200);
  transition: background-color 0.3s ease;
  /*cursor: pointer;*/
}

.form-item:hover {
  background-color: var(--primary-color-100);
}

.form-item h3 {
  margin-top: 0;
}

.form-item p {
  margin-bottom: 0;
}
</style>