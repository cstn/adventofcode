const fs = require('fs');

const readInput = (filename) => fs.readFileSync(`${__dirname}/${filename}`, 'utf8');

const splitIntoBlocks = (text) => text.split(/\s\r?\n/).map((block) => block.split(/\r?\n/).map((token) => parseInt(token, 10)));

const sum = (numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

const max = (numbers) => numbers.reduce((acc, curr) => curr > acc ? curr : acc, 0);

const main = () => {
    const text = readInput('input');
    const calories = splitIntoBlocks(text);

    console.log('Maximum calories:', max(calories.map(sum)));
};

main();