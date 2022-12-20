#!/usr/bin/node
/* A Script that prints x times “C is fun”, Where x is the first argument of the script */

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
let i = 0;

if (!myNum) {
  console.log('Missing number of occurrences');
} else {
  while (i < myNum) {
    console.log('C is fun');
    i++;
  }
}
