#!/usr/bin/node
function add (a, b) {
    const num1 = parseInt(a);
    const num2 = parseInt(b);
    if (isNaN(num1) || isNaN(num2)) {
        console.log(NaN);
    } else {
        console.log(num1 + num2);
    }
}
const args = process.argv.slice(2);
add(args[0], args[1]);
