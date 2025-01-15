var randomtxt = "";
var typetext = document.getElementById("typetext");
var txtstore = typetext.innerHTML;
var timer = document.getElementById("timer");
var WPM = document.getElementById("livescore");
var typestate = false;
var typestore = "";
var punct = /\p{P}/gu;
var errorstate = false;
var errorcount = 0;
var totalcount = 0;
var time = 0;

function render(){
    typetext.innerHTML = "";
    txtstore.split('').forEach(chr => {
        typetext.appendChild(document.createElement('span'));
        var chrSpan = document.createElement('span');
        chrSpan.innerText = chr;
        typetext.appendChild(chrSpan);
    });
    timefxn();
}

document.addEventListener("click", function(event){
    if (!event.target.closest("#typetext")) {
        typestate = false;
        typetext.id = "typetext";
        return;
    };
    typestate = true;
    typetext.id = "typetext-active";
});

document.addEventListener("keydown", function(event){
    if (typestate){
        //console.clear();
        if ((/^[A-Za-z]+$/.test(event.key) && event.key.length == 1) || event.key.match(punct) || event.key == " "){
            typestore += event.key;
            totalcount++;
        }
        if (event.key == "Backspace" && typestore.length > 0){
            typestore = typestore.substring(0,typestore.length -1);
            totalcount--;
        }

        //console.log(typestore);

        var txtarray = typetext.querySelectorAll('span');
        var inputarray = typestore.split('');
        txtarray.forEach((chrSpan, i) => {
            var chr = inputarray[i];
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
        console.clear();
        console.log("total: " + totalcount + "\nerror: " + errorcount);
    }
});

function timefxn(){
    timer.innerHTML = 0;
    var init = Date.now();
    setInterval(function(){
        time = Math.abs(Math.floor((init - Date.now()) / 1000));
        timer.innerHTML = time;
    }, 100)
}

setInterval(function(){
    livescore.innerHTML = Math.max(0, Math.min(Math.floor(((totalcount/5) - errorcount) / (time/60)), 999));
}, 100);

render();