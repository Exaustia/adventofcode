import axios from "axios";
const fs = require("node:fs");
const readline = require("node:readline");
const calcScore = (player1: string, player2: string) => {
  let scorePlayer2 = 0;

  // Player 2 score
  switch (player2) {
    case "X":
      scorePlayer2 += 1;
      if (player1 === "C") {
        scorePlayer2 += 6;
      } else if (player1 === "A") {
        scorePlayer2 += 3;
      }
      break;
    case "Y":
      if (player1 === "A") {
        scorePlayer2 += 6;
      } else if (player1 === "B") {
        scorePlayer2 += 3;
      }
      scorePlayer2 += 2;
      break;
    case "Z":
      if (player1 === "B") {
        scorePlayer2 += 6;
      } else if (player1 === "C") {
        scorePlayer2 += 3;
      }
      scorePlayer2 += 3;
      break;
  }

  return scorePlayer2;
};

(async () => {
  // A = rock
  // B = paper
  // C = scissors

  // X = rock
  // Y = paper
  // Z = scissors

  // A = X
  // B = Y
  // C = Z

  // win round =  +6 points
  // lose round = 0 points
  // draw round = +3 points
  // Win with rock = +1 point
  // Win with paper = +2 points
  // Win with scissors = +3 points

  const fileStream = fs.createReadStream("input.txt");

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  let scorePlayerOne = 0;

  for await (const line of rl) {
    const [player1, player2] = line.split(" ");
    const my = calcScore(player1, player2);
    scorePlayerOne += my;
  }
  console.log("scorePlayerOne", scorePlayerOne);
})();

// async function processLineByLine() {
//   const fileStream = fs.createReadStream("input.txt");

//   const rl = readline.createInterface({
//     input: fileStream,
//     crlfDelay: Infinity,
//   });

//   for await (const line of rl) {
//   }
// }
