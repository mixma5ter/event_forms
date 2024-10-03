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

      <nav aria-label="Page navigation" v-if="totalPages > 1">
        <ul class="pagination">
          <li v-if="currentPage > 1" class="page-item">
            <a class="page-link" href="#" aria-label="Previous" @click.prevent="goToPage(currentPage - 1)">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>

          <li class="page-item" :class="{ active: currentPage === 1 }">
            <a class="page-link" href="#" @click.prevent="goToPage(1)">1</a>
          </li>

          <li v-if="currentPage > 3" class="page-item disabled">
            <span class="page-link">...</span>
          </li>

          <li class="page-item" v-for="page in visiblePages" :key="page" :class="{ active: currentPage === page }">
            <a class="page-link" href="#" @click.prevent="goToPage(page)">{{ page }}</a>
          </li>

          <li v-if="currentPage < totalPages - 2" class="page-item disabled">
            <span class="page-link">...</span>
          </li>

          <li class="page-item" :class="{ active: currentPage === totalPages }">
            <a class="page-link" href="#" @click.prevent="goToPage(totalPages)">{{ totalPages }}</a>
          </li>

          <li v-if="currentPage < totalPages" class="page-item">
            <a class="page-link" href="#" aria-label="Next" @click.prevent="goToPage(currentPage + 1)">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </section>
  </main>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue';
import resources from "@/services/resources";

export default {
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
