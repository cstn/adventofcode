const fs = require('fs');

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

const applyMove = (stacks, { move, from, to }) => {
  const nextStacks = [...stacks];
  const fromIndex = from - 1;
  const toIndex = to - 1;

  const crates = stacks[fromIndex].slice(-move).reverse();
  nextStacks[fromIndex] = [...nextStacks[fromIndex].slice(0, nextStacks[fromIndex].length - move)];
  nextStacks[toIndex] = [...nextStacks[toIndex], ...crates];

  return nextStacks;
}

const run = (stacks, script) => {
  if (!script.length) {
    return stacks;
  }

  const [scriptLine, ...restScript] = script;
  const nextStacks = applyMove(stacks, scriptLine);

  return run(nextStacks, restScript);
};

const partOne = (filename = 'input.txt') => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');

  const { stacks, script } = parseInput(text);

  const finalStacks = run(stacks, script);

  const result = getTop(finalStacks).filter(Boolean).join('');

  // eslint-disable-next-line no-console
  console.log('Part 1: top of each stack', result);
};

partOne('input.txt');
