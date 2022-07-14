let homeButton = document.getElementById('homeButton')
let searchButton = document.getElementById('searchButton')
let listadoButton = document.getElementById('listadoButton')
let agregarButton = document.getElementById('agregarButton')

let home = document.getElementById('home')
let plantSearch = document.getElementById('plantSearch')
let listado = document.getElementById('listado')
let agregar = document.getElementById('agregar')
let formAgregarSender = document.getElementById('formAgregarSender')

let listadoPlantas = [];

window.addEventListener('DOMContentLoaded', (event) => {
    listadoPlantas = JSON.parse(localStorage.getItem("plantas") || "[]");
});

function storagePlantas(planta) {
    listadoPlantas = JSON.parse(localStorage.getItem("plantas") || "[]");
    listadoPlantas.push(planta)
    localStorage.setItem("plantas", JSON.stringify(listadoPlantas));
}
homeButton.addEventListener('click', () => {
    plantSearch.style.display = 'none';
    listado.style.display = 'none';
    agregar.style.display = 'none';
    home.style.display ='block';
})
searchButton.addEventListener('click', () => {
    home.style.display = 'none';
    listado.style.display = 'none';
    agregar.style.display = 'none';
    plantSearch.style.display ='block';
})
listadoButton.addEventListener('click', () => {
    plantSearch.style.display = 'none';
    home.style.display = 'none';
    agregar.style.display = 'none';
    listado.style.display ='block';
})
agregarButton.addEventListener('click', () => {
    plantSearch.style.display = 'none';
    listado.style.display = 'none';
    home.style.display = 'none';
    agregar.style.display ='block';
})

formAgregarSender.addEventListener('click', (event) => {
    let plantType = document.getElementById('typeSelector').value;
    let plantName = document.getElementById('plantName').value;
    let plantSiembra  = document.getElementById('plantSiembra').value;
    let plantCosecha = document.getElementById('plantCosecha').value;
    let planta = {
        'type': plantType,
        'name': plantName,
        'cosecha': plantCosecha,
        'siembra': plantSiembra
    }
    console.log(planta)
    storagePlantas(planta)
})
