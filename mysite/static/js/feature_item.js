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
      path = "/api/featuresitems/?id=".concat(id);
      console.log(path);
      this.$http.get(path)
        .then((response) => {
            this.featuresArray = response.data[0];
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
    var url_str = window.location.href;
    var url = new URL(url_str);
    var id = url.searchParams.get("id");
    console.log("ID is " + id);
    this.getFeature(id);
    console.log(window.location.href);
  }
});