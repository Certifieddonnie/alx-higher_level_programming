#!/usr/bin/node
/* A Script that searches the second biggest integer in the list of arguments. */

const myArgs = process.argv.slice(2);
const len = myArgs.length;

if (len <= 3) {
  console.log(0);
}
secondhigh(myArgs, len);

function secondhigh (arr, size) {
  let i;

  // sort the array.
  arr.sort();
  // start from second last element
  // as the largest element is at last.
  for (i = size - 2; i >= 0; i--) {
    // if the element is not
    // equal to largest element
    if (arr[i] !== arr[size - 1]) {
      console.log(arr[i]);
      return;
    }
  }
}
