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

const runMotionScript = (motions, head, tail) => {
  let currentHead = head;
  let currentTail = tail;

  return motions.reduce((acc, curr) => {
    for (let stepCount = 0; stepCount < curr.steps; stepCount += 1) {
      // move head
      currentHead = move(currentHead, curr.direction);

      // move tail
      if (currentTail.y !== currentHead.y && Math.abs(currentTail.x - currentHead.x) === 2) {
        currentTail.y = currentHead.y;
      } else if (currentTail.x !== currentHead.x && Math.abs(currentTail.y - currentHead.y) === 2) {
        currentTail.x = currentHead.x;
      }

      if (currentTail.y === currentHead.y && Math.abs(currentTail.x - currentHead.x) === 2) {
        currentTail = move(currentTail, curr.direction);
      } else if (currentTail.x === currentHead.x && Math.abs(currentTail.y - currentHead.y) === 2) {
        currentTail = move(currentTail, curr.direction);
      }

      // remember current tail position
      // eslint-disable-next-line no-loop-func
      if (!acc.find((position) => position.x === currentTail.x && position.y === currentTail.y)) {
        // eslint-disable-next-line no-param-reassign
        acc = [...acc, { ...currentTail }];
      }
    }

    return acc;
  }, [tail]);
}

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const motions = parseMotionScript(text);

  const head = { x: 1, y: 1 };
  const tail = { x: 1, y: 1 };

  return runMotionScript(motions, head, tail).length;
};

console.log('Part 1:', partOne('input.txt'));
