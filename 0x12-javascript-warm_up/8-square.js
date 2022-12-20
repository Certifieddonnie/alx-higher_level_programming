#!/usr/bin/node
/* A Script that prints a square, Where the first argument is the size of square. */

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
let i = 0;
const word = 'X';

if (!myNum) {
  console.log('Missing size');
} else {
  while (i < myNum) {
    console.log(word.repeat(myNum));
    i++;
  }
}
