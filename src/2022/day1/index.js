const { readFileContent } = require('../../utils/file');

const splitIntoBlocks = (text) => text.split(/\s\r?\n/).map((block) => block.split(/\r?\n/).map((token) => parseInt(token, 10)));

const sum = (numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

const max = (numbers) => numbers.reduce((acc, curr) => curr > acc ? curr : acc, 0);

const main = () => {
    const text = readFileContent(`${__dirname}/input`);
    const calories = splitIntoBlocks(text);

    console.log('Maximum calories:', max(calories.map(sum)));
};

main();