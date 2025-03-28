document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll("button");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            button.disabled = true;
            setTimeout(() => { button.disabled = false; }, 500); // Shorter delay
            console.log(button.innerText === "Next" ? "Next step" : "Generating itinerary");
        });
    });
});