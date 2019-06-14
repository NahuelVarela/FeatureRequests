Vue.component('feature-request-comp', {
  data: function () {
    return {
      title: "Hamaca",
      description: "Para que la gente pueda dormir",
    }
  },
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
    message: 'Hello Vue!'
  }
});