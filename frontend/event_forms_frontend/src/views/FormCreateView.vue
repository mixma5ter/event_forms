<template>
  <main class="content">
    <section class="desk">
      <h2>Конструктор форм</h2>
      <router-link to="/">Главная страница</router-link>
      <router-link to="/list">Список форм</router-link>
    </section>
  </main>
</template>

<script>
// Пример загрузки данных из хранилища
// import { useDataStore } from "@/stores/data";
// import { computed, onMounted } from "vue";
//
// export default {
//   setup() {
//     const dataStore = useDataStore();
//
//     // Загрузка данных при монтировании компонента
//     onMounted(async () => {
//       if (!dataStore.isDataLoaded) {
//         await dataStore.loadData();
//       }
//     });
//
//     return {
//       forms: computed(() => dataStore.forms), // Доступ к формам
//       isDataLoaded: computed(() => dataStore.isDataLoaded),
//     };
//   },
// };
</script>