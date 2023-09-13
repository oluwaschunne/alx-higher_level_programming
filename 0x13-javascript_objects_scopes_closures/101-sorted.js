#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
const keys = [];
const vals = new Set();

for (const key in dict) {
  keys.push([key, dict[key]]);
  vals.add(dict[key]);
}

for (const val of vals) {
  const first = [];
  for (let i = 0; i < keys.length; i++) {
    if (val === keys[i][1]) {
      first.push(keys[i][0]);
    }
  }
  newDict[val] = first;
}
console.log(newDict);
