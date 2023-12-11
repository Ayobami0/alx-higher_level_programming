#!/usr/bin/node

const argv = process.argv;

const num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let square = '';
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
