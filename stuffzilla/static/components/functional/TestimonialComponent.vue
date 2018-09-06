<!--
    Testimonial Component Documentation
    Functional component managing the Testimonials for Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <div class="media-object align-right">
        <div class="media-object-section">
            <h4>{{ current_testimonial.title }}</h4>
            <blockquote>
                {{ current_testimonial.content }}
                <cite>{{ current_testimonial.person_name }}</cite>
            </blockquote>
        </div>
        <div class="media-object-section align-middle">
            <div class="thumbnail">
                <img :src="current_testimonial.person_image">
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data: function() {
            return {
                current_testimonial: {},
                testimonials: [],
            }
        },
        methods: {
            changeTestimonial: function(){
                this.current_testimonial = this.testimonials[Math.floor(Math.random() * this.testimonials.length)];
            }
        },
        mounted: function() {
            var api = 'api/testimonials';
            axios.get(api).then((response) => {
                this.testimonials = response.data;
                //Call once
                this.changeTestimonial();
            });
            //Call every interval miliseconds
            var interval = 1000*60 //minute
            window.setInterval(() => {
                this.changeTestimonial();
            },interval);
        }
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
    img{
        width:100px;
    }
</style>
