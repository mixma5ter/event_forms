<template>
  <main class="content">
    <section class="desk">
      <h2>Список форм</h2>
      <ul v-if="forms.length">
        <li v-for="form in forms" :key="form.id">
          <router-link :to="{ name: 'FormUpdateView', params: { id: form.id } }">{{ form.title }}</router-link>
        </li>
      </ul>
      <p v-else>Форм пока нет.</p>

      <Pagination
          :current-page="currentPage"
          :total-pages="totalPages"
          @update:current-page="currentPage = $event"
      />
    </section>
  </main>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue';
import resources from "@/services/resources";
import Pagination from "@/views/components/Pagination.vue";

export default {
  components: {
    Pagination,
  },
  setup() {
    const forms = ref([]);
    const internalCurrentPage = ref(1);
    const totalPages = ref(1);

    const currentPage = computed({
      get: () => internalCurrentPage.value,
      set: (value) => {
        if (value >= 1 && value <= totalPages.value) {
          internalCurrentPage.value = value;
        }
      },
    });

    const fetchForms = async () => {
      try {
        const res = await resources.forms.getForms({ page: currentPage.value });
        if (res.__state === "success") {
          forms.value = res.data.results;
          totalPages.value = res.data.total_pages;
        } else {
          console.error('Ошибка загрузки данных:', res.data);
        }
      } catch (error) {
        console.error('Произошла ошибка:', error);
      }
    };

    const visiblePages = computed(() => {
      const pages = [];
      const pagesToShow = 3;

      // Calculate startPage and endPage within the computed property
      const startPage = Math.max(2, currentPage.value - Math.floor((pagesToShow - 1) / 2));
      const endPage = Math.min(totalPages.value - 1, startPage + pagesToShow - 1);

      for (let i = startPage; i <= endPage; i++) {
        pages.push(i);
      }
      return pages;
    });

    const goToPage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page;
      }
    };

    onMounted(fetchForms);

    watch(currentPage, fetchForms);

    return {
      forms,
      currentPage,
      totalPages,
      visiblePages,
      goToPage,
    };
  },
};
</script>
