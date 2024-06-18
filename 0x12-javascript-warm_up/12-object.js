#!/usr/bin/node
function updateArgs(args) {
  const nums = args.map(Number);
  const index = nums.indexOf(12);
  if (index > -1) {
    nums[index] = 89;
  }
  return nums;
}
const args = process.argv.slice(2);
console.log(updateArgs(args));
