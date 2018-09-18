<!--
    Testimonial Component Documentation
    Functional component managing the Testimonials for Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <div v-if="current_testimonial != null" class="media">
        <div class="media-body">
            <h5 class="mt-0 mb-1">{{ current_testimonial.title }}</h5>
            <blockquote>
                {{ current_testimonial.content }}<br>
                <cite> -- {{ current_testimonial.person_name }}</cite>
            </blockquote>
        </div>
        <img :src="current_testimonial.person_image">
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data: function() {
            return {
                current_testimonial: null,
                testimonials: [],
                interval: 1000*60 //minutes
            }
        },
        methods: {
            changeTestimonial: function(){
                /* If testimonials are found fetch on randomly from the list */
                if (this.testimonials.length >= 1) {
                    this.current_testimonial = this.testimonials[ Math.floor(Math.random() * this.testimonials.length)];
                } else {
                    this.current_testimonial = null
                }
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
            window.setInterval(() => {
                this.changeTestimonial();
            }, this.interval);
        }
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
    img{
        width:100px;
    }
</style>
