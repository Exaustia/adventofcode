const fs = require("node:fs");
const readline = require("node:readline");

(async () => {
  const lines = await processLineByLine();
  let sumOfPriorities = 0;

  // group lines by 3 lines
  const groupedLines: string[][] = [];
  for (let i = 0; i < lines.length; i += 3) {
    groupedLines.push([lines[i], lines[i + 1], lines[i + 2]]);
  }

  for (const line of groupedLines) {
    const intersection = new Set(
      [...new Set(line[0].split(""))]
        .filter((x) => new Set(line[1].split("")).has(x))
        .filter((x) => new Set(line[2].split("")).has(x))
    );

    // get the priority of the item type
    const priorities = [...intersection].map((item: any) => {
      const charCode = item.charCodeAt(0);
      if (charCode >= 65 && charCode <= 90) {
        return charCode - 38;
      }
      return charCode - 96;
    });

    sumOfPriorities += Math.max(...priorities);
  }
  console.log(sumOfPriorities);
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
