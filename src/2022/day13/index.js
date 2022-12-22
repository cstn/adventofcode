const fs = require('fs');

const parseInput = (text) =>
  text
    .split(/\n\n/)
    .map((packages) => packages.split(/\n/))
    .map(([left, right]) => ([JSON.parse(left), JSON.parse(right)]));

const compare = ([a, b]) => {
  const firstA = a[0];
  const firstB = b[0];
  // both values are integers
  if (typeof firstA === 'number' && typeof firstB === 'number') {
    if (firstA < firstB) {
      return true;
    }
    if (firstA > firstB) {
      return false
    }

    return compare([a.slice(1), b.slice(1)]);
  }

  // both values are lists
  if (Array.isArray(firstA) && Array.isArray(firstB)) {
    const minLength = Math.min(firstA.length, firstB.length);

    for (let i = 0; i < minLength; i += 1) {
      if (!compare([firstA[i], firstB[i]])) {
        return false;
      }
    }

    if (firstA.length < firstB.length) {
      return true;
    }
    if (firstA.length > firstB.length) {
      return false;
    }

    return compare([firstA.slice(1), firstB.slice(1)]);
  }

  // exactly one value is an integer
  if (Array.isArray(firstA) && typeof firstB === 'number') {
    return compare([firstA, [firstB]]);
  }
  if (typeof firstA === 'number' && Array.isArray(firstB)) {
    return compare([[firstA], firstB]);
  }

  return false;
};

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const data = parseInput(text);
  return data.map(compare).reduce((acc, curr, index) => curr ? acc + index + 1 : acc, 0);
};

console.log('Part 1:', partOne('sample.txt'));
