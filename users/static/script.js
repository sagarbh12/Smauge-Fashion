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
