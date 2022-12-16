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

const partOne = (filename, maxSize) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  return Object.values(traverseLog(text.split(/\n/)))
    .filter((size) => size <= maxSize)
    .reduce((acc, curr) => acc + curr, 0);
};

const partTwo = (filename, totalSpace, updateSpace) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  // does not work, do not know why
  const sizes = traverseLog(text.split(/\n/));
  const unusedSpace = totalSpace - sizes['/'];
  const requiredSpace = updateSpace - unusedSpace;

  return Object.values(sizes)
    .filter((size) => size >= requiredSpace)
    .sort((a, b) => a - b)[0];
};

console.log('Part 1:', partOne('input.txt', 100000));
console.log('Part 2:', partTwo('input.txt', 70000000, 30000000));
