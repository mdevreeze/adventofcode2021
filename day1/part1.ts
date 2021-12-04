const example = await Deno.readTextFile("./example");
const input = await Deno.readTextFile("./input");

function countIncreases(values: number[]) {
    let previousValue: number|undefined = undefined;
    let increaseCount = 0;
    values.forEach(value => {
        if (previousValue && value > previousValue) {
            increaseCount++;
        }
        previousValue = value;
    });
    return increaseCount;
}

const toNumberArray = (text: string) => text.split("\n").map((v) => { return parseInt(v)});

console.log("Example answer is:", countIncreases(toNumberArray(example)));
console.log("Real answer is:", countIncreases(toNumberArray(input)));