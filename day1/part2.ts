import _ from "https://cdn.skypack.dev/lodash";

const example = await Deno.readTextFile("./example");
const input = await Deno.readTextFile("./input");

function countIncreasedMeasurementWindows(values: number[]) {
    const valuesPerWindow = 3;
    let increaseCount = 0;

    for (let i = valuesPerWindow; i < values.length; i += valuesPerWindow) {

        for (let i = va; i < valuesPerWindow; i++) {
        }
        for (let i = 0; i < valuesPerWindow; i++) {
        }
    }
}

const toNumberArray = (text: string) => text.split("\n").map((v) => { return parseInt(v)});

console.log("Example answer is:", countIncreasedMeasurementWindows(toNumberArray(example)));
// console.log("Real answer is:", countIncreasedMeasurementWindows(toNumberArray(input)));