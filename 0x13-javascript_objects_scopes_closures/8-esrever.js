#!/usr/bin/node

exports.esrever = function (list) {
  const new_arr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    new_arr.push(list[i]);
  }
  return new_arr;
};
