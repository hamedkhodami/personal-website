document.addEventListener("DOMContentLoaded", function () {

  const toggleButton = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");

  if (toggleButton && mobileMenu) {
    toggleButton.addEventListener("click", function () {
      console.log("Clicked!");
      mobileMenu.classList.toggle("hidden");
    });
  } else {
    console.log("❌");
  }
});