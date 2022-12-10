import { th } from "date-fns/locale";

const fs = require("node:fs");
const readline = require("node:readline");
const { takeRight } = require("lodash");

(async () => {
  // read input.txt
  const lines = await processLineByLine();

  const threeMap = new Map();
  threeMap.set("/", 0);
  const whereIAm: string[] = ["/"];
  // we start at the root
  for (let index = 0; index < lines.length; index++) {
    const element = lines[index];
    const [root, command, path] = element.split(" ");
    // start with the first cd

    if (root === "$" && command === "cd" && path !== ".." && path !== "/") {
      whereIAm.push(path);
    }
    if (root === "$" && command === "cd" && path === "..") {
      whereIAm.pop();
    }
    if (Number(root)) {
      // check extension of command
      const extension = command.split(".");
      let nameFile = command;
      if (extension.length === 1) {
        nameFile = command + ".exau";
      }
      threeMap.set(whereIAm.join("/") + "/" + nameFile, parseInt(root));
    }
    if (root === "dir") {
      threeMap.set(whereIAm.join("/") + "/" + command, 0);
    }
  }

  // sort threeMap by the number of backslash
  const sortedThreeMap = new Map(
    [...threeMap.entries()].sort((a, b) => {
      const splitA = a[0].split("/").length;
      const splitB = b[0].split("/").length;
      return splitB - splitA;
    })
  );

  sortedThreeMap.forEach((value, key) => {
    const splitKey = key.split("/");
    const parent = splitKey.slice(0, splitKey.length - 1).join("/");
    sortedThreeMap.set(parent, sortedThreeMap.get(parent) + value);
  });

  // order my map by value
  const sortedThreeMapByValue = new Map(
    [...sortedThreeMap.entries()].sort((a, b) => {
      return b[1] - a[1];
    })
  );

  // PART 1
  let sum = 0;
  sortedThreeMapByValue.forEach((value, key) => {
    // don't take the key if we have a extension
    const haveExtension = key.split(".").length > 1;
    if (key !== "/" && value !== 0 && value < 100000 && !haveExtension) {
      sum += value;
    }
  });

  console.log("sum", sum); // 95437

  // PART 2
  const totalMap = sortedThreeMapByValue.get("/");
  const sizeMapA = 70000000 - totalMap;
  const sizeMapB = 30000000 - sizeMapA;
  const values = [...sortedThreeMapByValue.values()];

  const indexA = values.filter((value) => value >= sizeMapB);

  console.log(indexA);
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
