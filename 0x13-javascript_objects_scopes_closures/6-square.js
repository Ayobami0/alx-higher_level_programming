#!/usr/bin/node
const ImportedSquare = require('./5-square');
class Square extends ImportedSquare {
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
