import { th } from "date-fns/locale";

const fs = require("node:fs");
const readline = require("node:readline");
const { takeRight, dropRight, slice, isEmpty, concat } = require("lodash");

(async () => {
  // read input.txt
  const lines = await processLineByLine();
  // parse input.txt
  const parsedLines = lines.map((line: string) => {
    return line.split("");
  });
  const sum: number[] = [];
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
      // regroup all the array
      const allArray = [
        topArray.reverse(),
        bottomArray,
        leftArray.reverse(),
        rightArray,
      ];
      const indexOfName = ["top", "bottom", "left", "right"];
      const threeMap = new Map();
      for (let i = 0; i < allArray.length; i++) {
        const array = allArray[i];
        const name = indexOfName[i];

        for (let j = 0; j < array.length; j++) {
          const three = array[j];

          if (element > three) {
            threeMap.set(name, threeMap.get(name) + 1 || 1);
          }
          if (element === three || element < three) {
            threeMap.set(name, threeMap.get(name) + 1 || 1);
            break;
          }
        }
      }

      // sum the number of three like this 1 * 2 * 3 * 4
      const sumOfThree = Array.from(threeMap.values()).reduce(
        (a: number, b: number) => a * b
      );

      sum.push(sumOfThree);
    }
  }
  // get the highest number of sumOfThree
  const maxSum = Math.max(...sum);
  console.log(maxSum);
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
