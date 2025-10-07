

const tombolMode = document.querySelector("#tombol-mode");

tombolMode.addEventListener("click", function() {
  document.body.classList.toggle("dark-mode");
});

const kotak = document.querySelector("#kotak-interaktif")

kotak.addEventListener("mouseover", function (){
    kotak.style.backgroundColor = "orangered"
    kotak.innerHTML = "Wow, kamu berhasil!";
});

kotak.addEventListener("mouseout",function(){
    kotak.style.backgroundColor = ""
    kotak.innerHTML = " Arahkan kursor ke sini";
});