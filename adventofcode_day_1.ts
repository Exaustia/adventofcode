// DAY 1 https://adventofcode.com/2022/day/1

import axios from "axios";
const fs = require("node:fs");
const readline = require("node:readline");

(async () => {
  const elfs = await processLineByLine();
  const calories: number[] = [];
  for (let i = 0; i < elfs.length; i++) {
    const elf = elfs[i];
    let sum = 0;
    for (let j = 0; j < elf.length; j++) {
      sum += elf[j];
    }
    calories.push(sum);
  }
  // get the top 1
  const maxCal = Math.max(...calories);
  // get the top 3 max
  const top3 = calories
    .map((cal, index) => ({ cal, index }))
    .sort((a, b) => b.cal - a.cal)
    .slice(0, 3);

  const sumTop3 = top3.reduce((acc, cur) => {
    acc += cur.cal;
    return acc;
  }, 0);
  console.log(sumTop3);
})();

async function processLineByLine() {
  const fileStream = fs.createReadStream("elf.txt");

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });
  // Note: we use the crlfDelay option to recognize all instances of CR LF
  // ('\r\n') in input.txt as a single line break.
  let myElfs: number[][] = [];
  let elf: number[] = [];
  for await (const line of rl) {
    // Each line in input.txt will be successively available here as `line`.
    if (line !== "") {
      const cal = parseInt(line);
      elf.push(cal);
    } else {
      myElfs = [...myElfs, elf];
      // remove all element in elf
      elf = [];
    }
  }
  return myElfs;
}
