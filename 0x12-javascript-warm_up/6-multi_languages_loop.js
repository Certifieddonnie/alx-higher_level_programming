#!/usr/bin/node
/* A Script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop */

const myLangs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;

while (i < myLangs.length) {
  console.log(myLangs[i]);
  i++;
}
