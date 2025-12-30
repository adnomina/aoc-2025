import { open } from "node:fs/promises";

(async () => {
	const file = await open("input.txt");

	const numbers = [];
	const operators = [];
	for await (const line of file.readLines()) {
		if (/\d{1,4}/g.test(line)) {
			numbers.push(line.match(/\d{1,4}/g));
		} else {
			operators.push(...line.match(/[\+\-\*\/]/g));
		}
	}

	let grandTotal = 0;
	for (let i = 0; i < operators.length; i++) {
		const operands = numbers.map((row) => row[i]);
		const problem = operands.join(operators[i]);
        const result = new Function(`return ${problem}`)(); 

		grandTotal += result;
	}

	console.log(grandTotal);
})();
