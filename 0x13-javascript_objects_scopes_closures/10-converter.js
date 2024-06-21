#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      return num < 10 ? num.toString() : String.fromCharCode(87 + num);
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base).toString();
    }
  };
};
