// Active Navbar 
let sections = document.querySelectorAll("section");
let navlinks = document.querySelectorAll("header ul li a");

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop;
        let height = sec.offsetHeight;
        let id = sec.getAttribute("id");

        if (top >= offset && top < offset + height){
            navlinks.forEach(link => { 
                link.classList.remove("active");
            });

            document.querySelectorAll('header ul li a[href*=' + id + ']').forEach(link => {
                link.classList.add("active");
            });
        };
    });
};

// Search Option
const icon = document.querySelector('.icon');
const search = document.querySelector('.search');
const input = document.getElementById('mysearch');
const clearButton = document.querySelector('.clear');

icon.onclick = function (event) {
    event.stopPropagation();
    search.classList.toggle('active');
    input.focus();
}

clearButton.onclick = function () {
    clearSearchInput();
}

document.addEventListener('click', function (event) {
    if (!search.contains(event.target)) {
        search.classList.remove('active');
    }
});

function clearSearchInput() {
    input.value = '';
}

function handleSearchInput() {
    const searchTerm = input.value.trim().toLowerCase();

    // Your logic for redirection based on the search term
    // For example, redirect to the blog section if the search term contains "blog"
    if (searchTerm.includes('blog')) {
        window.location.href = '/blog';
    }
    // Add more conditions for different sections or pages as needed
}

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


//### Landing Products ###
const buyBtns = document.getElementsByClassName('buy_btn');
const lan_images = document.getElementsByClassName("lan-images");
const lan_text=document.getElementsByClassName("lan-text");
const lan_text2=document.getElementsByClassName("lan-text2");
const lan_price=document.getElementsByClassName("lan-price");
const lan_img=document.getElementsByClassName("lan-img");

for (let i = 0; i < lan_images.length; i++) {
    lan_images[i].addEventListener("mouseover", (e) => {
        buyBtns[i].style.visibility = 'visible';
        lan_text[i].style.filter = 'blur(1px)';
        lan_text2[i].style.filter = 'blur(1px)';
        lan_img[i].style.filter = 'blur(1px)';
        lan_price[i].style.filter = 'blur(1px)';

    });

    lan_images[i].addEventListener("mouseout", (e) => {
        buyBtns[i].style.visibility = 'hidden';
        lan_text[i].style.filter = 'blur(0px)';
        lan_text2[i].style.filter = 'blur(0px)';
        lan_img[i].style.filter = 'blur(0px)';
        lan_price[i].style.filter = 'blur(0px)';

    });
}




  