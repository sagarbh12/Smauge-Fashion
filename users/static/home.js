// Slider Home Page Image
const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
let currentSlide = 0;

function showSlide(slideIndex) {
    slides.forEach(s => s.classList.remove('active'));
    slides[slideIndex].classList.add('active');
    currentSlide = slideIndex;
}

function showNextSlide() {
    showSlide(currentSlide === slides.length - 1 ? 0 : currentSlide + 1);
}

function showPreviousSlide() {
    showSlide(currentSlide === 0 ? slides.length - 1 : currentSlide - 1);
}

prevBtn.addEventListener('click', showPreviousSlide);
nextBtn.addEventListener('click', showNextSlide);

function startSlideshow() {
    showNextSlide();
    setTimeout(startSlideshow, 4000); // Adjust the delay as needed
}
startSlideshow();