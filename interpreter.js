//Constants
const fs = require("fs");
const path = require("path");
const readLine = require("readline");

//File System checks
if (process.argv[2] == null || process.argv[3] == null) throw new Error("Invalid arguments");
let sourceDir = path.resolve(process.argv[2]);
let targetDir = path.resolve(process.argv[3]);


fs.access(sourceDir, fs.constants.F_OK | fs.constants.R_OK, error => {if (error) throw new Error("Source folder is not readable")});
fs.access(targetDir, fs.constants.F_OK | fs.constants.W_OK, error => {if (error) throw new Error("Target folder is not writable")});

//Function Declarations
function getUserInput(question) {
    const rl = readLine.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise((resolve) => {
        rl.question(question, answer => resolve(answer));
    });
}

fs.readdir(targetDir, (error, files) => {
    if (error) throw error;
    
});