#!/usr/bin/node
function secondBiggest(args) {
  const nums = args.map(Number);
  if (nums.length === 0) return 0;
  if (nums.length === 1) return 0;
  const max = Math.max(...nums);
  const secondMax = Math.max(...nums.filter(n => n < max));
  return secondMax;
}
