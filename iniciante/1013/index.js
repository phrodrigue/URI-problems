var input = require('fs').readFileSync('./input.txt', 'utf8');
var lines = input.split('\n');
var list = lines[0].split(" ").map(x => parseInt(x))
var [a, b, c] = list

var maiorAB = (a + b + Math.abs(a - b)) / 2
var maiorABC = (maiorAB + c + Math.abs(maiorAB - c)) / 2

console.log(maiorABC, "eh o maior")