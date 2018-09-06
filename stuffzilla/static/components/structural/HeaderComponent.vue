<!--
    Header Component Documentation
    Structural component defining the header area of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <div class="top-bar">
        <div class="top-bar-left">
            <sz-logo></sz-logo>
        </div>
        <div class="top-bar-right">
            <sz-main-menu></sz-main-menu>
        </div>
    </div>

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
