<!--
    Header Component Documentation
    Structural component defining the header area of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <header class="container-fluid sticky-top">
        <nav class="row navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">{{ $t( 'Sharezilla' ) }}
                <img src="/staticfiles/images/favicons/favicon-32x32.png" width="32" height="32" class="d-inline-block align-top" alt="">
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarMainMenu" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <sz-main-menu></sz-main-menu>

        </nav>
    </header>
</template>

<script>
    import LogoComponent from '../../components/functional/LogoComponent.vue'
    import MainMenuComponent from '../../components/functional/MainMenuComponent.vue'

    export default {
        //name: 'name-of-component',
        components: {
            'sz-logo': LogoComponent,
            'sz-main-menu': MainMenuComponent,
        },
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
</style>
