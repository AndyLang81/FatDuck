// Select the burger icon and the nav menu
const burgerIcon = document.getElementById('burger-icon');
const navMenu = document.getElementById('nav-menu');

// Toggle the 'active' class on the nav when the burger icon is clicked
burgerIcon.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});