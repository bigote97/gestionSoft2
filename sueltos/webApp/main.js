let homeButton = document.getElementById('homeButton')
let searchButton = document.getElementById('searchButton')
let listadoButton = document.getElementById('listadoButton')
let agregarButton = document.getElementById('agregarButton')

let home = document.getElementById('home')
let plantSearch = document.getElementById('plantSearch')
let listado = document.getElementById('listado')
let agregar = document.getElementById('agregar')

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