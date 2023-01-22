import axios from "axios";
import { fi } from "date-fns/locale";
const fs = require("node:fs");
const readline = require("node:readline");

const addScoreLoose = (player1: string, player2: string) => {
  let scorePlayer2 = 0;
  // scissors
  if (player1 === "A") {
    scorePlayer2 += 3;
  }
  // paper
  else if (player1 === "B") {
    scorePlayer2 += 1;
  }
  // rock
  else if (player1 === "C") {
    scorePlayer2 += 2;
  }
  return scorePlayer2;
};

const addScoreDrawn = (player1: string, player2: string) => {
  let scorePlayer2 = 0;
  switch (player1) {
    case "A":
      scorePlayer2 += 1;
      break;
    case "B":
      scorePlayer2 += 2;
      break;
    case "C":
      scorePlayer2 += 3;
      break;
  }
  return scorePlayer2;
};

const addScoreWin = (player1: string, player2: string) => {
  let scorePlayer2 = 0;
  switch (player1) {
    case "A":
      scorePlayer2 += 2;
      break;
    case "B":
      scorePlayer2 += 3;
      break;
    case "C":
      scorePlayer2 += 1;
      break;
  }
  return scorePlayer2;
};

const calcScore = (player1: string, player2: string) => {
  let scorePlayer2 = 0;
  // X = loose
  // Y = draw
  // Z = win

  // A = rock
  // B = paper
  // C = scissors

  // X = rock
  // Y = paper
  // Z = scissors

  // Player 2 score
  let myscore = 0;
  switch (player2) {
    // Loose
    case "X":
      myscore += addScoreLoose(player1, player2);
      break;
    case "Y":
      myscore += 3;
      myscore += addScoreDrawn(player1, player2);
      break;
    case "Z":
      myscore += 6;
      myscore += addScoreWin(player1, player2);
      break;
  }

  return myscore;
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
