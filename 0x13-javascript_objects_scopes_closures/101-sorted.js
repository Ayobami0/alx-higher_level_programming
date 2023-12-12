#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

Object.keys(dict).forEach((e) => {
  if (newDict[dict[e]] === undefined) {
    newDict[dict[e]] = [];
  }
  newDict[dict[e]].push(e);
});

console.log(newDict);
