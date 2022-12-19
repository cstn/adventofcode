/* eslint-disable no-param-reassign */
const fs = require('fs');

const parseMotionScript = (text) => text.split(/\n/).map((line) => {
  const [direction, steps] = line.split(' ');
  return {
    direction,
    steps: parseInt(steps, 10),
  };
});

const move = (position, direction) => {
  if (direction === 'R') {
    return {
      x: position.x + 1,
      y: position.y,
    };
  }

  if (direction === 'L') {
    return {
      x: position.x - 1,
      y: position.y,
    };
  }

  if (direction === 'U') {
    return {
      x: position.x,
      y: position.y + 1,
    };
  }

  if (direction === 'D') {
    return {
      x: position.x,
      y: position.y - 1,
    };
  }

  return position;
}

const runMotionScript = (motions, head, tails) => {
  let currentHead = head;

  return motions.reduce((acc, curr) => {
    for (let stepCount = 0; stepCount < curr.steps; stepCount += 1) {
      // move head
      currentHead = move(currentHead, curr.direction);

      for (let tailCount = 0; tailCount < tails.length; tailCount += 1) {
        const predecessor = tailCount === 0 ? currentHead : tails[tailCount - 1];

        // move tail
        if (tails[tailCount].y !== predecessor.y && Math.abs(tails[tailCount].x - predecessor.x) === 2) {
          tails[tailCount].y = predecessor.y;
        } else if (tails[tailCount].x !== predecessor.x && Math.abs(tails[tailCount].y - predecessor.y) === 2) {
          tails[tailCount].x = predecessor.x;
        }

        if (tails[tailCount].y === predecessor.y && Math.abs(tails[tailCount].x - predecessor.x) === 2) {
          tails[tailCount] = move(tails[tailCount], curr.direction);
        } else if (tails[tailCount].x === predecessor.x && Math.abs(tails[tailCount].y - predecessor.y) === 2) {
          tails[tailCount] = move(tails[tailCount], curr.direction);
        }

        // remember current tail position
        // eslint-disable-next-line no-loop-func
        if (!acc.find((position) => position.x === tails[tailCount].x && position.y === tails[tailCount].y)) {
          // eslint-disable-next-line no-param-reassign
          acc = [...acc, { ...tails[tailCount] }];
        }
      }
    }

    return acc;
  }, [tails[0]]);
}

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const motions = parseMotionScript(text);

  const head = { x: 1, y: 1 };
  const tails = [{ x: 1, y: 1 }];

  return runMotionScript(motions, head, tails).length;
};

const partTwo = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const motions = parseMotionScript(text);

  const head = { x: 1, y: 1 };
  const tails = new Array(9).fill({ x: 1, y: 1 });

  return runMotionScript(motions, head, tails).length;
};

console.log('Part 1:', partOne('input.txt'));
console.log('Part 2:', partTwo('input.txt'));
