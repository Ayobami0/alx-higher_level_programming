#!/usr/bin/node

const fs = require('node:fs');
const { argv } = require('node:process');

try {
  const content = fs.readFileSync(argv[2], { flag: 'r', encoding: 'utf-8' });
  console.log(content);
} catch (error) {
  console.log(error);
}
