#!/usr/bin/node

const Rectangles = require('./4-rectangle');

class Square extends Rectangles {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
