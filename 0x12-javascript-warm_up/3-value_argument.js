#!/usr/bin/node
/* A Script that prints the first argument passed to it */

const myArgs = process.argv.slice(2);

if (!myArgs[0]) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}
