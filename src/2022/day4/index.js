const fs = require('fs');

const includes = (a, b) => a.from <= b.from && a.to >= b.to || a.from >= b.from && a.to <= b.to;

const partOne = (filename = 'input.txt') => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const result = text
    .split(/\n/)
    .map((line) => line.split(','))
    .map(([a, b]) => [a.split('-'), b.split('-')])
    .map(([a, b]) => [
      { from: parseInt(a[0], 10), to: parseInt(a[1], 10)},
      { from: parseInt(b[0], 10), to: parseInt(b[1], 10)},
    ])
    .filter((pair) => includes(...pair));

  // eslint-disable-next-line no-console
  console.log('Part 1: assignment pairs fully containing the other', result.length)
};

partOne('input.txt');
