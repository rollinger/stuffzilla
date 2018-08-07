<template>
    <div class="grid-x">
        <div class="cell medium-6 large-4">
            <h1>ShareZilla</h1>
        </div>
        <div class="cell medium-6 large-8">
            <p>{{ randomQuote }}</p>
        </div>
    </div>
</template>

<script>
export default {
  name: 'TitleComponent',
  data: function() {
      return {
          quotes: ['Sharing is caring...',
          'Share your Stuff With the World',
          'Make the World more Efficient']
      }
  },
  computed: {
      randomQuote: function() {
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
