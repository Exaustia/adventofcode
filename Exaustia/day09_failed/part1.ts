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

let h = new Array(0, 0);
let t = new Array(0, 0);

let sum = 0;

(async () => {
  let dataString = await getInput("input.txt")
    .split(/\n/g)
    .map((x: string) => x.split(" "))
    .map((x: string[]) => x.map((y: string) => y.replace("\n", "")));

  for (const row of dataString) {
    const [direction, distance] = row;
    const distanceInt = int(distance);
    console.log(distanceInt);
    for (let i = 0; i < distanceInt; i++) {
      moveHead(direction);
      // console.log("direction", direction + " " + distance);
      // console.log("HEAD", h);
      // console.log("TAIL", t);
      // console.log("------------------");
      res.add(t.join(","));
    }
  }
  console.log("res", res.size);
})();

function moveHead(direction: string) {
  switch (direction) {
    case "R":
      h[0] = h[0] + 1;
      break;
    case "L":
      h[0] = h[0] - 1;
      break;
    case "U":
      h[1] = h[1] + 1;
      break;
    case "D":
      h[1] = h[1] - 1;
      break;
  }
  follow();
}

function follow() {
  let toGo = h.map((x, i) => x - t[i]);
  let toGoAbs = toGo.map((x) => Math.abs(x));
  let toGoSigns = [0, 0];

  toGoAbs.forEach((x, i) => {
    if (x !== 0) {
      toGoSigns[i] = toGo[i] / toGoAbs[i];
    }
  });

  if (toGoAbs.includes(2)) {
    let idxMax = toGoAbs.indexOf(Math.max(...toGoAbs));
    toGoAbs[idxMax] = toGoAbs[idxMax] - 1;
    toGo = toGoAbs.map((x: number, i: number) => x * toGoSigns[i]);
    t = t.map((x, i) => x + toGo[i]);
    sum++;
    return t;
  } else {
    return t; // don't move
  }
}
