<!--
    Market Component Documentation
    Structural component defining the main market view of Sharezilla
-->

<template lang="html">
    <div>
        <!-- template code-->
        <h1>{{ $t( 'market.heading' ) }}</h1>
        <p>Current Language: {{ $i18n.locale() }}</p>
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
