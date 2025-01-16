var typetext = document.getElementById("typetext");
var timer = document.getElementById("timer");
var WPM = document.getElementById("livescore");
var again = document.getElementById("again-hide");
var scoretxt = document.getElementById("scoretxt");
var highscoretxt = document.getElementById("topscore");
var txtstore = typetext.innerHTML;
var txtlen = txtstore.length;
var timeflow = false;
var rendered = false;
var typestate = false;
var gamestate = false;
var errorstate = false;
var winstate = false;
var typestore = "";
var punct = /\p{P}/gu;
var score = 0;
var highscore = 0;
var timeID = 0;
var errorcount = 0;
var totalcount = 0;
var blinkcount = 0;
var time = 0;

function render(){
    typetext.innerHTML = "";
    txtstore.split('').forEach(chr => {
        var blinkSpan = document.createElement('span');
        blinkSpan.classList.add('inactive')
        typetext.appendChild(blinkSpan);
        var chrSpan = document.createElement('span');
        chrSpan.classList.add('txt');
        chrSpan.innerText = chr;
        typetext.appendChild(chrSpan);
    });
    rendered = true;
}

document.addEventListener("click", function(event){
    if (!event.target.closest("#typetext")) {
        typestate = false;
        typetext.id = "typetext";
        var blinkarray = typetext.querySelectorAll('span.inactive, span.blinker');
        blinkarray.forEach((val, i) => {
            val.classList.remove('blinker');
            val.classList.add('inactive');
        });
        return;
    };
    gamestate = true;
    typestate = true;
    typetext.id = "typetext-active";
    var blinkarray = typetext.querySelectorAll('span.inactive, span.blinker');
    blinkarray.forEach((val, i) => {
        if (i == blinkcount){
            val.classList.add('blinker');
            val.classList.remove('inactive');
        }
        else {
            val.classList.remove('blinker');
            val.classList.add('inactive');
        }
    });
});

document.addEventListener("keydown", function(event){
    if (typestate){
        //console.clear();
        if ((/^[A-Za-z]+$/.test(event.key) && event.key.length == 1) || event.key.match(punct) || event.key == " "){
            typestore += event.key;
            totalcount++;
            blinkcount++;
        }
        if (event.key == "Backspace" && typestore.length > 0){
            event.preventDefault();
            typestore = typestore.substring(0,typestore.length -1);
            blinkcount--;
        }

        //console.log(typestore);

        var txtarray = typetext.querySelectorAll('span.txt');
        var blinkarray = typetext.querySelectorAll('span.inactive, span.blinker');
        var inputarray = typestore.split('');
        txtarray.forEach((chrSpan, i) => {
            var chr = inputarray[i];
            if (i == blinkcount){
                blinkarray[i].classList.add('blinker');
                blinkarray[i].classList.remove('inactive');
            }
            else {
                blinkarray[i].classList.remove('blinker');
                blinkarray[i].classList.add('inactive');
            }

            if (chr == chrSpan.innerText){
                chrSpan.classList.add('correct');
                chrSpan.classList.remove('error');
            }
            else if (chr == null){
                chrSpan.classList.remove('correct');
                chrSpan.classList.remove('error');
            }
            else {
                chrSpan.classList.remove('correct');
                chrSpan.classList.add('error');
                errorstate = true;
            }
        })
        if (errorstate){
            errorcount++;
            errorstate = false;
        }
        //console.clear();
        //console.log("total: " + totalcount + "\nerror: " + errorcount);
    }
});

function timefxn(){
    timer.innerText = 0;
    var init = Date.now();
    timeID = setInterval(function(){
        time = Math.abs(Math.floor((init - Date.now()) / 1000));
        timer.innerText = Math.floor(time/60) + ":" + Math.floor(time%60/10) + Math.floor(time%60 - Math.floor(time%60/10) * 10);
        livescore.innerText = Math.max(0, Math.min(Math.floor(((totalcount/5) - errorcount) / (time/60)), 999));
    }, 100);
    timeflow = true;
}

again.addEventListener("click", function(){
    if (winstate){
        typetext.innerText = getQuote();
        txtstore = typetext.innerText;
        WPM.innerText = "Typing Test";
        timer.innerText = "The timer starts when you start typing!";
        txtlen = txtstore.length;
        timeflow = false;
        rendered = false;
        typestate = false;
        gamestate = false;
        errorstate = false;
        winstate = false;
        typestore = "";
        punct = /\p{P}/gu;
        timeID = 0;
        errorcount = 0;
        totalcount = 0;
        blinkcount = 0;
        time = 0;

        typetext.classList.remove("hide");
        timer.classList.remove("hide");
        WPM.id = "livescore";
        again.id = "again-hide";
    }
});

function gameloop(){
    setInterval(function(){
        if (!gamestate && !rendered){
            render();
        }
        if (gamestate && !timeflow && typestore.length > 0){
            timefxn();
        }
        if (typestore.length >= txtlen && !winstate){
            clearInterval(timeID);
            winstate = true;
            gamestate = false;
            typestate = false;
            typetext.classList.add("hide");
            timer.classList.add("hide");
            WPM.id = "livescore-result";
            again.id = "again";
            
            score = parseInt(WPM.innerText);
            scoretxt.innerHTML = score + " WPM";
            if (score > highscore || highscoretxt.innerHTML == ""){
                highscoretxt.innerText = score + " WPM";
                initial = true;
            }
            //console.log("heheheheheheheheh done");
        }
    }, 50);
}

function getQuote(){
    var key = document.getElementById("apikey");
    //console.log(key);
    let param = {
        method: 'GET',
        headers: { 'x-api-key':  key.innerText}
    };

    let link = 'https://api.api-ninjas.com/v1/quotes';

    fetch(link, param)
        .then(res => {
            return res.json().then(data => {
                console.log(data[0].quote);
                return data[0].quote;
            }).catch(err => {
                console.log(err);
            })
        })
}

gameloop();