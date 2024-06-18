#!/usr/bin/env node
const args = process.argv.slice(2).map(Number);
const secondBiggest = (arr) => {
  if (arr.length <= 1) return 0;

  let max = -Infinity; let secondMax = -Infinity;

  for (const num of arr) {
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  return secondMax;
};
console.log(secondBiggest(args));

