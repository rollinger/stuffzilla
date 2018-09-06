<!--
    Main Menu Component Documentation
    Functional component managing the Main Menu of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <ul class="vertical medium-horizontal menu">
        <li><router-link to='/'><i class="fi-list"></i> <span>Market</span></router-link>
            <!--ul class="menu vertical">
                <li><a href="#">One</a></li>
                <li><a href="#">Two</a></li>
                <li><a href="#">Three</a></li>
            </ul-->
        </li>
        <router-link to='/profile'><i class="fi-list"></i> <span>Profile</span></router-link>
        <li><a href="#0"><i class="fi-list"></i> <span>Sign Up</span></a></li>
        <li><a href="#0"><i class="fi-list"></i> <span>Login</span></a></li>
        <li><a href="#0"><i class="fi-list"></i> <span>Logout</span></a></li>
    </ul>
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
