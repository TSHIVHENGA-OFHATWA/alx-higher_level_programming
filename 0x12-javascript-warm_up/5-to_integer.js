#!/usr/bin/node
const arg = process.argv[2];
if (/^-?\d+$/.test(arg)) {
  const number = parseInt(arg, 10);
  console.log(`My number: ${number}`);
} else {
  console.log("Not a number");
}
