const fs = require('fs');

const contains = (a, b) => a.from <= b.from && a.to >= b.to || a.from >= b.from && a.to <= b.to;
const overlaps = (a, b) => contains(a, b) || a.from <= b.from && a.to >= b.from || a.from >= b.from && a.from <= b.to;

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const result = text
    .split(/\n/)
    .map((line) => line.split(','))
    .map(([a, b]) => [a.split('-'), b.split('-')])
    .map(([a, b]) => [
      { from: parseInt(a[0], 10), to: parseInt(a[1], 10)},
      { from: parseInt(b[0], 10), to: parseInt(b[1], 10)},
    ])
    .filter((pair) => contains(...pair));

  console.log('Part 1: assignment pairs fully containing the other', result.length)
};

const partTwo = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const result = text
    .split(/\n/)
    .map((line) => line.split(','))
    .map(([a, b]) => [a.split('-'), b.split('-')])
    .map(([a, b]) => [
      { from: parseInt(a[0], 10), to: parseInt(a[1], 10)},
      { from: parseInt(b[0], 10), to: parseInt(b[1], 10)},
    ])
    .filter((pair) => overlaps(...pair));

  console.log('Part 2: assignment pairs overlapping', result.length)
};

partOne('input.txt');
partTwo('input.txt');
