#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

fs.writeFile(argv[2], argv[3], { encoding: 'utf-8' }, (err) => {
  if (err != null) {
    console.log(err);
  }
});
