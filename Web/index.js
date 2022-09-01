const heroSection = document.querySelector(".header");
// =========================================
// Creating responsive navbar
// =========================================
const mobile_nav = document.querySelector(".mobile-navbar-btn");
const headerElem = document.querySelector(".header");

mobile_nav.addEventListener("click", () => {
  headerElem.classList.toggle("active");
})


// =========================================
// Creating a Portfolio Tabbed Componenet
// =========================================

const p_btns = document.querySelector(".p-btns");
const p_btn = document.querySelectorAll(".p-btn");
const p_img_elem = document.querySelectorAll(".img-overlay");

p_btns.addEventListener("click", (e) => {
    const p_btn_clicked = e.target;
    console.log(p_btn_clicked);

    p_btn.forEach((curElem) => curElem.classList.remove("p-btn-active"));

    p_btn_clicked.classList.add("p-btn-active");

    // To find the number in data  attr
    const btn_num = p_btn_clicked.dataset.btnNum;
    console.log(btn_num);

    const img_active = document.querySelectorAll(`.p-btn--${btn_num}`);

    p_img_elem.forEach((curElem) => curElem.classList.add("p-image-not-active"));
    
    img_active.forEach((curElem) => curElem.classList.remove("p-image-not-active"));
    // p_img_elem
    // p-btn--1

});


// =========================================
// Swiper JS Code
// =========================================
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 2,
    spaceBetween: 30,
    slidesPerGroup: 3,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });


// =========================================
// Scroll bottom to up
// =========================================
  const footerElem = document.querySelector(".section-footer");

  const scroollElement = document.createElement("div");
  scroollElement.classList.add("scrollTop-style");

  scroollElement.innerHTML = `<ion-icon name="arrow-up-outline" class="scroll-top"></ion-icon>`;

  footerElem.after(scroollElement);

  const scrollTop = () => {
    heroSection.scrollIntoView({behavior:"smooth"});
  }

  scroollElement.addEventListener("click",scrollTop)



