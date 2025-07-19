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


window.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".js-icon-github").forEach(el => el.innerHTML = `<svg ...>...</svg>`);
  document.querySelectorAll(".js-icon-linkedin").forEach(el => el.innerHTML = `<svg ...>...</svg>`);
  document.querySelectorAll(".js-icon-telegram").forEach(el => el.innerHTML = `<svg ...>...</svg>`);
  document.querySelectorAll(".js-icon-email").forEach(el => el.innerHTML = `<svg ...>...</svg>`);
});