#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      let toPrint = '';
      for (let column = 0; column < this.width; column++) {
        toPrint += c;
      }
      console.log(toPrint);
    }
  }
}
module.exports = Square;
