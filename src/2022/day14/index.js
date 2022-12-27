const fs = require('fs');

class Cave {
  minX = Number.MAX_VALUE;

  maxX = 0;

  minY = 0;

  maxY = 0;

  grid = [];

  constructor(paths) {
    // detect dimensions
    paths.forEach((path) => {
      path.forEach((line) => {
        if (line.x < this.minX) {
          this.minX = line.x;
        }
        if (line.x > this.maxX) {
          this.maxX = line.x;
        }
        if (line.y < this.minY) {
          this.minY = line.y;
        }
        if (line.y > this.maxY) {
          this.maxY = line.y;
        }
      });
    });

    // create grid
    this.grid = new Array(this.maxY + 1)
      .fill([])
      .map(() => new Array(this.maxX + 1).fill('.'));

    // draw paths
    paths.forEach((path) => {
      path.forEach((line, index) => {
        if (index >= path.length - 2) {
          return;
        }
        if (line.y === path[index + 1].y) {
          // horizontal line
          if (line.x <= path[index + 1].x) {
            for (let v = line.x; v <= path[index + 1].x; v += 1) {
              this.grid[line.y][v] = '#';
            }
          } else {
            for (let v = line.x; v >= path[index + 1].x; v -= 1) {
              this.grid[line.y][v] = '#';
            }
          }
        } else if (line.x === path[index + 1].x) {
          // vertical line
          if (line.y <= path[index + 1].y) {
            for (let h = line.y; h <= path[index + 1].y; h += 1) {
              this.grid[h][line.x] = '#';
            }
          } else {
            for (let h = line.y; h >= path[index + 1].y; h -= 1) {
              this.grid[h][line.x] = '#';
            }
          }
        }
      });
    })
  }

  toString() {
    return this.grid
      .slice(this.minY, this.maxY + 1)
      .map((line) => line
        .slice(this.minX, this.maxX + 1)
        .join(''))
      .join('\n');
  }
}

const parseInput = (text) =>
  text
    .split(/\n/)
    .map((line) => {
      const path = line.split(' -> ');

      return path.map((coordinates) => {
        const [x, y] = coordinates.split(',')

        return {
          x: parseInt(x, 10),
          y: parseInt(y, 10),
        };
      });
    });

const partOne = (filename) => {
  const text = fs.readFileSync(`${__dirname}/${filename}`, 'utf-8')
  const data = parseInput(text);
  const cave = new Cave(data);

  return cave.toString();
};

console.log('Part 1:', `\n${partOne('sample.txt')}`);
