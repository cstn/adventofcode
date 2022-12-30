const fs = require('fs');

const walk = (directions, startLevel = 0) =>
  directions.reduce((acc, curr) => curr === '(' ? acc + 1 : acc - 1, startLevel);

const goToBasement = (directions, startLevel = 0) => {
  let level = startLevel;

  return directions.findIndex((direction) => {
    level = direction === '(' ? level + 1 : level - 1;

    return level < 0;
  }) + 1;
}

const partOne = (filename) => {
  const input = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8').split('');

  return walk(input);
}

const partTwo = (filename) => {
  const input = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8').split('');

  return goToBasement(input);
}

console.log('Part 1:', partOne('input.txt'));
console.log('Part 2:', partTwo('input.txt'));
