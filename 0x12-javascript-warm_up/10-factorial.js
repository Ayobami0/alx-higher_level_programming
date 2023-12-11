#!/usr/bin/node

const argv = process.argv;

const a = Number(argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(a));
