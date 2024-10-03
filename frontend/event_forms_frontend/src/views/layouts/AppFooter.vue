<template>
  <footer class="footer">
    <div class="footer__content">
      <p>
        <span>
          <a href="https://mcko.ru/">
            МОСКОВСКИЙ ЦЕНТР КАЧЕСТВА ОБРАЗОВАНИЯ
          </a>
        </span>
      </p>
      <p>
        {{ currentYear }} © Все права защищены
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "AppFooter",
  setup() {
    const currentYear = new Date().getFullYear();
    return { currentYear };
  }
}
</script>

<style scoped>
.footer {
  position: relative;
  z-index: 2;
  display: flex;
  padding: 20px;
  justify-content: center;
}

.footer__content {
  text-align: center;
}
</style>