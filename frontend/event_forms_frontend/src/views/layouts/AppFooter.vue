<template>
  <footer class="footer">
    <p>
      <span>
        <a href="https://mcko.ru/">
          МОСКОВСКИЙ ЦЕНТР КАЧЕСТВА ОБРАЗОВАНИЯ
        </a>
      </span>
    </p>
    <p>
      2025 © Все права защищены
    </p>
  </footer>
</template>

<script>
export default {
  name: "AppFooter"
}
</script>

<style scoped>

.footer {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column; /* Положение контента футера по вертикали */
  padding: 20px;
}
</style>