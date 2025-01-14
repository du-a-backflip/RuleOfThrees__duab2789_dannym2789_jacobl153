var interactable = document.getElementById("interact");
var scoretxt = document.getElementById("scoretxt");
var text = document.getElementById("gametext");
var hightxt = document.getElementById("topscore");
var minInterval = 2000;
var maxInterval = 5000;
var topscore = 0;
var timeDiff = 0;
var waitClick = false;
var randomTime = 0;

function reaction() {
    randomTime = Math.floor(Math.random() * (maxInterval - minInterval)) + minInterval;

    text.textContent = "Get Ready!";
    interactable.style.background = "#0096FF";

    setTimeout(function() {
        timeDiff = Date.now();
        interactable.style.background = "#009578";
        waitClick = true;
    }, randomTime);

}

interactable.addEventListener("click", function(){
    if (waitClick){
        score = Date.now() - timeDiff;
        waitClick = false;
        text.textContent = score + " milliseconds";
        scoretxt.textContent = "Time: " + score + " milliseconds";

        if (score < topscore || hightxt.innerHTML == ""){
            topscore = score;
            hightxt.textContent = score + " milliseconds";
        }
    }
    else{
        reaction();
    }
});