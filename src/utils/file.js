const fs = require('fs');

const readFileContent = (filename) => fs.readFileSync(filename, 'utf8');

module.exports = {
    readFileContent,
};
