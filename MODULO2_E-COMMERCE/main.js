// 1. DEFINICIÓN DE PRODUCTOS (Yates) [Requisito: Arreglo de objetos]
const yates = [
    {
        id: 1,
        nombre: "Viking Majesty",
        precio: 5200000,
        descripcion: "Yate de lujo con acabados de alta gama y capacidad para 12 personas.",
        imagen: "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?q=80&w=600",
        categoria: "Lujo"
    },
    {
        id: 2,
        nombre: "Sport Cruiser X",
        precio: 1800000,
        descripcion: "Velocidad y diseño aerodinámico para los amantes de la adrenalina.",
        imagen: "https://images.unsplash.com/photo-1540946484617-41d4f738ba4c?q=80&w=600",
        categoria: "Deportivo"
    },
    {
        id: 3,
        nombre: "Eco-Spirit 2026",
        precio: 3500000,
        descripcion: "Propulsión híbrida sustentable diseñada para navegación silenciosa.",
        imagen: "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?q=80&w=600",
        categoria: "Sustentable"
    }
];

// 2. ESTADO DEL CARRITO [Requisito: Simulado con localStorage]
let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

// 3. FUNCIONES DE LÓGICA

// Actualiza el contador visual en el Navbar
function actualizarContador() {
    const contador = document.querySelector('#cart-count');
    if (contador) {
        contador.innerText = carrito.length;
    }
}

// Agrega un yate al arreglo del carrito y lo guarda en el navegador
function agregarAlCarrito(id) {
    const yateSeleccionado = yates.find(y => y.id === id);
    if (yateSeleccionado) {
        carrito.push(yateSeleccionado);
        localStorage.setItem('carrito', JSON.stringify(carrito)); // Guardar en persistencia
        actualizarContador();
        alert(`${yateSeleccionado.nombre} ha sido añadido a tu flota.`);
    }
}

// 4. INICIALIZACIÓN
// Ejecutamos la actualización al cargar el script para que no se pierda el número al refrescar
actualizarContador();

// 5. RENDERIZADO DINÁMICO [Requisito: Etiquetas Semánticas]
function renderizarYates() {
    const contenedor = document.querySelector('#contenedor-yates');
    if (!contenedor) return;

    contenedor.innerHTML = ""; // Limpiar antes de cargar

    yates.forEach(yate => {
        const div = document.createElement('div');
        div.className = "col-md-4 mb-4";
        
        // Aquí insertamos la etiqueta <article> para la rúbrica
        div.innerHTML = `
            <article class="card h-100 shadow-sm">
                <img src="${yate.imagen}" class="card-img-top" alt="${yate.nombre}">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title text-primary">${yate.nombre}</h5>
                    <p class="card-text flex-grow-1">${yate.descripcion}</p>
                    <p class="fw-bold fs-5">$${yate.precio.toLocaleString()} USD</p>
                    <button onclick="agregarAlCarrito(${yate.id})" class="btn btn-primary w-100">
                        Agregar al carrito
                    </button>
                </div>
            </article>
        `;
        contenedor.appendChild(div);
    });
}

// Llamar a la función al cargar la página
renderizarYates();