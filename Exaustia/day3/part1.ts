const fs = require("node:fs");
const readline = require("node:readline");

(async () => {
  const lines = await processLineByLine();
  let sumOfPriorities = 0;

  for (const line of lines) {
    const lenght = line.length;
    // cut the line in 2 parts
    const part1 = line.slice(0, lenght / 2).split("");
    const part2 = line.slice(lenght / 2, lenght).split("");

    // remove duplicata
    const firstPartCharsSet = new Set(part1);
    const secondPartCharsSet = new Set(part2);

    const intersection = new Set(
      [...firstPartCharsSet].filter((x) => secondPartCharsSet.has(x))
    );

    // Lowercase item types a through z have priorities 1 through 26.
    // Uppercase item types A through Z have priorities 27 through 52.

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
