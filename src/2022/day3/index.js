const fs = require('fs');

const splitIntoCompartments = (contents) => {
  const chars = contents.split('');

  return [chars.slice(0, chars.length / 2), chars.slice(chars.length / 2)];
};

const sum = (numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

const findShared = (compartmentA, compartmentB) => compartmentA.find((a) => compartmentB.find((b) => b === a));

const priority = (item) => (/[a-z]/.test(item) ? item.charCodeAt(0) - 97 + 1 : item.charCodeAt(0) - 65 + 27);

const badge = (rucksackA, rucksackB, rucksackC) =>
  rucksackA
    .find((a) => rucksackB.find((b) => a === b) && rucksackC.find((c) => a === c));

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
  console.log('Part1: sum of the priorities', result);
};

const partTwo = () => {
  const text = fs.readFileSync(`${__dirname}/input.txt`, 'utf-8');
  const priorities = text
    .split(/\n/)
    .filter((line) => line.trim().length)
    .map((line) => line.split(''))
    .reduce((groups, rucksack, index) => {
      const groupIndex = Math.floor(index / 3);
      // eslint-disable-next-line no-param-reassign
      groups[groupIndex] = !groups[groupIndex] ? [rucksack] : [...groups[groupIndex], rucksack];

      return groups;
    }, [])
    .map((group) => badge(...group))
    .map((item) => priority(item));

  const result = sum(priorities);

  // eslint-disable-next-line no-console
  console.log('Part2: sum of priority badges', result);
};

partOne();
partTwo();
