<!--
    Logo Component Documentation
    Functional component managing the Logo of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <router-link to='/' class="navbar-brand">
        {{ $t( 'Sharezilla' ) }}
        <img src="/staticfiles/images/favicons/favicon-32x32.png" width="32" height="32" class="d-inline-block align-top" alt="">
    </router-link>
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
