// Toggle Dark Mode
const tombolMode = document.getElementById("tombol-mode");
const body = document.body;

tombolMode.addEventListener("click", () => {
  body.classList.toggle("dark-mode");
  
  // Ganti ikon tombol
  if (body.classList.contains("dark-mode")) {
    tombolMode.textContent = "night mode";
  } else {
    tombolMode.textContent = "light mode";
  }
});
