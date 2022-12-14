const fs = require('fs');

const splitIntoBlocks = (text) => text.split(/\s\r?\n/).map((block) => block.split(/\r?\n/).map((token) => parseInt(token, 10)));

const sum = (numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

const max = (numbers) => numbers.reduce((acc, curr) => (curr > acc ? curr : acc), 0);

const partOne = () => {
  const text = fs.readFileSync(`${__dirname}/input.txt`, 'utf8');
  const calories = splitIntoBlocks(text);

  // eslint-disable-next-line no-console
  console.log('Maximum calories:', max(calories.map(sum)));
};

partOne();
