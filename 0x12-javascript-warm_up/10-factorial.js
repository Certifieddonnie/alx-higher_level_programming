#!/usr/bin/node
/* A Script that computes and prints a factorial */

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
const res = factorial(myNum);
console.log(res);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
