#!/usr/bin/node
/* A Script that prints the addition of 2 integers */

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
const myNum2 = parseInt(myArgs[1]);
const res = add(myNum, myNum2);
console.log(res);

function add (a, b) {
  return a + b;
  // Add Function
}
