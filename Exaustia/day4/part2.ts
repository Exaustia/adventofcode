const fs = require("node:fs");
const readline = require("node:readline");

(async () => {
  const lines = await processLineByLine();

  let sumOfRangeContainOther = 0;
  for (const line of lines) {
    const [firstRange, secondRange] = line.split(" ")[0].split(",");
    const [firstRangeStart, firstRangeEnd] = firstRange.split("-");
    const [secondRangeStart, secondRangeEnd] = secondRange.split("-");

    if (
      Math.max(firstRangeStart, secondRangeStart) <=
      Math.min(firstRangeEnd, secondRangeEnd)
    ) {
      sumOfRangeContainOther++;
    }
  }
  console.log(sumOfRangeContainOther);
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
