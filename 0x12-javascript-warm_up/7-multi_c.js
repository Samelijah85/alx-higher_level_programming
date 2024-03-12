#!/usr/bin/node
const arg = process.argv[2];

if (arg === undefined || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(arg);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
