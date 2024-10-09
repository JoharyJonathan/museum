<template>
    <section class="vh-100 bg-image" style="background-image: url('https://mdbcdn.b-cdn.net/img/Photos/new-templates/search-box/img4.webp');">
      <div class="mask d-flex align-items-center h-100 gradient-custom-3">
          <div class="container h-100">
              <div class="row d-flex justify-content-center align-items-center h-100">
                  <div class="col-12 col-md-9 col-lg-7 col-xl-6">
                      <div class="card" style="border-radius: 15px;">
                          <div class="card-body p-5">
                              <h2 class="text-uppercase text-center mb-5">Create an account</h2>

                              <form @submit.prevent="register">
                                  <div data-mdb-input-init class="form-outline mb-4">
                                      <input v-model="username" type="text" id="form3Example1cg" class="form-control form-control-lg" required />
                                      <label class="form-label" for="form3Example1cg">Your Name</label>
                                  </div>

                                  <div data-mdb-input-init class="form-outline mb-4">
                                      <input v-model="email" type="email" id="form3Example3cg" class="form-control form-control-lg" required />
                                      <label class="form-label" for="form3Example3cg">Your Email</label>
                                  </div>

                                  <div data-mdb-input-init class="form-outline mb-4">
                                      <input v-model="password" type="password" id="form3Example4cg" class="form-control form-control-lg" required />
                                      <label class="form-label" for="form3Example4cg">Password</label>
                                  </div>

                                  <div class="d-flex justify-content-center">
                                      <button type="submit" class="btn btn-success btn-block btn-lg gradient-custom-4 text-body">Register</button>
                                  </div>
                              </form>

                              <p class="text-center text-muted mt-5 mb-0">Have already an account? <router-link to="/login" class="fw-bold text-body"><u>Login here</u></router-link></p>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </section>
</template>

<script>
    export default {
        name: 'signup-view',
        data(){
            return {
                username: '',
                email: '',
                password: ''
            };
        },
        methods: {
            async register(){
                try {
                    const response = await fetch('http://localhost:8000/users/api/signup/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                        },
                        body: JSON.stringify({
                            username: this.username,
                            email: this.email,
                            password: this.password
                        })
                    });
                    const data = await response.json();
                    if (response.ok) {
                        localStorage.setItem('access_token', data.access);
                        localStorage.setItem('refresh_token', data.refresh);
                        this.$router.push('/login');
                    } else {
                        console.error(data);
                    }
                } catch (error) {
                    console.error('Error during registration', error);
                }
            }
        }
    };
</script>

<style>

</style>