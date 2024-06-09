/* carousel autoplay */ 

var myCarousel = document.querySelector('#carouselExampleFade');
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 5000, // 2 seconds
  ride: 'carousel'
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


