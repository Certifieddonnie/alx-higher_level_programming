#!/usr/bin/node
/* A Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer */

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);

if (!myNum) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
