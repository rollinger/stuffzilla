<!--
    Footer Component Documentation
    Structural component defining the footer area of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <!-- O  TODO: Footer unsatisfactorial: fixed bottom better sticky-bottom and the InterfaceComponent is scrolling between the two - like Foundation-->
    <footer class="page-footer container-fluid fixed-bottom bg-light border-top d-none d-md-block">
        <div class="row align-items-center mt-3">
            <div class="col-sm-6">
                <sz-feedback></sz-feedback>
            </div>
            <div class="col-sm-6">
                <sz-testimonial></sz-testimonial>
            </div>
        </div>
    </footer>
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
