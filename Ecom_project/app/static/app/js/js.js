// Carousel autoplay
document.addEventListener("DOMContentLoaded", function () {
  var myCarousel = document.querySelector("#carouselExampleFade");
  if (myCarousel) {
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 2000,
      ride: "carousel",
    });
  }
});
//offer banner carousel autoplay
document.addEventListener("DOMContentLoaded", function () {
  var myCarousel = document.querySelector("#ob-carouselExampleFade");
  if (myCarousel) {
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 2000,
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
          "Login and try agian"
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
// Thumbnail click function
function changeImage(imageUrl) {
  // Change the main image source
  var mainImage = $("#mainImage");
  mainImage.attr("src", imageUrl);

  // Remove existing zoom instance to avoid duplication
  $('.zoomContainer').remove(); // Removes the zoom container if it exists
  mainImage.removeData('elevateZoom'); // Removes any existing zoom data

  // Reinitialize elevateZoom
  mainImage.data("zoom-image", imageUrl).elevateZoom({
      zoomType: "window",
      cursor: "crosshair",
      zoomWindowWidth: 420,
      zoomWindowHeight: 420,
      borderSize: 1,
      borderColor: "#333",
      zoomWindowOffsetX: 20, // Corrected typo in zoomWindowOffsetX
      zoomWindowOffsetY: 20, // Added Y offset for consistency with initialization
      responsive: true,
      easing: true
  });

  // Remove the border from all thumbnails
  $('.small-images .col').css('borderColor', 'transparent');

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
      zoomWindowOffsetX: 20,
      zoomWindowOffsetY: 20,
      responsive: true,
      easing: true
  });
});
// to toggle form visibility and hide/show existing addresses
function toggleAddressForm() {
  var form = document.getElementById('address-form');
  var existingAddresses = document.getElementById('existing-addresses');
  
  if (form.classList.contains('d-none')) {
      form.classList.remove('d-none');
      existingAddresses.classList.add('d-none');
  } else {
      form.classList.add('d-none');
      existingAddresses.classList.remove('d-none');
  }
}
// Set a timeout to hide the message container after 3 seconds (3000 milliseconds)
document.addEventListener('DOMContentLoaded', function() {
  
  var messageContainer = document.getElementById('message-container');
  setTimeout(function() {
      if (messageContainer) {
          messageContainer.style.display = 'none'; // Hide the message container
      }
  }, 3000); 
});
// Print Invoice
function print_fun(p, redirectUrl) {
  var a = document.body.innerHTML;
  var b = document.getElementById(p).innerHTML;
  document.body.innerHTML = b;
  window.print();
  // Add a timeout to redirect after printing
  setTimeout(function() {
      window.location.href = redirectUrl; // Use the passed URL
  }, 1000); // Redirect after 1 second
}
// Scrolling down animation
document.addEventListener('DOMContentLoaded', function() {
  AOS.init({
    duration: 1000, 
    once: false      
  });
});

// live search

function LiveSearchInput(event) {
  const query = event.target.value;
  if (query.trim() === '') {
    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = '';
    searchResults.classList.remove('show');
    return;
  }

  fetch(`/livesearch?q=${query}`)
    .then((response) => response.json())
    .then((data) => DisplaySearchResults(data))
    .catch((error) => console.error('Error:', error));
}

function DisplaySearchResults(data) {
  const searchResults = document.getElementById('searchResults');
  searchResults.innerHTML = '';
  
  if (data.products.length === 0) {
    searchResults.innerHTML = '<p class="text-center p-2">No products found</p>';
    return;
  }

  data.products.forEach((product) => {
    const searchItems = document.createElement('a');
    searchItems.className = 'dropdown-item align-items-center d-flex gap-10';
    searchItems.href = `/product_details/${product.id}`;
    searchItems.innerHTML = `
      <img src="${product.product_image}" class="search-image" style="width: 100px; height: 100px; ">
      <div class="d-flex flex-column p-5">
        <h5 class="product-name">${product.product_name} <h6 class="product-price">₹ ${product.product_price}</h6></h5>
        
      </div>
    `;
    searchResults.appendChild(searchItems);
  });

  searchResults.classList.add('show');
}
