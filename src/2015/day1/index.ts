import * as fs from 'fs';

const walk = (directions: string[], startLevel = 0): number =>
  directions.reduce((acc, curr) => curr === '(' ? acc + 1 : acc - 1, startLevel);

const goToBasement = (directions: string[], startLevel = 0): number => {
  let level = startLevel;

  return directions.findIndex((direction: string) => {
    level = direction === '(' ? level + 1 : level - 1;

    return level < 0;
  }) + 1;
}

const partOne = (filename: string) => {
  const input = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8').split('');

  return walk(input);
}

const partTwo = (filename: string) => {
  const input = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8').split('');

  return goToBasement(input);
}

console.log('Part 1:', partOne('input.txt'));
console.log('Part 2:', partTwo('input.txt'));
