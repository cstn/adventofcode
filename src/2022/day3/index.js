const fs = require('fs');

const splitIntoCompartments = (contents) => {
  const chars = contents.split('');

  return [chars.slice(0, chars.length / 2), chars.slice(chars.length / 2)];
};

const sum = (numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

const findShared = (compartmentA, compartmentB) => compartmentA.filter((itemA) => compartmentB.find((itemB) => itemB === itemA));

const priority = (item) => (/[a-z]/.test(item) ? item.charCodeAt(0) - 97 + 1 : item.charCodeAt(0) - 65 + 27);

const partOne = () => {
  const text = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8');
  const priorities = text
    .split(/\n/)
    .filter((line) => line.trim().length)
    .map(splitIntoCompartments)
    .map((rucksack) => findShared(...rucksack)?.[0])
    .map((item) => priority(item));

  const result = sum(priorities);

  // eslint-disable-next-line no-console
  console.log('sum of the priorities', result);
};

partOne();
