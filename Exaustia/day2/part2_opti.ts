const fs = require("node:fs");
const readline = require("node:readline");

// X = loose
// Y = draw
// Z = win

(async () => {
  const lines = await processLineByLine();
  const combinaitons = [
    ["A", "X"], // out => loose => + 0   use scissors + 3 = 3
    ["A", "Y"], // out => draw => + 3   use rock + 1 = 4
    ["A", "Z"], // out => win =>  + 6   use paper + 2 =  8
    ["B", "X"], // out => loose =>  +0   use rock + 1 =  1
    ["B", "Y"], // out => draw =>  + 3   use paper + 2 =  5
    ["B", "Z"], // out => win =>  + 6   use scissors + 3 = 9
    ["C", "X"], // out => loose => + 0   use paper + 2 =  2
    ["C", "Y"], // out => draw =>  + 3  use scissors + 3 =  6
    ["C", "Z"], // out => win => + 6  use rock + 1 =  7
  ];
  const scores = [3, 4, 8, 1, 5, 9, 2, 6, 7];

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
