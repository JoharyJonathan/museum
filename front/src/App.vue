<template>
  <div id="app" class="container">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
          <div class="container-fluid">
            <!-- Navbar brand -->
            <a class="navbar-brand">
              <img :src="require('@/assets/mu.png')" height="48" alt="" loading="lazy" style="margin-top: -3px;">
            </a>
            <button class="navbar-toggler" type="button" data-mdb-collapse-init data-mdb-target="#navbarExample01"
              aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
              <i class="fas fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarExample01">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item active">
                  <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" aria-current="page" to="/">ArtWorks</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" aria-current="page" to="/about">About</router-link>
                </li>
              </ul>

              <ul class="navbar-nav d-flex flex-row">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="margin-right: 60px;">
                            Profile
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="{% url 'profile' %}">View Profile</a></li>
                            <li><a class="dropdown-item" href="{% url 'profile-update' %}">Update Profile</a></li>
                            <li><a class="dropdown-item" href="{% url 'watch_history' %}">History</a></li>
                            <li><a class="dropdown-item" href="{% url 'favorites-movies' %}">Favorites</a></li>
                            <li><a class="dropdown-item openmodal" href="#" data-toggle="modal" data-target="#myModal">Feed Back</a></li>
                            <li><a class="dropdown-item" href="{% url 'logout' %}">Log Out</a></li>
                        </ul>
                    </li>
              </ul>
            </div>
          </div>
        </nav>
        <!-- Navbar -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Ajoutez des styles globaux ici */
nav ul {
  list-style-type: none;
  padding: 0;
}
nav li {
  display: inline;
  margin-right: 10px;
}
</style>
