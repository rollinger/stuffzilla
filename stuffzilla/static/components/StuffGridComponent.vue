<template>
    <h3>List</h3>
    <p>{{stufflist}}</p>
</template>

<script>
export default {
  name: 'StuffGridComponent',
  data: function() {
      return {
          stufflist: [],
      }
  },
  methods: {
      fetch_stufflist: function() {
          var api_call = '/api/stuff/'
          // Returns the Stufflist by API GET
          this.$http.get(api_call).then(response => {
            this.stufflist = response.data;
          }, response => {
            console.log(response);
          });
      }
  },
  mounted: function() {
      // When mounted fetch stuff
      this.fetch_stufflist()
  }
}
</script>

<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
</style>
