Vue.component('feature-request-comp', {
  data: function () {
    return {
      x: "",
      xxxx: "",
    }    
  },
  props:["title","description"],

  template: `<div class="card" style="width: 18rem;">
  				<div class="card-body">
   					<h5 class="card-title">{{title}}</h5>
    				<p class="card-text">{{description}}</p>
   					<a href="#" class="btn btn-primary">I like it!</a>
 				 </div>
			</div>`
})

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    featuresArray: [],

  },

  methods: {
    getFeatures: function(status){
      console.log('Comienzo la funcion');
      this.loading = true;
      path = "/api/featuresitems/?status=" + "status"
      this.$http.get('/api/featuresitems/?status=')
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
  this.getFeatures("");
}
});