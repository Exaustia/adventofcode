const fs = require("node:fs");
const readline = require("node:readline");
const { takeRight } = require("lodash");

const orderMyCrates = (lines: any) => {
  let crates: string[] = [];
  for (const line of lines) {
    if (line === "" || line.includes("1")) {
      break;
    }
    crates.push(
      line
        .replace(/\s{2,5}/g, " - ")
        .replaceAll("[", "")
        .replaceAll("]", "")
        .split(" ")
        .filter((x: string) => x !== "")
    );
  }

  let orderCrates: string[][] = [];
  let index = 0;
  for (const crate of crates) {
    for (const letter of crate) {
      if (!orderCrates[index]) {
        orderCrates[index] = [];
      }
      orderCrates[index].push(letter);
      if (index === 8) {
        index = 0;
      } else {
        index++;
      }
    }
  }
  // inverse the array
  const reOrderCrates = orderCrates.map((e) => {
    return e.reverse().filter((x: string) => x !== "-");
  });
  return reOrderCrates;
};

const moveCrates = (
  lines: any,
  orderCrates: string[][],
  crateMover: Boolean = false
) => {
  let start = false;
  for (const line of lines) {
    // start when the line = ""

    if (line === "") {
      start = true;
    }
    if (start) {
      //move 3 from 8 to 9
      const [, nbOfCrate, , from, , to] = line.split(" ");
      if (nbOfCrate === undefined) continue;

      const nbOfCrateInt = parseInt(nbOfCrate);
      const fromInt = parseInt(from);
      const toInt = parseInt(to);
      // get the crates

      let getLastCrates = takeRight(orderCrates[fromInt - 1], nbOfCrateInt);

      if (!crateMover) getLastCrates.reverse();

      orderCrates[fromInt - 1] = orderCrates[fromInt - 1].slice(
        0,
        orderCrates[fromInt - 1].length - nbOfCrateInt
      );
      // add to the other
      orderCrates[toInt - 1] = [...orderCrates[toInt - 1], ...getLastCrates];
    }
  }

  return orderCrates;
};

(async () => {
  const lines = await processLineByLine();
  const crates = orderMyCrates(lines);
  const orderCrates = moveCrates(lines, crates, false); // true = crateMover = part 2  or false = part 1
  // get last crate from orderCrates
  const lastCrate = orderCrates.map((e) => e[e.length - 1]);

  // create line with lastCrate
  const line = lastCrate.join("");
  console.log(line);
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
