#!/usr/bin/node

const argv = process.argv;
function compare (a, b) {
  return b - a;
}

if (argv.length < 4) {
  console.log(0);
} else {
  const arr = argv.slice(2);
  arr.sort(compare);
  console.log(arr[1]);
}
