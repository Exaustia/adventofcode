import { th } from "date-fns/locale";

const fs = require("node:fs");

function getInput(filename: string) {
  return (
    fs
      .readFileSync(filename, { encoding: "utf-8" })
      // Remove the last character (the closing newline)
      .slice(0, -1)
  );
}

const int = (s: string) => parseInt(s, 10);

const res = new Set();

let rope: number[][] = [];

for (let i = 0; i < 10; i++) {
  if (!rope[i]) {
    rope.push(new Array(0, 0));
  }
}

(async () => {
  let dataString = await getInput("input.txt")
    .split(/\n/g)
    .map((x: string) => x.split(" "))
    .map((x: string[]) => x.map((y: string) => y.replace("\n", "")));

  for (const row of dataString) {
    const [direction, distance] = row;
    const distanceInt = int(distance);
    for (let i = 0; i < distanceInt; i++) {
      moveHead(direction);
    }
  }
  console.log("res", res.size);
})();

function moveHead(direction: string) {
  switch (direction) {
    case "R":
      rope[0][0] = rope[0][0] + 1;
      break;
    case "L":
      rope[0][0] = rope[0][0] - 1;
      break;
    case "U":
      rope[0][1] = rope[0][1] + 1;
      break;
    case "D":
      rope[0][1] = rope[0][1] - 1;
      break;
  }
  for (let i = 1; i < 10; i++) {
    rope[i] = follow(rope[i - 1], rope[i]);
  }
  const str = JSON.stringify(rope[9]);
  res.add(str);
}

function follow(h: number[], t: number[]) {
  let toGo = h.map((x: number, i: number) => x - t[i]);
  let toGoAbs = toGo.map((x: number) => Math.abs(x));
  let toGoSigns = [0, 0];

  toGoAbs.forEach((x: number, i: number) => {
    if (x !== 0) {
      toGoSigns[i] = toGo[i] / toGoAbs[i];
    }
  });

  if (toGoAbs.includes(2)) {
    let toGoAbs2 = toGoAbs.map((value, index) => {
      if (value === 2) {
        return index;
      }
    });

    toGoAbs2.forEach((index) => {
      if (index !== undefined) toGoAbs[index] -= 1;
    });

    // toGo = toGoAbs.map((value, index) => value * toGoSigns[index]);

    // let idxMax = toGoAbs.indexOf(Math.max(...toGoAbs));
    // toGoAbs[idxMax] = toGoAbs[idxMax] - 1;
    toGo = toGoAbs.map((x: number, i: number) => x * toGoSigns[i]);
    t = t.map((x: any, i: number) => x + toGo[i]);
    return t;
  } else {
    return t; // don't move
  }
}
