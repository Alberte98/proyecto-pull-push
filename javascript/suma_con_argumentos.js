// Similar a args en Python

function sumaConArgs(...args) {
  let resultado = 0;
  for (let num of args) {
      resultado += num;
  }
  return resultado;
}

const numeros = [1, 2, 3, 4, 5];
const total = sumaConArgs(...numeros);
console.log("La suma es:", total);
