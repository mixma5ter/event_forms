<template>
  <nav aria-label="Page navigation" v-if="totalPages > 1">
    <ul class="pagination">
      <li class="page-item" :class="{ disabled: currentPage === 1 }">
        <a class="page-link" href="#" aria-label="Previous" @click.prevent="goToPage(currentPage - 1)">
          <span aria-hidden="true">&laquo;</span>
        </a>
      </li>

      <li class="page-item active">
        <span class="page-link">{{ currentPage }}</span>
      </li>

      <li class="page-item" :class="{ disabled: currentPage === totalPages }">
        <a class="page-link" href="#" aria-label="Next" @click.prevent="goToPage(currentPage + 1)">
          <span aria-hidden="true">&raquo;</span>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    currentPage: {
      type: Number,
      required: true,
    },
    totalPages: {
      type: Number,
      required: true,
    },
  },
  emits: ['update:current-page'],
  computed: {
    visiblePages() {
      const maxVisiblePages = 1; // Максимальное количество видимых страниц (без 1 и последней)
      const pages = [];

      if (this.totalPages <= maxVisiblePages + 2) { // Если страниц мало, показываем все
        for (let i = 2; i < this.totalPages; i++) {
          pages.push(i);
        }
      } else {
        const middlePage = Math.floor(maxVisiblePages / 2);
        const startPage = Math.max(2, this.currentPage - middlePage);
        const endPage = Math.min(this.totalPages - 1, startPage + maxVisiblePages - 1);

        for (let i = startPage; i <= endPage; i++) {
          pages.push(i);
        }
      }

      return pages;
    },
  },
  methods: {
    goToPage(page) {
      this.$emit('update:current-page', page);
    },
  },
};
</script>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  margin: 0;
  padding: 0;
}

.page-item {
  list-style: none;
  margin: 0 0.2rem;
}

.page-link {
  display: inline-block;
  width: 2.5rem;
  height: 2.5rem;
  background-color: var(--primary-color-100);
  color: var(--text-color);
  text-align: center;
  line-height: 2.5rem;
  border-radius: 3px;
  text-decoration: none;
}

.page-link:hover {
  background-color: var(--primary-color-300);
  color: var(--text-color);
}

.page-item.active .page-link {
  background-color: var(--secondary-color-100);
}

.page-item.disabled .page-link,
.page-item.disabled .page-link:hover {
  color: var(--primary-color-100);
  background-color: var(--primary-color-300);
  cursor: not-allowed;
}
</style>