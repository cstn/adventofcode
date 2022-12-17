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

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const grid = scanGrid(text);

  const visibleMap = grid.map((row, rowIndex) =>
    getRow(grid, rowIndex)
      .map((col, colIndex) => isVisible(grid, rowIndex, colIndex))
  );

  return visibleMap.reduce((acc, curr) => acc + curr.filter(Boolean).length, 0);
};

console.log('Part 1:', partOne('input.txt'));
