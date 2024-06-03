/* carousel autoplay */ 

var myCarousel = document.querySelector('#carouselExampleFade');
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 5000, // 2 seconds
  ride: 'carousel'
});
