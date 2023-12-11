#!/usr/bin/node
const { argv } = require('node:process');

const first = argv[2];
const second = argv[3];
const sentence = first + ' is ' + second;
console.log(sentence);
