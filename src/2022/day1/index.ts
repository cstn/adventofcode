import * as fs from 'fs';

const splitIntoBlocks = (text: string) => text.split(/\s\r?\n/).map((block) => block.split(/\r?\n/).map((token) => parseInt(token, 10)));

const sum = (numbers: number[]) => numbers.reduce((acc, curr) => acc + curr, 0);

const max = (numbers: number[]) => numbers.reduce((acc, curr) => (curr > acc ? curr : acc), 0);

const top = (numbers: number[], amount: number) => [...numbers].sort((a, b) => b - a).slice(0, amount);

const partOne = (filename: string) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf8');
  const calories = splitIntoBlocks(text);

  return max(calories.map(sum));
};

const partTwo = (filename: string) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf8');
  const calories = splitIntoBlocks(text);

  const topCalories = top(calories.map(sum), 3);

  return {
    top: topCalories,
    sum: sum(topCalories)
  };
};

console.log('Part 1: Maximum calories:', partOne('input.txt'));
console.log('Part 2: Maximum calories:', partTwo('input.txt'));
