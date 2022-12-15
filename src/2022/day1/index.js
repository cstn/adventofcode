const fs = require('fs');

const splitIntoBlocks = (text) => text.split(/\s\r?\n/).map((block) => block.split(/\r?\n/).map((token) => parseInt(token, 10)));

const sum = (numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

const max = (numbers) => numbers.reduce((acc, curr) => (curr > acc ? curr : acc), 0);

const top = (numbers, amount) => [...numbers].sort((a, b) => b - a).slice(0, amount);

const partOne = () => {
  const text = fs.readFileSync(`${__dirname}/input.txt`, 'utf8');
  const calories = splitIntoBlocks(text);

  console.log('Maximum calories:', max(calories.map(sum)));
};

const partTwo = () => {
  const text = fs.readFileSync(`${__dirname}/input.txt`, 'utf8');
  const calories = splitIntoBlocks(text);

  const topCalories = top(calories.map(sum), 3);

  console.log('Top calories:', topCalories, `sum = ${sum(topCalories)}`);
};

partOne();
partTwo();
