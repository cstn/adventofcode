const fs = require('fs');

const isCommand = (line) => line.startsWith('$');
const getCommand = (line) => line.replace('$ ', '').split(/\s/);

const isDir = (line) => line.startsWith('dir ');

const isFile = (line) => /^\d+\s.+$/.test(line);

const getFileSize = (line) => parseInt(line.split(/\s/)[0], 10);

const pwd = (path) => path.join('/').replace('//', '/');

const traverseLog = (lines) => {
  const currentDir = [];
  const sizes = {};

  // wanted to resolve this with immutable methods, but couldn't
  lines.forEach((line) => {
    if (isCommand(line) && getCommand(line)[0] === 'cd' && getCommand(line)[1] !== '..') {
      currentDir.push(getCommand(line)[1]);
      sizes[pwd(currentDir)] = 0;
    } else if (isCommand(line) && getCommand(line)[0] === 'cd' && getCommand(line)[1] === '..') {
      const dirSize = sizes[pwd(currentDir)];
      currentDir.pop();
      sizes[pwd(currentDir)] += dirSize;
    } else if (isDir(line)) {
      // does not count
    } else if (isFile(line)) {
      sizes[pwd(currentDir)] += getFileSize(line);
    }
  });

  // final root
  sizes['/'] += sizes[pwd(currentDir)];

  return sizes;
};

const main = (filename, maxSize) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  return Object.values(traverseLog(text.split(/\n/)))
    .filter((size) => size <= maxSize)
    .reduce((acc, curr) => acc + curr, 0);
};

console.log('Part 1:', main('input.txt', 100000));
