import { th } from "date-fns/locale";

const fs = require("node:fs");

function getInput(filename: string) {
  return fs.readFileSync(filename, { encoding: "utf-8" });
  // Remove the last character (the closing newline)
}

const int = (s: string) => parseInt(s, 10);

// cycle need to be completed
// first is one cycle before completion
const noop = 1;
// cycle need to be completed after 2
const addx = 2;
let cycle = 1;

const indexMap = new Map();
indexMap.set("noop", noop);
indexMap.set("addx", addx);

const XSet = new Map();
XSet.set(1, 1);
const BigXMap = new Map();

let sum = 0;

(async () => {
  let dataString = await getInput("input.txt")
    .split(/\n/g)
    .map((x: string) => x.split(" "))
    .map((x: string[]) =>
      x.map((y: string) => y.replace("\n", "").replace("\r", ""))
    );

  for (const row of dataString) {
    const [action, value] = row;
    const valueInt = int(value);
    if (action === "noop") {
      for (let i = 0; i < noop; i++) {
        cycle++;
        XSet.set(cycle, XSet.get(cycle - 1));
        if (cycle === 20 || (cycle - 20) % 40 === 0) {
          const XValue = XSet.get(cycle) * cycle;
          BigXMap.set(cycle, XValue);
        }
      }
    } else if (action === "addx") {
      for (let i = 0; i < addx; i++) {
        cycle++;
        XSet.set(cycle, XSet.get(cycle - 1));
        if (cycle + addx === cycle + i + 1) {
          const XValue = XSet.get(cycle) + valueInt;
          XSet.set(cycle, XValue);
        }
        if (cycle === 20 || (cycle - 20) % 40 === 0) {
          const XValue = XSet.get(cycle) * cycle;
          BigXMap.set(cycle, XValue);
        }
      }
    }
  }
  // sum of BigXMap
  for (const [key, value] of BigXMap) {
    sum += value;
  }
  console.log(BigXMap);
  console.log("sum", sum);
})();
