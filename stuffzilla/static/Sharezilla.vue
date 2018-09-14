<template lang="html">

    <div>
        <sz-header></sz-header>
        <sz-interface></sz-interface>
        <sz-footer></sz-footer>
    </div>

</template>

<script>
import HeaderComponent from './components/structural/HeaderComponent.vue'
import InterfaceComponent from './components/structural/InterfaceComponent.vue'
import FooterComponent from './components/structural/FooterComponent.vue'

export default {
    name: 'Sharezilla',
    data: function() {
        return {}
    },
    components: {
        'sz-header': HeaderComponent,
        'sz-interface': InterfaceComponent,
        'sz-footer': FooterComponent,
    },

    mounted: function() {
    }
}
</script>

<style lang="scss" scoped>

</style>
