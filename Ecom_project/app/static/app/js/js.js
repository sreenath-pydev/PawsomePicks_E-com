/* carousel autoplay */ 
document.addEventListener('DOMContentLoaded', function() {
  // Your custom JavaScript code here
  var myCarousel = document.querySelector('#carouselExampleFade');
  if (myCarousel) {
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 5000,
      ride: 'carousel'
    });
  }
});


/* single product details view more */ 
document.addEventListener('DOMContentLoaded', function() {
  var viewMoreBtn = document.getElementById('viewMoreBtn');
  var extraDetails = document.getElementById('extraDetails');
  
  viewMoreBtn.addEventListener('click', function() {
      if (extraDetails.style.display === 'none') {
          extraDetails.style.display = 'block';
          viewMoreBtn.style.display = 'none'; // Hide the "View More" button after clicking
      }
  });
});

/*navbar drop down hover effect */
document.addEventListener('DOMContentLoaded', function () {
  var dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(function (dropdown) {
      dropdown.addEventListener('mouseover', function () {
          this.querySelector('.dropdown-menu').classList.add('show');
      });

      dropdown.addEventListener('mouseleave', function () {
          this.querySelector('.dropdown-menu').classList.remove('show');
      });
  });
});

/*cart plus and minus */

$('.plus-cart').click(function(){
  var id = $(this).attr("pid").toString()
  var obj = this.parentNode.children[2]
  console.log("pid=",id)
  $.ajax({
    type : "GET",
    url : '/plus_cart',
    data : {
      prod_id : id
    },
    success:function(data){
      console.log("data = " ,data);
      obj.innerText = data.quantity
      document.getElementById('amount').innerText = data.amount
      document.getElementById('totalamount').innerText = data.totalamount
    }
    

  })
})
/* minus cart*/
$('.minus-cart').click(function(){
  var id = $(this).attr("pid").toString()
  var obj = this.parentNode.children[2]
  console.log("pid=",id)
  $.ajax({
    type : "GET",
    url : '/minus_cart',
    data : {
      prod_id : id
    },
    success:function(data){
      console.log("data = " ,data);
      obj.innerText = data.quantity
      document.getElementById('amount').innerText = data.amount
      document.getElementById('totalamount').innerText = data.totalamount
    }
    

  })
})
