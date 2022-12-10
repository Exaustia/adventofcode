const fs = require("node:fs");
const readline = require("node:readline");
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
(async () => {
  const lines = await processLineByLine();
  const combinaitons = [
    ["A", "X"], // drawn - rock vs rock  +3 + 1 = 4
    ["A", "Y"], // win - rock vs paper +6 + 2 = 8
    ["A", "Z"], // lose - rock vs scissors 0 + 3 = 3
    ["B", "X"], // lose - paper vs rock 0 + 1 = 1
    ["B", "Y"], // drawn - paper vs paper +3 + 2 = 5
    ["B", "Z"], // win - paper vs scissors +6 + 3 = 9
    ["C", "X"], // win - scissors vs rock +6 + 1 = 7
    ["C", "Y"], // lose - scissors vs paper 0 + 2 = 2
    ["C", "Z"], // drawn - scissors vs scissors +3 + 3 = 6
  ];
  const scores = [4, 8, 3, 1, 5, 9, 7, 2, 6];

  const scorePlayerOne = lines.reduce(
    (acc: number, line: { split: (arg0: string) => [any, any] }) => {
      const [player1, player2] = line.split(" ");
      const index = combinaitons.findIndex(
        (combination) =>
          combination[0] === player1 && combination[1] === player2
      );
      return acc + scores[index];
    },
    0
  );

  console.log("scorePlayerOne", scorePlayerOne);
})();

async function processLineByLine() {
  const fileStream = fs.createReadStream("input.txt");

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  const lines: any = [];
  for await (const line of rl) {
    lines.push(line);
  }
  return lines;
}
