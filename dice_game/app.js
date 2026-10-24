
const PIP_PATTERNS = {
    1: [[2, 2]],
    2: [[1, 1], [3, 3]],
    3: [[1, 1], [2, 2], [3, 3]],
    4: [[1, 1], [3, 3], [3, 1], [3, 3]],
    5: [[1, 1], [1, 3], [2, 2], [3, 1], [3, 3]],
    6: [[1, 1], [2, 1], [3, 1], [1, 3], [2, 3], [3, 3]]
};

function renderDie(element, value) {
    element.innerHTML = "";
    const pattern = PIP_PATTERNS[value] || PIP_PATTERNS[1];

    pattern.forEach(([r, c]) => {
        const pip = document.createElement("div");
        pip.className = "pip";
        pip.style.gridRow = r;
        pip.style.gridColumn = c;
        element.appendChild(pip);
    });
}

// Set initial dice to 1
renderDie(document.getElementById("p-die-1"), 1);
renderDie(document.getElementById("p-die-2"), 1);
renderDie(document.getElementById("c-die-1"), 1);
renderDie(document.getElementById("c-die-2"), 1);

const btnRoll = document.getElementById("btn-roll");
const btnReset = document.getElementById("reset-btn");
const resultMsg = document.getElementById("result-msg");
const allDice = document.querySelectorAll('.die');

btnRoll.addEventListener("click", async () => {
    btnRoll.disabled = true;
    btnReset.disabled = true;
    resultMsg.textContent = "Rolling...";
    allDice.forEach(die => die.classList.add("shake"));

    try {
        const res = await fetch('/roll', { method: "POST" })
        const data = await res.json();

        setTimeout(() => {
            // update dice
            renderDie(document.getElementById('p-die-1'), data.player_dice[0]);
            renderDie(document.getElementById('p-die-2'), data.player_dice[1]);
            renderDie(document.getElementById('c-die-1'), data.computer_dice[0]);
            renderDie(document.getElementById('c-die-2'), data.computer_dice[1]);

            // update totals
            document.getElementById('p-total').textContent = "Total: " + data.player_total;
            document.getElementById('c-total').textContent = "Total: " + data.computer_total;

            // update scoreboard
            document.getElementById('player-score').textContent = data.player_score;
            document.getElementById('computer-score').textContent = data.computer_score;
            document.getElementById('ties').textContent = data.ties;

            // update message
            resultMsg.className = `result-msg ${data.winner}`;
            resultMsg.textContent = `${data.message} (${data.player_score} vs ${data.computer_score})`;

            // enable buttons
            btnRoll.disabled = false;
            btnReset.disabled = false;
        }, 400);

    } catch (error) {
        console.error("Error:", error);
        allDice.forEach(die => die.classList.remove("shake"));
        btnRoll.disabled = false;
        btnReset.disabled = false;
        resultMsg.textContent = "Error occurred.";
    }
});

btnReset.addEventListener('click', async () => {
    try {
        const res = await fetch('/reset', { method: 'POST' });
        const data = await res.json();

        document.getElementById('p-total').textContent = "Total: 0";
        document.getElementById('c-total').textContent = "Total: 0";
        document.getElementById('player-score').textContent = "0";
        document.getElementById('computer-score').textContent = "0";
        document.getElementById('ties').textContent = "0";
        resultMsg.className = "result-msg";
        resultMsg.textContent = "Roll the dice!";
        btnRoll.disabled = false;
        btnReset.disabled = false;
    }
    catch (error) {
        console.error("Error:", error);
        btnRoll.disabled = false;
        btnReset.disabled = false;
        resultMsg.textContent = "Error occurred.";
    }
})