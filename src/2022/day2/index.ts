import * as fs from 'fs';

enum Shape {
  Rock = 'Rock',
  Paper = 'Paper',
  Scissors = 'Scissors',
}

enum ShapeCode {
  A = Shape.Rock,
  B = Shape.Paper,
  C = Shape.Scissors,
  // part one code: X, Y, Z
  X = Shape.Rock,
  Y = Shape.Paper,
  Z = Shape.Scissors,
}

const ShapeScore = {
  [Shape.Rock]: 1,
  [Shape.Paper]: 2,
  [Shape.Scissors]: 3,
};

enum Ending  {
  Loss = 'loss',
  Draw = 'draw',
  Win = 'win',
}

const EndingCode = {
  X: Ending.Loss,
  Y: Ending.Draw,
  Z: Ending.Win,
};

const EndingScore = {
  [Ending.Loss]: 0,
  [Ending.Draw]: 3,
  [Ending.Win]: 6,
};

const splitIntoGames = (text: string) => text.split(/\r?\n/).map((line: string) => line.split(' '));

const play = (a: Shape, b: Shape): Ending => {
  if (a === Shape.Rock && b === Shape.Scissors) {
    return Ending.Loss;
  }
  if (a === Shape.Scissors && b === Shape.Rock) {
    return Ending.Win;
  }

  if (a === Shape.Scissors && b === Shape.Paper) {
    return Ending.Loss;
  }
  if (a === Shape.Paper && b === Shape.Scissors) {
    return Ending.Win;
  }

  if (a === Shape.Paper && b === Shape.Rock) {
    return Ending.Loss;
  }
  if (a === Shape.Rock && b === Shape.Paper) {
    return Ending.Win;
  }

  return Ending.Draw;
};

const score = (opponentChoice: Shape, playerChoice: Shape): number => {
  const game = play(opponentChoice, playerChoice);

  return EndingScore[game];
};

const calcPlayerChoice = (opponentChoice: Shape, result: Ending): Shape => {
  if (opponentChoice === Shape.Rock && result === Ending.Loss) {
    return Shape.Scissors;
  }
  if (opponentChoice === Shape.Rock && result === Ending.Draw) {
    return Shape.Rock;
  }
  if (opponentChoice === Shape.Rock && result === Ending.Win) {
    return Shape.Paper;
  }

  if (opponentChoice === Shape.Paper && result === Ending.Loss) {
    return Shape.Rock;
  }
  if (opponentChoice === Shape.Paper && result === Ending.Draw) {
    return Shape.Paper;
  }
  if (opponentChoice === Shape.Paper && result === Ending.Win) {
    return Shape.Scissors;
  }

  if (opponentChoice === Shape.Scissors && result === Ending.Loss) {
    return Shape.Paper;
  }
  if (opponentChoice === Shape.Scissors && result === Ending.Draw) {
    return Shape.Scissors;
  }
  if (opponentChoice === Shape.Scissors && result === Ending.Win) {
    return Shape.Rock;
  }

  return null;
};

const partOne = (filename: string) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf8');
  const games = splitIntoGames(text);

  const totalScore = games.reduce((acc, curr) => {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const opponentChoice = ShapeCode[curr[0]] as Shape;
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const playerChoice = ShapeCode[curr[1]] as Shape;

    return acc + score(opponentChoice, playerChoice) + ShapeScore[playerChoice];
  }, 0);

  return {
    games: games.length,
    totalScore,
  };
};

const partTwo = (filename: string) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf8');
  const games = splitIntoGames(text);

  const totalScore = games.reduce((acc, curr) => {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const opponentChoice = ShapeCode[curr[0]];
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const result = EndingCode[curr[1]];
    const playerChoice = calcPlayerChoice(opponentChoice, result);

    return acc + score(opponentChoice, playerChoice) + ShapeScore[playerChoice];
  }, 0);

  return {
    games: games.length,
    totalScore,
  };
};

console.log('Part 1:', partOne('input.txt'));
console.log('Part 2:', partTwo('input.txt'));

