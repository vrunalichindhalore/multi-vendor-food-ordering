console.log("JS Working");

const cartButtons = document.querySelectorAll(".card button");

console.log(cartButtons.length);

cartButtons.forEach(button => {
    button.addEventListener("click", () => {
        alert("Item Added To Cart");
    });
});