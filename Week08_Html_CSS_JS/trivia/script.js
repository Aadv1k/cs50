function checkAnswer(button) {
    const question = document.getElementById("question1");
    const result = document.getElementById("result1");

    const isCorrect = button.textContent === "Paris";

    result.textContent = isCorrect ? "Correct!" : "Incorrect :/";
    result.className = isCorrect ? "correct" : "incorrect";

    button.style.backgroundColor = isCorrect ? "green" : "red";

    const choices = document.querySelectorAll(".choice");
    choices.forEach(choice => choice.disabled = true);
}

function checkFreeResponse() {
    const question = document.getElementById("question2");
    const answerInput = document.getElementById("answerInput");
    const result = document.getElementById("result2");

    const isCorrect = answerInput.value.toLowerCase() === "jupiter";

    result.textContent = isCorrect ? "Correct!" : "Incorrect";
    result.className = isCorrect ? "correct" : "incorrect";
    answerInput.className = isCorrect ? "correct" : "incorrect";

    answerInput.disabled = true;
    document.querySelector("button").disabled = true;
}

