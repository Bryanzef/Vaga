// String a ser invertida
let str = "Hello, world!";

// Converter a string em um array de caracteres
let arr = str.split("");

// Inverter o array
let reversedArr = [];
for (let i = arr.length - 1; i >= 0; i--) {
  reversedArr.push(arr[i]);
}

// Converter o array de volta para uma string
let reversedStr = reversedArr.join("");

// Exibir a string invertida
console.log(reversedStr);
