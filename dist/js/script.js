const hamburger = document.querySelector('.hamburger');
const menu = document.querySelector('.menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('is-active');
    menu.classList.toggle('menu-active');
});

window.addEventListener("scroll", () => {
    hamburger.classList.remove("is-active");
    menu.classList.remove("menu-active");
});

var mysong = document.getElementById("mysong");
var icon = document.getElementById("icon");
    icon.onclick =function(){
        if(mysong.paused){
            mysong.play();
            icon.src = "assets/images/pause.png";
        }else{
                mysong.pause();
                icon.src = "assets/images/play.png";
        }
    }