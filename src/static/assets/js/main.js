document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  toggleBtn.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden");
  });
});