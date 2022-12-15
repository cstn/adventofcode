const fs = require('fs');

const Mode = {
  Single: 'single',     // CrateMover 9000
  Multiple: 'multiple', // CrateMover 9001
};

const parseMove = (line) => {
  const tokens = line.split(/\s/);

  return {
    move: parseInt(tokens[1], 10),
    from: parseInt(tokens[3], 10),
    to: parseInt(tokens[5], 10),
  };
};

const parseInput = (text) => {
  const lines = text.split(/\n/);
  const separatorIndex = lines.findIndex((line) => !line);

  const stackLines = lines.slice(0, separatorIndex - 1);
  const scriptLines = lines.slice(separatorIndex + 1);

  const stackLabels = lines[separatorIndex - 1].split(/\s*/).filter(Boolean);
  const numberOfStacks = stackLabels.length;

  const stacks = stackLines
    .reduce((acc, curr) => {
      for (let i = 0; i < numberOfStacks; i += 1) {
        const crate = curr[i * 4 + 1];
        if (crate && crate !== ' ') {
          acc[i] = [crate, ...acc[i]];
        }
      }

      return acc;
    }, new Array(numberOfStacks).fill([]));

  const script = scriptLines.map(parseMove);

  return {
    stacks,
    script,
  };
};

const getTop = (stacks) => stacks.map((stack) => stack.length ? stack[stack.length - 1] : '');

const applyMove = (mode) => (stacks, { move, from, to }) => {
  const nextStacks = [...stacks];
  const fromIndex = from - 1;
  const toIndex = to - 1;

  const crates = mode === Mode.Multiple ? stacks[fromIndex].slice(-move) : stacks[fromIndex].slice(-move).reverse();
  nextStacks[fromIndex] = [...nextStacks[fromIndex].slice(0, nextStacks[fromIndex].length - move)];
  nextStacks[toIndex] = [...nextStacks[toIndex], ...crates];

  return nextStacks;
}

const run = (stacks, script, applyFunction) => {
  if (!script.length) {
    return stacks;
  }

  const [scriptLine, ...restScript] = script;
  const nextStacks = applyFunction(stacks, scriptLine);

  return run(nextStacks, restScript, applyFunction);
};

const main = (filename, mode) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const { stacks, script } = parseInput(text);

  const finalStacks = run(stacks, script, applyMove(mode));

  return getTop(finalStacks).filter(Boolean).join('');
};

console.log('Part 1: top of each stack with CateMover 9000', main('input.txt', Mode.Single));
console.log('Part 2: top of each stack with CrateMover 9001', main('input.txt', Mode.Multiple));
