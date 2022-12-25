const fs = require('fs');

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
  const data = text
    .split(/\n\n/)
    .map((packages) => packages.split(/\n/))
    .map(([left, right]) => ({ left: JSON.parse(left), right: JSON.parse(right) }));

  return data
    .map(({ left, right }) => compare(left, right))
    .reduce((acc, curr, index) => curr < 0 ? acc + index + 1 : acc, 0);
};

const partTwo = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const data = text.split(/\n/).filter(Boolean).map((line) => JSON.parse(line));

  const sortedData = [...data, [[2]], [[6]]].sort(compare);
  const firstDividerIndex = sortedData.findIndex((value) => Array.isArray(value) && value.length === 1 && Array.isArray(value[0]) && value[0].length === 1 && value[0][0] === 2);
  const secondDividerIndex = sortedData.findIndex((value) => Array.isArray(value) && value.length === 1 && Array.isArray(value[0]) && value[0].length === 1 && value[0][0] === 6);

  return (firstDividerIndex + 1) * (secondDividerIndex + 1);
};

console.log('Part 1:', partOne('input.txt'));
console.log('Part 2:', partTwo('input.txt'));
