const numOperations = 100000000;

// Addition
let startTime = Date.now();
let result = 0;
for (let i = 0; i < numOperations; i++) {
    result += 1;
}
let endTime = Date.now();
console.log(`Time taken for 100 million additions: ${(endTime - startTime) / 1000} seconds`);

// Subtraction
startTime = Date.now();
result = numOperations;
for (let i = 0; i < numOperations; i++) {
    result -= 1;
}
endTime = Date.now();
console.log(`Time taken for 100 million subtractions: ${(endTime - startTime) / 1000} seconds`);

// Multiplication
startTime = Date.now();
result = 1;
for (let i = 0; i < numOperations; i++) {
    result *= 1;
}
endTime = Date.now();
console.log(`Time taken for 100 million multiplications: ${(endTime - startTime) / 1000} seconds`);

// Division
startTime = Date.now();
result = numOperations;
for (let i = 0; i < numOperations; i++) {
    result /= 1;
}
endTime = Date.now();
console.log(`Time taken for 100 million divisions: ${(endTime - startTime) / 1000} seconds`);

// Time taken for 100 million additions: 0.073 seconds
// Time taken for 100 million subtractions: 0.059 seconds
// Time taken for 100 million multiplications: 0.045 seconds
// Time taken for 100 million divisions: 0.045 seconds