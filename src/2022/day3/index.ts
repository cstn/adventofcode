import * as fs from 'fs';

const splitIntoCompartments = (contents: string): string[][] => {
  const chars = contents.split('');

  return [chars.slice(0, chars.length / 2), chars.slice(chars.length / 2)];
};

const sum = (numbers: number[]): number => numbers.reduce((acc, curr) => acc + curr, 0);

const findShared = (compartmentA: string[], compartmentB: string[]): string => compartmentA.find((a) => compartmentB.find((b) => b === a));

const priority = (item: string): number => (/[a-z]/.test(item) ? item.charCodeAt(0) - 97 + 1 : item.charCodeAt(0) - 65 + 27);

const badge = (rucksackA: string[], rucksackB: string[], rucksackC: string[]) =>
  rucksackA
    .find((a) => rucksackB.find((b) => a === b) && rucksackC.find((c) => a === c));

const partOne = (filename: string) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf8');
  const priorities = text
    .split(/\n/)
    .map(splitIntoCompartments)
    .map((rucksack: string[][]) => findShared(rucksack[0], rucksack[1])?.[0])
    .map((item) => priority(item));

  return sum(priorities);
};

const partTwo = (filename: string) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf8');
  const priorities = text
    .split(/\n/)
    .map((line) => line.split(''))
    .reduce((groups: string[][], rucksack: string[], index) => {
      const groupIndex = Math.floor(index / 3);
      // eslint-disable-next-line no-param-reassign
      groups[groupIndex] = !groups[groupIndex] ? [rucksack] : [...groups[groupIndex], rucksack];

      return groups;
    }, [])
    .map((group) => badge(group[0], group[1], group[2]))
    .map((item) => priority(item));

  return sum(priorities);


};

console.log('Part1: sum of the priorities', partOne('input.txt'));
console.log('Part2: sum of priority badges', partTwo('input.txt'));
