var app = new Vue({
  el: '#feature_list_item',
  data: {
    message: 'Hello Vue!',
    featuresArray: [],

  },

  methods: {
    getFeature: function(id){
      console.log('Comienzo la funcion');
      this.loading = true;
      path = "/api/featuresitems/1".concat(id);
      console.log(path);
      this.$http.get(path)
        .then((response) => {
            this.featuresArray = response.data;
            this.loading = false;
            console.log(this.featuresArray);
            console.log('Termino la funcion');
          })
        .catch((err) => {
            this.loading = false;
             console.log(err);
           });

    },
  },
  mounted() {
    this.getFeature("");
    console.log(window.location.href);
  }
});