// (abc)^n (ab)^m, n>=1, m>=1

const input = "abcabcabc";

let cursorOffset = 0;
let n = 0;
let m = 0;

// Считываем (abc)^n
while (
    cursorOffset + 2 < input.length &&
    input[cursorOffset] === 'a' &&
    input[cursorOffset + 1] === 'b' &&
    input[cursorOffset + 2] === 'c'
) {
    cursorOffset += 3;
    n++;
}

// Считываем (ab)^m
while (
    cursorOffset + 1 < input.length &&
    input[cursorOffset] === 'a' &&
    input[cursorOffset + 1] === 'b'
) {
    cursorOffset += 2;
    m++;
}

console.log(`Строка: ${input}, n=${n}, m=${m}`);
// Проверяем все условия
if (cursorOffset === input.length && n >= 1 && m >= 1) {
  console.log("Подходит");
} else {
  console.log("Не подходит");
}
