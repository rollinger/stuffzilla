<template>
    <div class="grid-container">
        <div class="grid-x grid-margin-x">
            <div class="cell small-6 medium-4">
                <h1>ShareZilla</h1>
            </div>
            <div class="cell small-6 medium-8">
                <p>{{ getRandomQuote }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TitleComponent',
    data: function() {
        return {
            quotes: ['Sharing is Caring!',
            'Unused Value is Wasted Value',
            'Share your Stuff With the World',
            'Make the World more Efficient']
        }
    },
    computed: {
        getRandomQuote: function() {
            return this.quotes[ Math.floor(Math.random() * this.quotes.length) ]
        }
    }
}
</script>

<style lang="scss" scoped>
    h1 {
        text-align: center;
    }
</style>
