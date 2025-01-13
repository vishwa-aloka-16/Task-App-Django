menuOpenIcon = document.getElementById('menuOpen');
menuCloseIcon = document.getElementById('menuClose');
navBar = document.getElementById('navBar');

menuOpenIcon.addEventListener('click',function () {
    navBar.style.top="0";
    menuCloseIcon.style.display="block";
    menuOpenIcon.style.display="none";
})
menuCloseIcon.addEventListener('click',function () {
    navBar.style.top="-100vh";
    menuOpenIcon.style.display="block";
    menuCloseIcon.style.display="none";
})