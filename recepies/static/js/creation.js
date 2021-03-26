function openCreation(type) {
    const shadow = document.getElementById("shadow__creation");
    const container = document.getElementById("container__creation");
    shadow.hidden = false;
    container.hidden = false;
}

function closeCreation() {
    const shadow = document.getElementById("shadow__creation");
    const container = document.getElementById("container__creation");
    shadow.hidden = true;
    container.hidden = true;
}

function addStep() {
    const step = document.querySelector("#step");
    step.value = "";
}

function addIngredient() {
    const step = document.querySelector("#quantity");
    step.value = "";
}