#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const f1 = argv[2];
const f2 = argv[3];
const dest = argv[4];

fs.readFile(f1, 'utf8', (err, f1data) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(f2, 'utf8', (err, f2data) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(dest, `${f1data}${f2data}`, err => {
      if (err) {
        console.error(err);
      }
    });
  });
});
