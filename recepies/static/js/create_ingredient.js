const app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]" ],
    data: {
        name: "",
        image: "",
        summary: "",
        quantity: 1,
        ingredients: {},
        selectedIngredient: "",
        ingredientOptions: {},
        type: "",
        steps: [],
        currentStep: "",
    },
    created: function() {
        this.type = document.querySelector("#title").innerHTML.toLowerCase();
        this.fetchIngredientOptions();
    },
    methods: {
        submit: function(e) {
            e.preventDefault();
            this.createFood(
                this.clearURL(`/${this.type}/create`),
            );
        },
        createFood: async function(url) {
            return await fetch(encodeURI(url), {
                method: "post",
                body: this.getData(),
                headers: {
                    'Content-Type': 'application/json',
                }
            }).then(res => res.json())
            .then(json => {
                console.log(json);
                window.location.replace(encodeURI(json.link));
            });
        },
        addIngredient: function () {
            if(this.selectedIngredient.name) {
                this.ingredients[this.selectedIngredient.name] = {
                    ...this.selectedIngredient,
                    quantity: this.quantity, 
                };
                this.selectedIngredient = {};
                this.quantity = 1;
            }
        },
        addStep: function () {
            if(this.currentStep) {
                this.steps.push(this.currentStep);
                this.currentStep = "";
            }
        },
        selectIngredient:function(ingredient){
            this.selectedIngredient = ingredient;
        },
        getData: function() {
            if(this.type == "ingredient") {
                return JSON.stringify({
                    name: this.name,
                    summary: this.summary,
                    image: this.image,
                });
            }
            return JSON.stringify({
                name: this.name,
                summary: this.summary,
                image: this.image,
                ingredients: this.ingredients,
                steps: this.steps
            })
        },
        clearURL: function(url) {
            return url.replace(/[\n\s]+/g, "");
        },
        fetchIngredientOptions: function() {
            if(this.type == "recepie") {
                return fetch(this.clearURL("/ingredient/list"))
                    .then(res => res.json())
                    .then(json => {
                        console.log(json);
                        this.ingredientOptions = json;
                    });
            }
            
        }
    }
})