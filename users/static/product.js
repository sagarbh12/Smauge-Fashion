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

   
      
      

    