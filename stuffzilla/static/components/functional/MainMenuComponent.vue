<!--
    Main Menu Component Documentation
    Functional component managing the Main Menu of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <div class="collapse navbar-collapse" id="navbarMainMenu">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <router-link to='/' class="nav-link">
                    {{ $t( 'Market' )}}
                    <span class="sr-only">(current)</span>
                </router-link>
            </li>
            <li v-if="profile.username" class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="userMenuDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <span>
                        <img :src="profile.public_profile.user_image" width="24" height="24" alt="">
                        {{ profile.username }}
                    </span>
                </a>
                <div class="dropdown-menu" aria-labelledby="userMenuDropdown">
                    <router-link to='/profile' class="dropdown-item">
                        {{ $t( 'Profile' ) }}
                        <span class="sr-only">(current)</span>
                    </router-link>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Logout</a>
                </div>
            </li>
            <span v-else>
                <a class="btn btn-outline-primary my-2 my-sm-0" href="#" role="button">Login</a>
                <a class="btn btn-outline-success my-2 my-sm-0" href="#" role="button">Sign Up</a>
            </span>
        </ul>

        <form class="form-inline">
            <input class="form-control mr-sm-2" type="search" placeholder="You want..." aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Ask</button>
        </form>
    </div>

</template>

<script>
    import axios from 'axios'

    export default {
        //name: 'name-of-component',
        data: function() {
            return {
                uid: '',
                profile: {
                    'username': '',
                    'public_profile': '',
                    'private_profile': '',
                    'internal_profile': '',
                },
            }
        },
        methods: {
            getUserProfile: function(){
                var api = `api/myprofile/${this.uid}/`;
                axios.get(api).then((response) => {
                    this.profile = response.data;
                });
            },
        },
        mounted: function(){
            // Get the user id and fetch the User Profile
            this.uid = document.documentElement.getAttribute('uid') || '';
            this.getUserProfile()
        }
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
</style>
