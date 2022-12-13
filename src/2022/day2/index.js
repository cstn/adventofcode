const { readFileContent } = require('../../utils/file');

const Shape = {
    Rock: 'Rock',
    Paper: 'Paper',
    Scissors: 'Scissors',
};

const Code = {
    'A': Shape.Rock,
    'B': Shape.Paper,
    'C': Shape.Scissors,
    'X': Shape.Rock,
    'Y': Shape.Paper,
    'Z': Shape.Scissors,
};

const ShapeScore = {
    [Shape.Rock]: 1,
    [Shape.Paper]: 2,
    [Shape.Scissors]: 3,
};

const splitIntoGames = (text) => text.split(/\r?\n/).map((line) => line.split(' '));

const decode = (token) => Code[token];

const play = (a, b) => {
    if (a === Shape.Rock && b === Shape.Scissors) {
        return -1;
    }
    if (a === Shape.Scissors && b === Shape.Rock) {
        return 1;
    }

    if (a === Shape.Scissors && b === Shape.Paper) {
        return -1;
    }
    if (a === Shape.Paper && b === Shape.Scissors) {
        return 1;
    }

    if (a === Shape.Paper && b === Shape.Rock) {
        return -1;
    }
    if (a === Shape.Rock && b === Shape.Paper) {
        return 1;
    }

    return 0;
};

const score = (a, b) => {
    const opponentChoice = decode(a);
    const playerChoice = decode(b);
    const game = play(opponentChoice, playerChoice);

    if (game < 0) {
        return ShapeScore[playerChoice] + 0;
    }

    if (game > 0) {
        return ShapeScore[playerChoice] + 6;
    }

    return ShapeScore[playerChoice] + 3;
};

const partOne = () => {
    const text = readFileContent(`${__dirname}/input`);
    const games = splitIntoGames(text);

    const totalScore = games.reduce((acc, curr) => acc + score(...curr), 0);

    console.log(`Part one: Total score after ${games.length} games:`, totalScore);
};

partOne();