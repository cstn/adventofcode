const fs = require('fs');

const hasUniqueCharacters = (text) => text.length === (new Set(text)).size;

const findMarkerIndex = (buffer, markerSize) =>
  buffer
    .split('')
    .slice(0, buffer.length - markerSize)
    .findIndex((_, i) => hasUniqueCharacters(buffer.substring(i, i + markerSize)));

const main = (filename, markerSize) => {
  const buffer = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  return findMarkerIndex(buffer, markerSize) + markerSize;
};

console.log('Part 1: first marker completed after character', main('input.txt', 4));
console.log('Part 2: first marker completed after character', main('input.txt', 14));
