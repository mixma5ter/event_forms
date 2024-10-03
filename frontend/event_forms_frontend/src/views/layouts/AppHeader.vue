<template>
  <header class="header">
    <div class="content">
      <div class="header__logo">
        <router-link :to="{ name: 'HomeView' }" class="">
          <img
              src="@/assets/img/mcko_logo_250_250.png"
              alt=""
              width="100"
              height="100"
          />
        </router-link>
      </div>
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
  background-color: var(--base-color);
  font-family: "Roboto", sans-serif;
  font-weight: 700;
  justify-content: center;
}
</style>