function openCreation(type) {
    const shadow = document.getElementById("app_shadow");
    const app = document.getElementById("app");
    shadow.hidden = false;
    app.hidden = false;
}

function closeCreation() {
    const shadow = document.getElementById("app_shadow");
    const app = document.getElementById("app");
    shadow.hidden = true;
    app.hidden = true;
}

function addStep() {
    const step = document.querySelector("#step");
    step.value = "";
}