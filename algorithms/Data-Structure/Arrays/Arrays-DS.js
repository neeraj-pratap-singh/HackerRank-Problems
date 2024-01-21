// // An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A, of size N, each memory location has some unique index, i (where 0<=i<=N), that can be referenced as A[i].

// // Reverse an array of integers.

// // Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

// // Example
// // A = [1,2,3]
// // Return [3,2,1].

// // Function Description

// // Complete the function reverseArray in the editor below.

// // reverseArray has the following parameter(s):

// // int A[n]: the array to reverse
// // Returns

// // int[n]: the reversed array
// // Input Format

// // The first line contains an integer, N, the number of integers in A.
// // The second line contains N space-separated integers that make up A.

// // Method 1: Using Array.prototype.reverse()
// function reverseArrayM1(A) {
//     return A.reverse();
// }

// // Method 2: Two-pointer Approach
// function reverseArrayM2(A) {
//     let start = 0;
//     let end = A.length - 1;
//     while (start < end) {
//         [A[start], A[end]] = [A[end], A[start]]; // Swap elements
//         start++;
//         end--;
//     }
//     return A;
// }

// // Method 3: Using a New Array
// function reverseArrayM3(A) {
//     const newArray = [];
//     for (let i = A.length - 1; i >= 0; i--) {
//         newArray.push(A[i]);
//     }
//     return newArray;
// }


// const A = [1, 2, 3];
// console.log('Using Method 1: ',reverseArrayM1(A)); // Output: [3, 2, 1]
// console.log('Using Method 2: ',reverseArrayM2(A)); // Output: [3, 2, 1]
// console.log('Using Method 3: ',reverseArrayM3(A)); // Output: [3, 2, 1]


'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'reverseArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function reverseArray(a) {
    // Write your code here
    let reverseArray = [];
    for(let i = a.length -1; i >= 0; i--){
        reverseArray.push(a[i])
    }
    return reverseArray;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const arrCount = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const res = reverseArray(arr);

    ws.write(res.join(' ') + '\n');

    ws.end();
}
