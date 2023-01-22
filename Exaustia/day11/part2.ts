// helped for the tricks to calculate the sum

import fs from "node:fs";
import { lcm } from "mathjs";

function getInput(filename: string) {
  const dataString = fs
    .readFileSync(filename, { encoding: "utf-8" })
    .split(/\n/g)
    .map((x: string) => x.split(" "))
    .map((x: string[]) =>
      x
        .map((y: string) =>
          y.replace("\n", "").replace("\r", "").replace(/:/, "")
        )
        .filter((z: string) => z !== "")
    )
    .filter((x: string[]) => x.length > 0);

  // group by 6 elements
  const data: any = [];
  for (let i = 0; i < dataString.length; i += 6) {
    data.push(dataString.slice(i, i + 6));
  }
  return data;
}

(async () => {
  const monkeys = getInput("input.txt");
  let monkeysWorries: any = [];
  for (let i = 0; i < monkeys.length; i++) {
    monkeysWorries.push([]);
  }

  let g = monkeys
    .map((m: any) => m[3][3])
    .reduce((a: any, b: any) => lcm(parseInt(a), parseInt(b)), 1);

  let index = 0;
  while (index < 10000) {
    for (const monkey of monkeys) {
      const [_, monkeyIndex] = monkey[0];
      const numberOfItems = monkey[1]
        .map((x: string) => parseInt(x))
        .filter((x: any) => !Number.isNaN(x));
      const [, , , , operation, value] = monkey[2];
      const [, , , disivibleBy] = monkey[3];
      const [, , , , , toMonkeyIsTrue] = monkey[4];
      const [, , , , , toMonkeyIfFalse] = monkey[5];

      for (const item of numberOfItems) {
        monkeysWorries[monkeyIndex] += 1;

        const operationNb = value === "old" ? item : parseInt(value);
        // multiplied
        let level = 0;
        switch (operation) {
          case "+":
            level = item + operationNb;
            break;
          case "-":
            level = item - operationNb;
            break;
          case "*":
            level = item * operationNb;
            break;
          case "/":
            level = item / operationNb;
            break;
        }

        // and rounded down to the nearest integer
        const worry = level % g;

        if (worry % disivibleBy === 0) {
          monkeys[toMonkeyIsTrue][1].push(worry);
          if (monkeyIndex !== toMonkeyIsTrue) {
            monkeys[monkeyIndex][1].splice(
              monkeys[monkeyIndex][1].indexOf(item),
              1
            );
          }
        } else {
          monkeys[toMonkeyIfFalse][1].push(worry);
          if (monkeyIndex !== toMonkeyIfFalse) {
            monkeys[monkeyIndex][1].splice(
              monkeys[monkeyIndex][1].indexOf(item),
              1
            );
          }
        }
      }
    }
    index++;
  }
  // console.log("Monkeys worries", monkeysWorries[0].length);
  monkeysWorries.forEach((element: any) => {
    console.log(element.length);
  });
  // order by number of items inspected
  const sorted = monkeysWorries.map((x: any) => x.length);

  // order by desc
  sorted.sort((a: any, b: any) => b - a);

  console.log("SUM", sorted[0] * sorted[1]);
})();
