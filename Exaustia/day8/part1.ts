import { th } from "date-fns/locale";

const fs = require("node:fs");
const readline = require("node:readline");
const { takeRight, dropRight, slice, isEmpty } = require("lodash");

(async () => {
  // read input.txt
  const lines = await processLineByLine();
  // parse input.txt
  const parsedLines = lines.map((line: string) => {
    return line.split("");
  });
  let sum = 0;
  for (let i = 1; i < parsedLines.length - 1; i++) {
    const line = parsedLines[i];

    for (let y = 1; y <= line.length - 2; y++) {
      const element = parseInt(line[y]);
      const leftArrayNotParsedToInt = slice(line, 0, y);
      const leftArray = leftArrayNotParsedToInt.map((element: string) => {
        return parseInt(element);
      });
      const rightArrayNotParsedToInt = slice(line, y + 1);
      const rightArray = rightArrayNotParsedToInt.map((element: string) => {
        return parseInt(element);
      });
      let topArray: number[] = [];
      let bottomArray: number[] = [];
      // get all the element in the top column
      parsedLines.forEach((parsedLine: any, index: number) => {
        let numberToPush = parseInt(parsedLine[y]);
        if (index < i) {
          topArray.push(numberToPush);
        } else if (index > i) {
          bottomArray.push(numberToPush);
        }
      });

      // get the max of the top array
      const maxTop = Math.max(...topArray);
      // get the max of the bottom array
      const maxBottom = Math.max(...bottomArray);
      // get the max of the left array
      const maxLeft = Math.max(...leftArray);
      // get the max of the right array
      const maxRight = Math.max(...rightArray);

      if (
        element > maxTop ||
        element > maxBottom ||
        element > maxLeft ||
        element > maxRight
      ) {
        sum++;
      }
    }
  }
  const lineLenght = parsedLines[0].length - 2;
  const columnLenght = parsedLines.length;

  console.log("SUM", sum + lineLenght * 2 + columnLenght * 2);
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
