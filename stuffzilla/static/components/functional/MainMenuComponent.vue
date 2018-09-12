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
            <li class="nav-item">
                <router-link to='/profile' class="nav-link">
                    {{ $t( 'Profile' )}}
                    <span class="sr-only">(current)</span>
                </router-link>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="LangDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Lang
                </a>
                <div class="dropdown-menu" aria-labelledby="LangDropdown">
                    <a class="dropdown-item" href="#">En</a>
                    <a class="dropdown-item" href="#">Pt</a>
                    <a class="dropdown-item" href="#">Es</a>
                    <a class="dropdown-item" href="#">De</a>
                </div>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    User
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Sign Up</a>
                    <a class="dropdown-item" href="#">Login</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Logout</a>
                </div>
            </li>
        </ul>

        <form class="form-inline">
            <input class="form-control mr-sm-2" type="search" placeholder="You want..." aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Ask</button>
        </form>
    </div>
    
</template>

<script>
    // import Component from './components/../Component.vue'

    export default {
        //name: 'name-of-component',
        //components: {
            // import Components
        //},
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
</style>
