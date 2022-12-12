// I have don't understand how what i need to do this in first place,
// but i have take example https://github.com/jared-hughes/adventofcode/blob/master/2022/day12.ts
// Thanks this guy, i have understand how to do this

import fs from "fs";

function getInput(filename: string) {
  return fs.readFileSync(filename, { encoding: "utf-8" });
}

let dataString = getInput("input.txt");

function run(part: 1 | 2) {
  let S = [0, 0];
  let E = [0, 0];

  // convert the input to a 2D array of index of the letter
  // and set the start and end points
  let grid = dataString
    .split(/\n/g)
    .map((line, y) =>
      [...line].map((c, x) =>
        c == "S"
          ? ((S = [x, y]), 0)
          : c == "E"
          ? ((E = [x, y]), 25)
          : c.charCodeAt(0) - 97
      )
    );

  // get the length and width of the grid
  let w = grid[0].length;
  let h = grid.length;

  // create a set to store the visited points and add the end point
  let visited = new Set<string>();
  visited.add(E.join(","));
  // create a queue to store the points to visit and add the end point
  let queue = [[E[0], E[1], 0]];
  // create a counter to keep track of the current point
  let i = 0;
  // loop until the queue is empty
  while (true) {
    // get the current point
    let [x, y, dist] = queue[i];
    // increment the counter
    i += 1;
    // get the points that can be visited from the current point
    let pointsToCheck = [
      [x + 1, y],
      [x, y + 1],
      [x - 1, y],
      [x, y - 1],
    ];

    // find the points that can be visited from the current point
    let pointsAvailable = pointsToCheck.filter(
      ([u, v]) =>
        u >= 0 &&
        v >= 0 &&
        u <= w - 1 &&
        v <= h - 1 &&
        !visited.has(u + "," + v) &&
        grid[v][u] >= grid[y][x] - 1
    );

    // loop through the points that can be visited
    for (let [u, v] of pointsAvailable) {
      if (part === 1 ? u === S[0] && v === S[1] : grid[v][u] === 0) {
        console.log(dist + 1);
        return;
      }
      queue.push([u, v, dist + 1]);
      visited.add(u + "," + v);
    }
  }
}

run(1);
run(2);
