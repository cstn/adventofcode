const fs = require('fs');

const REGEX = /Monkey (\d+):\n\s+Starting items: (.+)\n\s+Operation: new = old ([*\-+/]) (\w+)\n\s+Test: divisible by (\d+)\n\s+If (\w+): throw to monkey (\d+)\n\s+If (\w+): throw to monkey (\d+)/;

const parseInput = (text) => {
  const blocks = text.split(/\n\n/);

  return blocks.reduce((acc, block) => {
    const matches = block.match(REGEX);

    if (!matches) {
      return acc;
    }

    return [
      ...acc,
      {
        monkey: parseInt(matches[1], 10),
        inspections: 0,
        items: matches[2].split(',').map((token) => token.trim()).map((token) => BigInt(parseInt(token, 10))),
        operation: (value) => {
          const num = matches[4] === 'old' ? value : parseInt(matches[4], 10);
          switch (matches[3]) {
            case '+':
              return value + BigInt(num);
            case '-':
              return value - BigInt(num);
            case '*':
              return value * BigInt(num);
            case '/':
              return value / BigInt(num);
            default:
              return value;
          }
        },
        test: {
          divisible: BigInt(parseInt(matches[5], 10)),
          [matches[6] === 'true' ? 'yes' : 'no']: parseInt(matches[7], 10),
          [matches[8] === 'true' ? 'yes' : 'no']: parseInt(matches[9], 10),
        },
      }];
  }, []);
};

const run = (monkeys, rounds, worryDivider) => {
  for (let roundIndex = 0; roundIndex < rounds; roundIndex += 1) {
    monkeys.forEach((monkey) => {
      monkey.items.forEach((item) => {
        // eslint-disable-next-line no-param-reassign
        monkey.inspections += 1;

        const worryLevel = monkey.operation(item);
        const boredWorryLevel = worryLevel / worryDivider;
        const nextMonkeyIndex = (boredWorryLevel % monkey.test.divisible === 0n) ? monkey.test.yes : monkey.test.no;
        const nextMonkey = monkeys.find((m) => m.monkey === nextMonkeyIndex);
        if (nextMonkey) {
          nextMonkey.items = [...nextMonkey.items, boredWorryLevel];
        }
      });

      // eslint-disable-next-line no-param-reassign
      monkey.items = [];
    });

    // console.log(`After round ${roundIndex + 1}:`, monkeys.map(({ monkey, items }) => ({ monkey, items })));
  }

  return monkeys
};

const main = (filename, rounds, worryDivider) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8');
  const monkeys = parseInput(text);

  const topInspections = run(monkeys, rounds, worryDivider)
    .map(({ inspections}) => inspections)
    .sort((a, b) => b - a)
    .slice(0, 2);

  return topInspections[0] * topInspections[1];
};

console.log('Part 1:', main('input.txt', 20, 3n));
console.log('Part 2:', main('sample.txt', 10000, 1n));
