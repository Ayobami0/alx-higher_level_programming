#!/usr/bin/node
exports.logMe = function (item) {
  let count = 0;

  return function () {
    console.log(`${count}: ${item}`);
    count++;
  };
};
