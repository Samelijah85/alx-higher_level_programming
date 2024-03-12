#!/usr/bin/node
const { argv } = require('node:process');

const arg = argv[2];

if (!isNaN(arg)) {
  console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
