var prev = document.getElementById("prev");
var next = document.getElementById("next");
var thumbnail = document.getElementsByClassName("thumbnail");
var main = document.getElementById("main");
let i=0;
var backgroundImg = new Array("Main_background.jpeg", "background1.jpeg","background2.jpeg", "background3.jpeg", "background4.jpeg", "background5.jpeg");

next.onclick = function()
{
    if(i<4)
    {
        //main.style.backgroundImage = 'url("'+backgroundImg[i+1]+'")';
        thumbnail[i+1].classList.add("active");
        thumbnail[i].classList.remove("active");
 	    i++;

    }
}


prev.onclick = function()
{
    if(i>0)
    {
 	    //main.style.backgroundImage = 'url("'+backgroundImg[i-1]+'")';
        thumbnail[i-1].classList.add("active");
        thumbnail[i].classList.remove("active");
        i--;
    }
}

// Onclick event for Submit button
function regBtn()
{

    var regId = document.getElementById("id").value;                // It takes the value enter in the Id textbox
    var regName = document.getElementById("name").value;            // It takes the value enter in the Name textbox
    document.getElementById("myForm").style.display = "none";       // It hides the Pop-up form
    eel.CaptureFaces(regId,regName);                                // calls the CaptureFaces() function with the user entered data from the textbox
}

// Onclick event for Register button
function openFrom(){
    document.getElementById("myForm").style.display = "block"; // It make the Pop-up form to appear
}

// Onclick event for Unlock button
function unlockBtn()
{
    eel.RecognizeFaces();    // calls the RecognizeFace() function
}