<template>
  <div id="app" class="container">
    <NavBar v-if="showNavbar" />
    <router-view/>
  </div>
</template>

<script>
  import NavBar from './components/NavBar.vue';

  export default {
    name: 'App',
    components: {
      NavBar
    },
    data(){
      return {
        showNavbar: true
      };
    },
    watch: {
      $route(to) {
        if (to.path === '/login' || to.path === '/signup') {
          this.showNavbar = false;
        } else {
          this.showNavbar = true;
        }
      }
    }
  };
</script>

<style>
</style>
