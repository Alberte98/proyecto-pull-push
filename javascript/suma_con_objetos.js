/* 
Similar a **kwargs en python

En JAvaScript se utiliza el operador de propagación "..."
*/

function sumaConKwargs(...args) {
  let resultado = 0;
  for (let key in args) {
      resultado += args[key];
  }
  return resultado;
}

const valores = { a: 10, b: 20, c: 30 };
const total = sumaConKwargs(valores);
console.log("La suma es:", total);
