const f1 = () => {
    let frutas = ["maçã", "banana"];
    frutas.push("laranja");
    console.log(frutas);
}

const f2 = () => {
    let arr = [1, 2, 3, 4];
    console.log(arr.pop());
}

const f3 = () => {
    let animais = ["gato", "cachorro"];
    animais.unshift("pássaro");
    console.log(animais);
}

const f4 = () => {
    let cores = ["vermelho", "verde", "azul"];
    console.log(cores.shift());
}

const f5 = () => {
    let carros = ["Fiat", "Ford", "Chevrolet"];
    carros.splice(1, 0, "Volkswagen");
    console.log(carros);
}

const f6 = () => {
    let letras = ['a', 'b', 'c', 'd', 'e'];
    let newLetras = letras.slice(1, 4);
    console.log(newLetras);
}

const f7 = () => {
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr.forEach((a) => {
        console.log(a*2);
    })
}

const f8 = () => {
    let cidades = [12, 18, 25, 30, 15];
    let newCidades = cidades.filter((x) => {
        return x>18;
    }).map((x)=> {
        return x*2;
    })
    console.log(newCidades);
}

const f9 = () => {
    let nomes = ["joao", "maria", "marivaldo", "jonas", "morgana"];
    nomes.forEach(nome => {
        console.log(nome);
    })
    let numbers = [1, 2, 5, 6 ,7, 9, 10, 20, 31, 123];
    numbers = numbers.map(number => {
        return number*2;
    })
    let odds = numbers.filter(number => {
        return number%2 != 0;
    })
}

(() => {
    f9()
})()