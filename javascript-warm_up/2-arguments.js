#!/usr/bin/node

const processs = require('process');

const argsCount = processs.argv.length;

if (argsCount === 2) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
