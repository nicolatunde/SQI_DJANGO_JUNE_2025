// Show popup 3 seconds after page load
window.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => {
    const popup = document.getElementById("newsletter-popup");
    if (popup) popup.style.display = "flex";
  }, 3000);
});

// Close popup when clicking close button
document.addEventListener("DOMContentLoaded", function () {
  const closeBtn = document.getElementById("popup-close");
  closeBtn?.addEventListener("click", () => {
    const popup = document.getElementById("newsletter-popup");
    if (popup) popup.style.display = "none";
  });
});
