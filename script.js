let boxes = document.querySelectorAll(".box");
let reset = document.querySelector("#reset");
let newbtn = document.querySelector("#new");
let msgcontainer = document.querySelector(".msg-container");
let msg = document.querySelector("#msg");
let turn0 = true; // player0, playerX
let gameOver = false; // Add a flag to track game over status

const winPatterns = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

boxes.forEach((box) => {
    box.addEventListener("click", () => {
        if (box.innerText !== "" || gameOver) return; // Prevent further clicks on filled boxes or if game is over
        if (turn0) {
            box.innerText = "O";
            turn0 = false;
        } else {
            box.innerText = "X";
            turn0 = true;
        }
        checkWinner();
    });
});

const disableBoxes = () => {
    for (let box of boxes) {
        box.disabled = true;
    }
};

const enableBoxes = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
};

const showWinner = (winner) => {
    msg.innerText = `Congratulations, Winner is ${winner}`;
    msgcontainer.classList.remove("hide");
    disableBoxes();
    gameOver = true; // Set game over flag
};

const checkWinner = () => {
    let isDraw = true; // Assume it's a draw until proven otherwise
    for (let pattern of winPatterns) {
        let pos1 = boxes[pattern[0]].innerText;
        let pos2 = boxes[pattern[1]].innerText;
        let pos3 = boxes[pattern[2]].innerText;
        
        if (pos1 !== "" && pos2 !== "" && pos3 !== "") {
            if (pos1 === pos2 && pos2 === pos3) {
                console.log("winner", pos1);
                showWinner(pos1);
                return; // Exit function early if there is a winner
            }
        }
    }

    // Check if all boxes are filled to declare a draw
    for (let box of boxes) {
        if (box.innerText === "") {
            isDraw = false; // If there's an empty box, it's not a draw
        }
    }

    if (isDraw) {
        console.log("It's a draw");
        showDraw();
    }
};

const showDraw = () => {
    msg.innerText = "It's a draw!";
    msgcontainer.classList.remove("hide");
    disableBoxes();
    gameOver = true; // Set game over flag
};

const resetGame = () => {
    turn0 = true;
    enableBoxes();
    msgcontainer.classList.add("hide");
    gameOver = false; // Reset game over flag
};

newbtn.addEventListener("click", resetGame);
reset.addEventListener("click", resetGame);
