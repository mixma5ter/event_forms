<template>
  <header class="header">
    <div class="header__logo">
      <router-link :to="{ name: 'HomeView' }" class="logo">
        <img
            src="@/assets/img/mcko_logo_250_250.png"
            alt=""
            width="100"
            height="100"
        />
      </router-link>
    </div>
    <div class="header__info">
      <a href="https://mcko.ru/">
        <span>МОСКОВСКИЙ ЦЕНТР<br>КАЧЕСТВА ОБРАЗОВАНИЯ</span>
      </a>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader"
}
</script>

<style scoped>

.header {
  position: relative;
  z-index: 2;
  display: flex;
  padding: 20px;
  background-color: var(--primary-color);
  font-family: "Roboto", sans-serif;
  font-weight: 700;
}

.header__logo {
  padding-top: 10px;
  padding-bottom: 10px;
}

.header__info {
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>