#!/usr/bin/node
/* A Script that prints a message depending of the number of arguments passed */

const myArgs = process.argv.slice(2);
const len = myArgs.length;

if (len < 1) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
