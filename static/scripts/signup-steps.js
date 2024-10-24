function goStep1() {
    document.getElementById("step1").style.display = "flex";
    document.getElementById("step2").style.display = "none";
    document.getElementById("step3").style.display = "none";
}

function goStep2() {
    document.getElementById("step1").style.display = "none";
    document.getElementById("step2").style.display = "flex";
    document.getElementById("step3").style.display = "none";
}

function goStep3() {
    document.getElementById("step1").style.display = "none";
    document.getElementById("step2").style.display = "none";
    document.getElementById("step3").style.display = "flex";
}