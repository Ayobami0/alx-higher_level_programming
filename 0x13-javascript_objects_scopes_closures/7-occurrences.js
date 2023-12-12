#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(e => {
    count += e === searchElement ? 1 : 0;
  });
  return count;
};
