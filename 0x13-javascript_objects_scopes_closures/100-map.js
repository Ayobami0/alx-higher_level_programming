#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((item, idx) => {
  return item * idx;
});

console.log(list);
console.log(newList);
