#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], { flag: 'r', encoding: 'utf-8' }, (err, data) => {
  if (err != null) {
    console.log(err);
  }
  console.log(data);
});
