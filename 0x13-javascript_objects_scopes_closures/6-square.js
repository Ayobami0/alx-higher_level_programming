#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0)) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
class SquareBase extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

class Square extends SquareBase {
  charPrint (c) {
    let printSymbol = 'X';
    if (c !== undefined) {
      printSymbol = c;
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += printSymbol;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
