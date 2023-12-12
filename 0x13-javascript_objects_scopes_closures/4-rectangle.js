#!/usr/bin/node
class Rectangle {
  width;
  height;

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
module.exports = Rectangle;
