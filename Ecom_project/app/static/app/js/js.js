// Carousel autoplay
document.addEventListener("DOMContentLoaded", function () {
  var myCarousel = document.querySelector("#carouselExampleFade");
  if (myCarousel) {
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 5000,
      ride: "carousel",
    });
  }
});
//offer banner carousel autoplay
document.addEventListener("DOMContentLoaded", function () {
  var myCarousel = document.querySelector("#ob-carouselExampleFade");
  if (myCarousel) {
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 5000,
      ride: "carousel",
    });
  }
});
// navbar drop down hover effect
document.addEventListener("DOMContentLoaded", function () {
  var dropdowns = document.querySelectorAll(".dropdown");

  dropdowns.forEach(function (dropdown) {
    dropdown.addEventListener("mouseover", function () {
      this.querySelector(".dropdown-menu").classList.add("show");
    });
    dropdown.addEventListener("mouseleave", function () {
      this.querySelector(".dropdown-menu").classList.remove("show");
    });
  });
});
// cart plus button
$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var obj = this.parentNode.children[2];
  console.log("pid=", id);
  $.ajax({
    type: "GET",
    url: "/plus_cart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      console.log("data = ", data);
      obj.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("total_amount").innerText = data.total_amount;
    },
  });
});
// cart minus button
$(".minus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var obj = this.parentNode.children[2];
  console.log("pid=", id);
  $.ajax({
    type: "GET",
    url: "/minus_cart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      console.log("data = ", data);
      obj.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("total_amount").innerText = data.total_amount;
    },
  });
});
// Get the radio buttons  checkout page -(Enable the payment button if a radio button is selected)
const radioButtons = document.querySelectorAll(".address-radio");
radioButtons.forEach(function (radioButton) {
  radioButton.addEventListener("change", function () {
    document.getElementById("rzp-button1").disabled = false;
  });
});
// Add product to wishlist
$(document).ready(function () {
  $(".plus_wishlist").click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
      type: "GET",
      url: "/pluswishlist",
      data: {
        prod_id: id,
      },
      success: function (data) {
        window.location.href = `/product_details/${id}`;
      },
      error: function (xhr, status, error) {
        console.error("An error occurred: " + error);
        alert(
          "An error occurred while adding the product to the wishlist. Please try again."
        );
      },
    });
  });
  // Remove product from wishlist
  $(".minus_wishlist").click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
      type: "GET",
      url: "/minuswishlist",
      data: {
        prod_id: id,
      },
      success: function (data) {
        window.location.href = `/product_details/${id}`;
      },
      error: function (xhr, status, error) {
        console.error("An error occurred: " + error);
        alert(
          "An error occurred while removing the product from the wishlist. Please try again."
        );
      },
    });
  });
});
// Dog products slider
var dogSwiper = new Swiper(".dog-slider .slide-content", {
  slidesPerView: 4,
  spaceBetween: 25,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".dog-swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".dog-swiper-next",
    prevEl: ".dog-swiper-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
    1130: {
      slidesPerView: 4,
    },
    1400: {
      slidesPerView: 5,
    },
  },
});
//cat products slider
var catSwiper = new Swiper(".cat-slider .slide-content", {
  slidesPerView: 4,
  spaceBetween: 25,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".cat-swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".cat-swiper-next",
    prevEl: ".cat-swiper-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
    1130: {
      slidesPerView: 4,
    },
    1400: {
      slidesPerView: 5,
    },
  },
});
//related products slider for product details section
var related_products_Swiper = new Swiper(".related-products-slider .slide-content", {
  slidesPerView: 4,
  spaceBetween: 25,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".cat-swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".cat-swiper-next",
    prevEl: ".cat-swiper-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
    1130: {
      slidesPerView: 4,
    },
    1400: {
      slidesPerView: 5,
    },
  },
});
// Thumbnail 
function changeImage(imageUrl) {
  // Change the main image source
  var mainImage = document.getElementById("mainImage");
  mainImage.src = imageUrl;
  
  // Remove existing zoom instance to avoid duplication
  $('.zoomContainer').remove(); // Removes the zoom container if it exists
  $('#mainImage').removeData('elevateZoom'); // Removes any existing zoom data

  // Reinitialize elevateZoom
  $("#mainImage").elevateZoom({
      zoomType: "window",
      cursor: "crosshair",
      zoomWindowWidth: 420,
      zoomWindowHeight: 420,
      borderSize: 1,
      borderColor: "#333",
      zoomWindowOffetx: 20,
  });

  // Remove the border from all thumbnails
  var thumbnails = document.querySelectorAll('.small-images .col');
  thumbnails.forEach(function(thumbnail) {
      thumbnail.style.borderColor = 'transparent';
  });

  // Add the border to the hovered thumbnail
  event.currentTarget.parentElement.style.borderColor = '#f48b48';
}
// Initialize zoom
$(document).ready(function() {
  $("#mainImage").elevateZoom({
      zoomType: "window",
      cursor: "crosshair",
      zoomWindowWidth: 420,
      zoomWindowHeight: 420,
      borderSize: 1,
      borderColor: "#333",
      zoomLevel: 1.5,
      zoomWindowOffetx: 20,
      zoomWindowOffsetY: 20,
      responsive: true, // Make zoom window responsive
      easing: true
  });
});

function changeImage(imageUrl) {
  $("#mainImage").attr("src", imageUrl);
  $("#mainImage").data("zoom-image", imageUrl).elevateZoom(); // Reinitialize zoom
}
