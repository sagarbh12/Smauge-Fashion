// ### Swiper Slide for Testimonials ###
const swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  
  // Optional: Pause slideshow on mouse hover
  const swiperContainer = document.querySelector(".mySwiper");
  swiperContainer.addEventListener("mouseenter", () => {
    swiper.autoplay.stop();
  });
  swiperContainer.addEventListener("mouseleave", () => {
    swiper.autoplay.start();
  });