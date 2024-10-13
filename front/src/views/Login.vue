<template>
    <section class="vh-100">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-6 text-black">
            <div class="px-5 ms-xl-4">
              <i class="fas fa-crow fa-2x me-3 pt-5 mt-xl-4" style="color: #709085;"></i>
              <img :src="require('@/assets/mu.png')" height="90" alt="" loading="lazy" style="margin-top: -3px;">
            </div>
  
            <div class="d-flex align-items-center h-custom-2 px-5 ms-xl-4 mt-5 pt-5 pt-xl-0 mt-xl-n5">
              <form @submit.prevent="login" style="width: 23rem;">
                <h3 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Log in</h3>
  
                <div data-mdb-input-init class="form-outline mb-4">
                  <input v-model="email" type="email" id="form2Example18" class="form-control form-control-lg" required />
                  <label class="form-label" for="form2Example18">Email address</label>
                </div>
  
                <div data-mdb-input-init class="form-outline mb-4">
                  <input v-model="password" type="password" id="form2Example28" class="form-control form-control-lg" required />
                  <label class="form-label" for="form2Example28">Password</label>
                </div>
  
                <div class="pt-1 mb-4">
                  <button data-mdb-button-init data-mdb-ripple-init class="btn btn-info btn-lg btn-block" type="submit">Login</button>
                </div>
  
                <p class="small mb-5 pb-lg-2"><a class="text-muted" href="#!">Forgot password?</a></p>
                <p>Don't have an account? <router-link to="/signup" class="link-info">Register here</router-link></p>
              </form>
            </div>
          </div>
          <div class="col-sm-6 px-0 d-none d-sm-block">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img3.webp"
              alt="Login image" class="w-100 vh-100" style="object-fit: cover; object-position: left;">
          </div>
        </div>
      </div>
    </section>
</template>

<script>
    export default {
        name: 'login-view',
        data() {
            return {
                email: '',
                password: '',
            };
        },
        methods: {
            async login() {
                try {
                    const response = await fetch('http://localhost:8000/users/api/login/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                        },
                        body: JSON.stringify({
                            username: this.email,
                            password: this.password
                        })
                    });
                    const data = await response.json();
                    if (response.ok) {
                        console.log('Access token :', data.access);
                        console.log('Refresh token :', data.refresh);
                        localStorage.setItem('access_token', data.access);
                        localStorage.setItem('refresh_token', data.refresh);
                        this.$router.push('/');
                    } else {
                        console.error(data);
                    }
                } catch (error) {
                    console.error('Error during login: ', error);
                }
            }
        }
    };
</script>

<style>
</style>