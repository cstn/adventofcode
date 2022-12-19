const fs = require('fs');

const parseInstructions = (text) =>
  text
    .split(/\n/)
    .map((line) => {
      const tokens = line.split(/\s/);
      return {
        command: tokens[0],
        param: tokens[1] ? parseInt(tokens[1], 10) : undefined,
      };
    });

const runInstructions = (instructions, initialState) => {
  let state = initialState;
  let signalStrength = 0;
  let cycle = 0;

  while (instructions.length) {
    cycle += 1;
    const instruction = instructions.shift();

    if (cycle % 40 === 20) {
      signalStrength += cycle * state;
      console.log(`cycle ${cycle}: state =`, state)
      console.log(`cycle ${cycle}: signal=`, cycle * state)
    }

    if (instruction.command === 'add') {
      state += instruction.param;
    } else if (instruction.command === 'addx') {
      instructions.unshift({ command: 'add', param: instruction.param });
    }
  }

  return signalStrength;
};

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const instructions = parseInstructions(text);

  return runInstructions(instructions, 1);
};

console.log('Part 1:', partOne('input.txt'));
