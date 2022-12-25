const fs = require('fs');

const parseInput = (text) =>
  text
    .split(/\n\n/)
    .map((packages) => packages.split(/\n/))
    .map(([left, right]) => ({ left: JSON.parse(left), right: JSON.parse(right)}));

const compare = (a, b) => {
  // both values are integers
  if (typeof a === 'number' && typeof b === 'number') {
    if (a < b) {
      return -1;
    }
    if (a > b) {
      return 1;
    }

    return 0;
  }

  // both values are lists
  if (Array.isArray(a) && Array.isArray(b)) {
    const minLength = Math.min(a.length, b.length);

    for (let i = 0; i < minLength; i += 1) {
      const result = compare(a[i], b[i])
      if (result !== 0) {
        return result;
      }
    }

    if (a.length < b.length) {
      return -1;
    }
    if (a.length > b.length) {
      return +1;
    }

    return 0;
  }

  // exactly one value is an integer
  if (Array.isArray(a) && typeof b === 'number') {
    return compare(a, [b]);
  }
  if (typeof a === 'number' && Array.isArray(b)) {
    return compare([a], b);
  }

  return 0;
};

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const data = parseInput(text);

  return data
    .map(({ left, right}) => compare(left, right))
    .reduce((acc, curr, index) => curr < 0 ? acc + index + 1 : acc, 0);
};

console.log('Part 1:', partOne('input.txt'));
