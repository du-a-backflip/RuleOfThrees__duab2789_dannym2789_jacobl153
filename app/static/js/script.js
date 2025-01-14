var interactable = document.getElementById("interact");
var scoretxt = document.getElementById("scoretxt");
var text = document.getElementById("gametext");
var hightxt = document.getElementById("topscore");
var minInterval = 2000;
var maxInterval = 5000;
var topscore = 0;
var timeDiff = 0;
var waitClick = false;
var initial = true;
var early = false;
var randomTime = 0;
var timeID = 0;

function reaction() {
    randomTime = Math.floor(Math.random() * (maxInterval - minInterval)) + minInterval;
    if (!early){
        text.textContent = "Get Ready!";
        interactable.style.background = "#0096FF";

        timeID = setTimeout(function() {
            timeDiff = Date.now();
            text.textContent = "Click!";
            interactable.style.background = "#009578";
            waitClick = true;
        }, randomTime);
    }
    else{
        text.textContent = "Too early! Click to try again!";
        interactable.style.background = "#C41E3A";
        clearTimeout(timeID);
    }
}

interactable.addEventListener("click", function(){
    if (waitClick){
        initial = false;
        score = Date.now() - timeDiff;
        waitClick = false;
        text.textContent = score + " milliseconds";
        scoretxt.textContent = "Time: " + score + " milliseconds";

        if (score < topscore || hightxt.innerHTML == ""){
            topscore = score;
            hightxt.textContent = score + " milliseconds";
            initial = true;
        }
    }
    else if (early){
        early = false;
        reaction();
    }
    else{
        if(!initial){
            early = true;
        }
        else{
            initial = false;
        }
        reaction();
    }
});
