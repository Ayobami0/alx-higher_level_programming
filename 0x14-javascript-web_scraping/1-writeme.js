#!/usr/bin/node

const fs = require('node:fs');
const { argv } = require('node:process');

try {
  fs.writeFileSync(argv[2], argv[3], { encoding: 'utf-8' });
} catch (error) {
  console.log(error);
}
