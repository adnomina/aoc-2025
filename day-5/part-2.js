import fs from "node:fs/promises";
 
function rangesOverlap(rangeA, rangeB) {
    return rangeA.start <= rangeB.end && rangeB.start <= rangeA.end;
}
 
function mergeRanges(rangeA, rangeB) {
    return {
        start: Math.min(rangeA.start, rangeB.start),
        end: Math.max(rangeA.end, rangeB.end)
    };
}
 
function calculateFreshIds(ranges) {
    if (ranges.length === 0) {
        return 0;
    }
 
    const currentRange = ranges.slice(0, 1)[0];
    const rest = ranges.slice(1);
 
    let mergedRange = currentRange;
    let unmergedRanges = [];
 
    for (const range of rest) {
        if (rangesOverlap(mergedRange, range)) {
            mergedRange = mergeRanges(mergedRange, range);
        } else {
            unmergedRanges.push(range);
        }
    }
 
    const freshIds = mergedRange.end - mergedRange.start + 1;
 
    return freshIds + calculateFreshIds(unmergedRanges);
}
 
(async () => {
    const file = await fs.open("input.txt");
 
    let ranges = [];
    for await (const line of file.readLines()) {
        if (!line.includes("-")) {
            continue;
        }
 
        const [start, end] = line.split("-").map(item => parseInt(item));
        ranges.push({ start, end });
    }
 
    ranges.sort((a, b) => a.start - b.start );
 
    const freshIds = calculateFreshIds(ranges);
    console.log(freshIds);
})();
