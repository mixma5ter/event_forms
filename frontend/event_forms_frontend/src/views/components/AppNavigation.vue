<template>
  <nav class="app-navigation">
    <ul>
      <li>
        <router-link :to="{ name: 'HomeView' }">Главная страница</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'FormListView' }">Список форм</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'FormCreateView' }">Новая форма</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "AppNavigation",
};
</script>

<style scoped>
.app-navigation {
  background-color: var(--secondary-color-100);
  padding: 0.5rem 0;
  text-align: center;
}

.app-navigation ul {
  display: inline-flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.app-navigation li {
  margin: 0 1rem;
}

.app-navigation a {
  color: var(--text-color);
  text-decoration: none;
}
</style>