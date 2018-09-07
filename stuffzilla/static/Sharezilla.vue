<template lang="html">
    <div class="grid-y medium-grid-frame">
        <div class="cell shrink header medium-cell-block-container">
            <sz-header></sz-header>
        </div>
        <div class="cell medium-auto medium-cell-block-container">
            <sz-interface></sz-interface>
            <!--p>
                {{ request.user }} <br>
                {{ request.LANGUAGE_CODE }} <br>
                {{ request.user.user_profile.language }}
            </p-->
        </div>
        <div class="cell shrink header medium-cell-block-container">
            <sz-footer></sz-footer>
        </div>
    </div>
</template>

<script>
import HeaderComponent from './components/structural/HeaderComponent.vue'
import InterfaceComponent from './components/structural/InterfaceComponent.vue'
import FooterComponent from './components/structural/FooterComponent.vue'

export default {
    name: 'Sharezilla',
    components: {
        'sz-header': HeaderComponent,
        'sz-interface': InterfaceComponent,
        'sz-footer': FooterComponent,
    },
}
</script>

<style lang="scss" scoped>

</style>
