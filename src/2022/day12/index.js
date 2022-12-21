const fs = require('fs');

const parseInput = (text) => text.split(/\n/).map((line) => line.split(''));

const findSymbol = (grid, symbol) => {
  const rowIndex = grid.findIndex((line) => line.find((char) => char === symbol));
  if (rowIndex === -1) {
    return null;
  }

  const colIndex = grid[rowIndex].findIndex((char) => char === symbol);

  return {
    x: colIndex,
    y: rowIndex,
  };
}

const getLevel = (grid, x, y) => grid[y][x].charCodeAt(0) - 96;

const detectPossibleDirections = (grid, { x, y }) => {
  const currentLevel = getLevel(grid, x, y);

  const directions = [];
  if (x >= 1 && (currentLevel === getLevel(grid, x - 1, y) || currentLevel === getLevel(grid, x - 1, y) - 1)) {
    directions.push('left');
  }
  if (y >= 1 && (currentLevel === getLevel(grid, x, y - 1) || currentLevel === getLevel(grid, x, y - 1) - 1)) {
    directions.push('up');
  }
  if (x < grid[0].length - 1 && (currentLevel === getLevel(grid, x + 1, y) || currentLevel === getLevel(grid, x + 1, y) - 1)) {
    directions.push('right');
  }
  if (y < grid.length - 1 && (currentLevel === getLevel(grid, x, y +1 ) || currentLevel === getLevel(grid, x, y + 1) - 1)) {
    directions.push('down');
  }

  return directions;
}

const step = (grid, { x, y }, direction) => {
  switch (direction) {
    case 'left':
      return {
        x: x - 1,
        y,
      };
    case 'right':
      return {
        x: x + 1,
        y,
      }
    case 'up':
      return {
        x,
        y: y - 1,
      };
    case 'down':
      return {
        x,
        y: y + 1,
      };
    default:
      return {
        x,
        y,
      };
  }
};

const seek = (grid, start, target, visited, limit) => {
  if (limit === 0) {
    // too expensive
    return 100000;
  }

  if (start.x === target.x && start.y === target.y) {
    // found
    return 0;
  }

  return detectPossibleDirections(grid, start)
    .map((direction) => step(grid, start, direction))
    .filter(({ x, y }) => !visited.find((v) => v.x === x && v.y === y))
    .map((nextPosition) => 1 + seek(grid, nextPosition, target, [...visited, nextPosition], limit - 1))
    .sort((a, b) => a - b)[0];
}

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const grid = parseInput(text);
  const start = findSymbol(grid, 'S');
  const target = findSymbol(grid, 'E');
  const limit = grid.length * grid[0].length;
  grid[start.y][start.x] = 'a';
  grid[target.y][target.x] = 'z';

  console.log('Start', start);
  console.log('Target', target);

  return seek(grid, start, target, [start], limit);
};

console.log('Part 1:', partOne('input.txt'));
