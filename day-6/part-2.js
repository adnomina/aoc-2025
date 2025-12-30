import { open } from "node:fs/promises";

async function parseLines(filename) {
    const operators = [];
    const numbers = [];

    const file = await open(filename);

    for await (const line of file.readLines()) {
        if (/[+\-*/]/.test(line)) {
            operators.push(...line.match(/[+\-*/]/g).reverse());

            break;
        }

        const row = line.split("").reverse();

        if (numbers.length === 0) {
            numbers.push(...row);

            continue;
        }

        for (let i = 0; i < row.length; i++) {
            numbers[i] += row[i];
        }
    }

    return {
        numbers: numbers.map((number) => number.trim()),
        operators,
    };
}

function evaluateProblems(numbers, operators) {
    let total = 0;
    let problem = [];
    let operatorIndex = 0;

    for (let i = 0; i < numbers.length; i++) {
        const number = numbers[i];
        const operator = operators[operatorIndex];

        if (number.length > 0) {
            problem.push(number);
        }

        if (number.length === 0 || i === numbers.length - 1) {
            const equation = problem.join(operator);
            const result = new Function(`return ${equation}`)();

            total += result;

            problem = [];
            operatorIndex++;
        }
    }

    return total;
}

(async function main() {
    parseLines("input.txt").then(({ numbers, operators }) => {
        const total = evaluateProblems(numbers, operators);
        console.log(total);
    }).catch((error) => {
        console.error(error);
        process.exit(1);
    });
})();
