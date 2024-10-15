<template>
    <div class="container">
        <div class="container bootstrap snippets bootdey">
            <h1 class="text-primary">Edit Profile</h1>
            <hr>
            <div class="row">

            <div class="col-md-3">
                <div class="text-center">
                    <img :src="user?.profile_image || 'https://bootdey.com/img/Content/avatar/avatar7.png'" class="avatar img-circle img-thumbnail" alt="avatar">
                    <h6>Upload a different photo...</h6>
                    <input type="file" class="form-control" @change="onFileChange">
                </div>
            </div>

            <div class="col-md-9 personal-info">
                <h3>Personal info</h3>
                    <form class="form-horizontal" role="form" @submit.prevent="updateProfile">
                        <div class="form-group">
                            <label class="col-lg-3 control-label">Username :</label>
                            <div class="col-lg-8">
                                <input class="form-control" type="text" v-model="user.username">
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="col-lg-3 control-label">Email:</label>
                            <div class="col-lg-8">
                                <input class="form-control" type="text" v-model="user.email">
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="my-2">
                                <button type="submit" class="btn btn-success rounded-sm">Update</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <hr>
    </div>
</template>

<script>
    import { jwtDecode } from 'jwt-decode';
    import axios from 'axios';

    export default {
        name: 'EditProfile',
        data() {
            return {
                user: {
                    id: '',
                    username: '',
                    email: '',
                    profile_image: ''
                },
                profileImage: null,
            };
        },
        created() {
            const token = localStorage.getItem('access_token');

            if (!token) {
                console.error("No access token found in localstorage");
                return;
            }

            try {
                const decodedToken = jwtDecode(token);

                const ImgUrl = decodedToken.profile_image ? `http://localhost:8000${decodedToken.profile_image}` : null;

                this.user = {
                    id: decodedToken.user_id,
                    username: decodedToken.username,
                    email: decodedToken.email,
                    profile_image: ImgUrl,
                }
                console.log("Id de l'user :" + this.user.id);
                console.log(decodedToken.profile_image);
            } catch (error) {
                console.error("Error decoding token", error);
            }
        },
        methods: {
            onFileChange(event) {
                this.profileImage = event.target.files[0];
            },
            updateProfile() {
                const formData = new FormData();
                formData.append('username', this.user.username);
                formData.append('email', this.user.email);

                if (this.profileImage) {
                    formData.append('profile_image', this.profileImage);
                }

                axios.put(`http://localhost:8000/users/api/profile/update/${this.user.id}/`, formData, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(response => {
                    console.log("Profile updated successfully", response.data);
                    this.logoutUser();
                })
                .catch(error => {
                    console.error("Error updating profile", error);
                });
            },
            logoutUser() {
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                this.$router.push('/login');
            }
        }
    }
</script>

<style>
    body{
        margin-top:20px;
    }
    .avatar{
        width:200px;
        height:200px;
    }
</style>