// Search Option
console.log("hellos")
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

// ### Sidebar ###
document.addEventListener("DOMContentLoaded", function() {
    const sidebarItems = document.querySelectorAll('.sidebar-nav li');

    sidebarItems.forEach(item => {
        item.addEventListener('click', function() {
            document.querySelector('.sidebar').style.width = '250px';
        });
    });
});


//  ### Edit Profile  ###
let profileDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");

let classList = profileDropdownList.classList;

const toggle = () => classList.toggle("active");

window.addEventListener("click", function (e) {
  if (!btn.contains(e.target)) classList.remove("active");
});

//  ### Edit and Delete Products ### 
function editProduct(productId) {
    // Redirect to edit page with product id
    window.location.href = `/edit_product/${productId}`;
  }

  function deleteProduct(productId) {
    if (confirm('Are you sure you want to delete this product?')) {
        $.ajax({
            type: 'POST',
            url: '/delete_product/' + productId + '/',  // Ensure trailing slash here
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                alert('Product deleted successfully!');
                // Reload the page to reflect the changes
                window.location.reload();
            },
            error: function (xhr, errmsg, err) {
              console.log(xhr.status + ': ' + xhr.responseText);
              alert('Error deleting product!');
            }
        });
    }
}


  
  
