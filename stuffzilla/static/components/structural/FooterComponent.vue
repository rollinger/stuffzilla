<!--
    Footer Component Documentation
    Structural component defining the footer area of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <div class="grid-x grid-padding-x">
        <div class="cell medium-6">
            <sz-feedback></sz-feedback>
        </div>
        <div class="cell medium-6">
            <sz-testimonial></sz-testimonial>
        </div>
    </div>
</template>

<script>
    import FeedbackComponent from '../../components/functional/FeedbackComponent.vue'
    import TestimonialComponent from '../../components/functional/TestimonialComponent.vue'

    export default {
        //name: 'name-of-component',
        components: {
            'sz-feedback': FeedbackComponent,
            'sz-testimonial': TestimonialComponent,
        },
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
</style>
