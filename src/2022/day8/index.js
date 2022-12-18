const fs = require('fs');

const scanGrid = (text) =>
  text
    .split(/\n/)
    .map((row) => row.split('').map((tree) => parseInt(tree, 10)));

const getRow = (grid, rowIndex) => grid[rowIndex];
const getCol = (grid, colIndex) => grid.map((row) => row[colIndex]);

const isOnTheEdge = (grid, rowIndex, colIndex) =>
  rowIndex === 0 || colIndex === 0 || colIndex === getRow(grid, rowIndex).length - 1 || rowIndex === grid.length - 1;

const isVisible = (grid, rowIndex, colIndex) => {
  if (isOnTheEdge(grid, rowIndex, colIndex)) {
    return true;
  }

  const row = getRow(grid, rowIndex);
  const col = getCol(grid, colIndex);
  const height = grid[rowIndex][colIndex];

  const isVisibleFromLeft = row.slice(0, colIndex).every((tree) => tree < height);
  const isVisibleFromRight = row.slice(colIndex + 1, row.length + 1).every((tree) => tree < height);
  const isVisibleFromTop = col.slice(0, rowIndex).every((tree) => tree < height);
  const isVisibleFromBottom = col.slice(rowIndex + 1, col.length + 1).every((tree) => tree < height);

  return isVisibleFromLeft || isVisibleFromRight || isVisibleFromTop || isVisibleFromBottom;
};

const countToLargerTree = (heights, tree) => {
  const largerIndex = heights.findIndex((height) => height >= tree);

  return largerIndex === -1 ? heights.length : largerIndex + 1;
}

const scenicScore = (grid, rowIndex, colIndex) => {
  const row = getRow(grid, rowIndex);
  const col = getCol(grid, colIndex);
  const height = grid[rowIndex][colIndex];

  const leftTreesInView = colIndex === 0
    ? 0
    : countToLargerTree(row.slice(0, colIndex).reverse(), height);
  const rightTreesInView = colIndex === col.length - 1 || colIndex === col.length - 1
    ? 0
    : countToLargerTree(row.slice(colIndex + 1, row.length + 1), height);
  const topTreesInView = rowIndex === 0
    ? 0
    : countToLargerTree(col.slice(0, rowIndex).reverse(), height);
  const bottomTreesInView = rowIndex === grid.length - 1 || colIndex === col.length - 1
    ? 0
    : countToLargerTree(col.slice(rowIndex + 1, col.length + 1), height);

  return leftTreesInView * rightTreesInView * topTreesInView * bottomTreesInView;
};

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const grid = scanGrid(text);

  const visibleMap = grid.map((row, rowIndex) =>
    getRow(grid, rowIndex)
      .map((col, colIndex) => isVisible(grid, rowIndex, colIndex)),
  );

  return visibleMap.reduce((acc, row) => acc + row.filter(Boolean).length, 0);
};

const partTwo = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const grid = scanGrid(text);

  const scoreMap = grid.map((row, rowIndex) =>
    getRow(grid, rowIndex)
      .map((col, colIndex) => scenicScore(grid, rowIndex, colIndex)),
  );

  return scoreMap.reduce((acc, row) => {
    const maxInRow = Math.max(...row);

    return maxInRow > acc ? maxInRow : acc;
  }, 0);
};

console.log('Part 1:', partOne('input.txt'));
console.log('Part 2:', partTwo('input.txt'));
