from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="MiCHUZO")

# ============================================================
# DATOS DE EJEMPLO
# Más adelante esto pasará a una base de datos.
# ============================================================

restaurantes = [
    {
        "id": 1,
        "nombre": "Hamburguesas El Parque",
        "categoria": "Hamburguesas",
        "emoji": "🍔",
        "rating": 4.8,
        "tiempo": "20-30 min",
        "domicilio": 4000,
        "descripcion": "Hamburguesas, papas y bebidas."
    },
    {
        "id": 2,
        "nombre": "Pizza Central",
        "categoria": "Pizza",
        "emoji": "🍕",
        "rating": 4.6,
        "tiempo": "25-35 min",
        "domicilio": 5000,
        "descripcion": "Pizzas artesanales y combos."
    },
    {
        "id": 3,
        "nombre": "Pollo Express",
        "categoria": "Pollo",
        "emoji": "🍗",
        "rating": 4.7,
        "tiempo": "20-30 min",
        "domicilio": 4000,
        "descripcion": "Pollo, papas, arroz y bebidas."
    },
    {
        "id": 4,
        "nombre": "Perros La Plaza",
        "categoria": "Perros",
        "emoji": "🌭",
        "rating": 4.5,
        "tiempo": "15-25 min",
        "domicilio": 3500,
        "descripcion": "Perros calientes y hamburguesas."
    }
]


menus = {
    1: [
        {
            "id": 101,
            "nombre": "Hamburguesa Clásica",
            "precio": 18000,
            "emoji": "🍔",
            "descripcion": "Carne, queso, tomate, lechuga y salsa."
        },
        {
            "id": 102,
            "nombre": "Hamburguesa Especial",
            "precio": 24000,
            "emoji": "🍔",
            "descripcion": "Doble carne, queso, tocineta y salsa especial."
        },
        {
            "id": 103,
            "nombre": "Papas Fritas",
            "precio": 8000,
            "emoji": "🍟",
            "descripcion": "Papas fritas crujientes."
        },
        {
            "id": 104,
            "nombre": "Gaseosa",
            "precio": 5000,
            "emoji": "🥤",
            "descripcion": "Gaseosa personal."
        }
    ],

    2: [
        {
            "id": 201,
            "nombre": "Pizza Personal",
            "precio": 18000,
            "emoji": "🍕",
            "descripcion": "Pizza personal con queso y salsa."
        },
        {
            "id": 202,
            "nombre": "Pizza Grande",
            "precio": 35000,
            "emoji": "🍕",
            "descripcion": "Pizza grande para compartir."
        },
        {
            "id": 203,
            "nombre": "Pizza Especial",
            "precio": 42000,
            "emoji": "🍕",
            "descripcion": "Pizza con varios ingredientes."
        }
    ],

    3: [
        {
            "id": 301,
            "nombre": "Pollo Asado",
            "precio": 30000,
            "emoji": "🍗",
            "descripcion": "Pollo asado con papas y ensalada."
        },
        {
            "id": 302,
            "nombre": "Medio Pollo",
            "precio": 18000,
            "emoji": "🍗",
            "descripcion": "Medio pollo con acompañamiento."
        },
        {
            "id": 303,
            "nombre": "Combo Familiar",
            "precio": 50000,
            "emoji": "🍗",
            "descripcion": "Pollo familiar con varios acompañamientos."
        }
    ],

    4: [
        {
            "id": 401,
            "nombre": "Perro Clásico",
            "precio": 12000,
            "emoji": "🌭",
            "descripcion": "Perro caliente con papas y salsas."
        },
        {
            "id": 402,
            "nombre": "Perro Especial",
            "precio": 16000,
            "emoji": "🌭",
            "descripcion": "Perro especial con queso y tocineta."
        },
        {
            "id": 403,
            "nombre": "Combo Perro",
            "precio": 20000,
            "emoji": "🌭",
            "descripcion": "Perro especial + papas + bebida."
        }
    ]
}


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

@app.get("/", response_class=HTMLResponse)
async def inicio():

    return HTMLResponse(content=HTML)


# ============================================================
# API DE RESTAURANTES
# ============================================================

@app.get("/api/restaurantes")
async def obtener_restaurantes():

    return restaurantes


# ============================================================
# API DEL MENÚ
# ============================================================

@app.get("/api/restaurante/{restaurante_id}/menu")
async def obtener_menu(restaurante_id: int):

    restaurante = next(
        (
            r for r in restaurantes
            if r["id"] == restaurante_id
        ),
        None
    )

    if restaurante is None:
        return {
            "error": "Restaurante no encontrado"
        }

    return {
        "restaurante": restaurante,
        "menu": menus.get(restaurante_id, [])
    }


# ============================================================
# HTML COMPLETO
# ============================================================

HTML = """
<!DOCTYPE html>

<html lang="es">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>MiChuzo</title>


<style>

/* =========================================================
   GENERAL
   ========================================================= */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {

    font-family:
    Arial,
    Helvetica,
    sans-serif;

    background: #f5f6f8;

    color: #202124;
}


/* =========================================================
   HEADER
   ========================================================= */

header {

    height: 70px;

    background: white;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 7%;

    box-shadow:
    0 2px 10px
    rgba(0,0,0,0.08);

    position: sticky;

    top: 0;

    z-index: 100;
}


.logo {

    font-size: 26px;

    font-weight: 800;

    color: #222;
}


.logo span {

    color: #ff4b2b;
}


.header-buttons {

    display: flex;

    gap: 10px;
}


.header-button {

    border: none;

    padding: 10px 17px;

    border-radius: 20px;

    background: #f1f1f1;

    cursor: pointer;

    font-weight: 600;
}


.header-button:hover {

    background: #ff4b2b;

    color: white;
}


.cart-button {

    background: #ff4b2b;

    color: white;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {

    background:
    linear-gradient(
        135deg,
        #ff512f,
        #dd2476
    );

    padding: 55px 7%;

    color: white;
}


.hero h1 {

    font-size: 42px;

    margin-bottom: 12px;
}


.hero p {

    font-size: 18px;

    margin-bottom: 25px;
}


.search-container {

    max-width: 650px;

    position: relative;
}


.search {

    width: 100%;

    border: none;

    outline: none;

    padding: 17px 20px;

    border-radius: 12px;

    font-size: 16px;
}


/* =========================================================
   CONTENIDO
   ========================================================= */

.container {

    width: 86%;

    max-width: 1200px;

    margin: 35px auto;
}


.section-title {

    margin-bottom: 20px;

    font-size: 25px;
}


/* =========================================================
   CATEGORIAS
   ========================================================= */

.categories {

    display: flex;

    gap: 12px;

    overflow-x: auto;

    padding-bottom: 15px;

    margin-bottom: 20px;
}


.category {

    border: none;

    background: white;

    padding: 12px 20px;

    border-radius: 25px;

    white-space: nowrap;

    cursor: pointer;

    font-weight: 600;

    box-shadow:
    0 2px 8px
    rgba(0,0,0,0.05);
}


.category:hover {

    background: #ff4b2b;

    color: white;
}


/* =========================================================
   RESTAURANTES
   ========================================================= */

.restaurants {

    display: grid;

    grid-template-columns:
    repeat(
        auto-fit,
        minmax(270px, 1fr)
    );

    gap: 22px;
}


.restaurant {

    background: white;

    border-radius: 16px;

    overflow: hidden;

    box-shadow:
    0 3px 15px
    rgba(0,0,0,0.08);

    transition:
    transform .2s;
}


.restaurant:hover {

    transform:
    translateY(-5px);
}


.restaurant-image {

    height: 170px;

    display: flex;

    justify-content: center;

    align-items: center;

    font-size: 65px;

    background:
    linear-gradient(
        135deg,
        #ff9966,
        #ff5e62
    );
}


.restaurant-info {

    padding: 20px;
}


.restaurant-info h3 {

    font-size: 20px;

    margin-bottom: 8px;
}


.rating {

    color: #f3a600;

    margin-bottom: 8px;
}


.info {

    color: #666;

    font-size: 14px;

    margin: 6px 0;
}


.description {

    color: #555;

    font-size: 14px;

    margin-top: 10px;
}


.menu-button {

    width: 100%;

    margin-top: 15px;

    padding: 12px;

    border: none;

    border-radius: 9px;

    background: #ff4b2b;

    color: white;

    font-weight: bold;

    cursor: pointer;
}


.menu-button:hover {

    background: #e43e21;
}


/* =========================================================
   MODAL
   ========================================================= */

.modal {

    display: none;

    position: fixed;

    inset: 0;

    background:
    rgba(0,0,0,.55);

    z-index: 500;

    align-items: center;

    justify-content: center;

    padding: 20px;
}


.modal.active {

    display: flex;
}


.modal-content {

    width: 100%;

    max-width: 600px;

    max-height: 90vh;

    overflow-y: auto;

    background: white;

    border-radius: 18px;

    padding: 25px;

    position: relative;
}


.close {

    position: absolute;

    right: 20px;

    top: 15px;

    border: none;

    background: #eee;

    width: 35px;

    height: 35px;

    border-radius: 50%;

    cursor: pointer;

    font-size: 18px;
}


.modal-title {

    margin-bottom: 5px;

    font-size: 27px;
}


.modal-subtitle {

    color: #666;

    margin-bottom: 25px;
}


/* =========================================================
   PRODUCTOS
   ========================================================= */

.product {

    display: flex;

    align-items: center;

    gap: 15px;

    padding: 15px 0;

    border-bottom:
    1px solid #eee;
}


.product-icon {

    width: 65px;

    height: 65px;

    background: #f3f3f3;

    border-radius: 12px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 35px;
}


.product-info {

    flex: 1;
}


.product-name {

    font-weight: bold;

    margin-bottom: 5px;
}


.product-description {

    color: #777;

    font-size: 13px;

    margin-bottom: 6px;
}


.product-price {

    font-weight: bold;

    color: #ff4b2b;
}


.add-button {

    border: none;

    background: #ff4b2b;

    color: white;

    width: 38px;

    height: 38px;

    border-radius: 50%;

    font-size: 22px;

    cursor: pointer;
}


/* =========================================================
   CARRITO
   ========================================================= */

.cart-items {

    margin-top: 20px;
}


.cart-item {

    display: flex;

    justify-content: space-between;

    align-items: center;

    padding: 13px 0;

    border-bottom:
    1px solid #eee;
}


.cart-total {

    display: flex;

    justify-content: space-between;

    font-size: 20px;

    font-weight: bold;

    margin-top: 20px;
}


.checkout {

    width: 100%;

    margin-top: 20px;

    padding: 15px;

    border: none;

    border-radius: 10px;

    background: #20a85a;

    color: white;

    font-size: 16px;

    font-weight: bold;

    cursor: pointer;
}


.empty {

    text-align: center;

    padding: 40px;

    color: #777;
}


/* =========================================================
   FOOTER
   ========================================================= */

footer {

    background: #202020;

    color: white;

    text-align: center;

    padding: 35px;

    margin-top: 60px;
}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 600px) {

    .hero h1 {

        font-size: 32px;
    }

    header {

        padding: 0 5%;
    }

    .logo {

        font-size: 22px;
    }

    .header-button {

        padding: 9px 12px;
    }

    .container {

        width: 90%;
    }

}

</style>

</head>


<body>


<!-- =======================================================
     HEADER
     ======================================================= -->

<header>

    <div class="logo">

        Mi<span>Chuzo</span>

    </div>


    <div class="header-buttons">

        <button
            class="header-button"
            onclick="login()">

            Iniciar sesión

        </button>


        <button
            class="header-button cart-button"
            onclick="abrirCarrito()">

            🛒 Carrito
            <span id="cartCount">0</span>

        </button>

    </div>

</header>



<!-- =======================================================
     HERO
     ======================================================= -->

<section class="hero">

    <h1>
        ¿Qué quieres comer?
    </h1>

    <p>
        Compra en los locales de tu pueblo
        y recibe tu pedido en casa.
    </p>


    <div class="search-container">

        <input
            id="search"
            class="search"
            type="text"
            placeholder="🔎 Buscar restaurante o comida..."
            oninput="buscar()">

    </div>

</section>



<!-- =======================================================
     CONTENIDO
     ======================================================= -->

<div class="container">


    <h2 class="section-title">
        Categorías
    </h2>


    <div class="categories">

        <button
            class="category"
            onclick="filtrar('Todos')">

            🍽️ Todos

        </button>


        <button
            class="category"
            onclick="filtrar('Hamburguesas')">

            🍔 Hamburguesas

        </button>


        <button
            class="category"
            onclick="filtrar('Pizza')">

            🍕

            Pizza

        </button>


        <button
            class="category"
            onclick="filtrar('Pollo')">

            🍗 Pollo

        </button>


        <button
            class="category"
            onclick="filtrar('Perros')">

            🌭 Perros

        </button>

    </div>



    <h2 class="section-title">

        🏪 Locales cerca de ti

    </h2>


    <div
        class="restaurants"
        id="restaurants">

    </div>


</div>



<!-- =======================================================
     MODAL MENU
     ======================================================= -->

<div
    class="modal"
    id="menuModal">


    <div class="modal-content">


        <button
            class="close"
            onclick="cerrarMenu()">

            ×

        </button>


        <h2
            class="modal-title"
            id="modalRestaurantName">

        </h2>


        <p
            class="modal-subtitle"
            id="modalRestaurantInfo">

        </p>


        <div id="menuProducts">

        </div>


    </div>

</div>



<!-- =======================================================
     MODAL CARRITO
     ======================================================= -->

<div
    class="modal"
    id="cartModal">


    <div class="modal-content">


        <button
            class="close"
            onclick="cerrarCarrito()">

            ×

        </button>


        <h2>

            🛒 Tu carrito

        </h2>


        <div
            class="cart-items"
            id="cartItems">

        </div>


        <div
            class="cart-total">

            <span>
                Total
            </span>

            <span id="cartTotal">
                $0
            </span>

        </div>


        <button
            class="checkout"
            onclick="hacerPedido()">

            Confirmar pedido

        </button>


    </div>

</div>



<!-- =======================================================
     FOOTER
     ======================================================= -->

<footer>

    <h3>
        MiChuzo
    </h3>

    <br>

    Tu plataforma local para pedir comida.

    <br><br>

    © 2026 MiChuzo

</footer>



<script>

/* =========================================================
   VARIABLES
   ========================================================= */

let restaurantes = [];

let carrito = [];

let restauranteActual = null;


/* =========================================================
   CARGAR RESTAURANTES
   ========================================================= */

async function cargarRestaurantes() {

    try {

        const respuesta =
            await fetch("/api/restaurantes");

        restaurantes =
            await respuesta.json();

        mostrarRestaurantes(restaurantes);

    }

    catch(error) {

        console.error(error);

        alert(
            "No se pudieron cargar los restaurantes."
        );

    }

}


/* =========================================================
   MOSTRAR RESTAURANTES
   ========================================================= */

function mostrarRestaurantes(lista) {

    const contenedor =
        document.getElementById(
            "restaurants"
        );


    contenedor.innerHTML = "";


    if (lista.length === 0) {

        contenedor.innerHTML = `

            <div class="empty">

                No encontramos restaurantes.

            </div>

        `;

        return;

    }


    lista.forEach(restaurante => {

        const tarjeta =
            document.createElement("div");


        tarjeta.className =
            "restaurant";


        tarjeta.dataset.categoria =
            restaurante.categoria;


        tarjeta.dataset.nombre =
            restaurante.nombre;


        tarjeta.innerHTML = `

            <div class="restaurant-image">

                ${restaurante.emoji}

            </div>


            <div class="restaurant-info">

                <h3>

                    ${restaurante.nombre}

                </h3>


                <div class="rating">

                    ⭐ ${restaurante.rating}

                </div>


                <div class="info">

                    🛵 ${restaurante.tiempo}

                </div>


                <div class="info">

                    💰 Domicilio:
                    $${formatoPrecio(
                        restaurante.domicilio
                    )}

                </div>


                <div class="description">

                    ${restaurante.descripcion}

                </div>


                <button
                    class="menu-button"
                    onclick="abrirMenu(
                        ${restaurante.id}
                    )">

                    Ver menú

                </button>

            </div>

        `;


        contenedor.appendChild(tarjeta);

    });

}


/* =========================================================
   BUSCAR
   ========================================================= */

function buscar() {

    const texto =
        document
        .getElementById("search")
        .value
        .toLowerCase()
        .trim();


    const resultados =
        restaurantes.filter(restaurante => {

            return (

                restaurante.nombre
                .toLowerCase()
                .includes(texto)

                ||

                restaurante.categoria
                .toLowerCase()
                .includes(texto)

                ||

                restaurante.descripcion
                .toLowerCase()
                .includes(texto)

            );

        });


    mostrarRestaurantes(resultados);

}


/* =========================================================
   FILTRAR
   ========================================================= */

function filtrar(categoria) {

    if (categoria === "Todos") {

        mostrarRestaurantes(restaurantes);

        return;

    }


    const resultados =
        restaurantes.filter(
            restaurante =>
                restaurante.categoria === categoria
        );


    mostrarRestaurantes(resultados);

}


/* =========================================================
   ABRIR MENÚ
   ========================================================= */

async function abrirMenu(restauranteId) {

    try {

        const respuesta =
            await fetch(
                `/api/restaurante/${restauranteId}/menu`
            );


        const datos =
            await respuesta.json();


        if (datos.error) {

            alert(datos.error);

            return;

        }


        restauranteActual =
            datos.restaurante;


        document.getElementById(
            "modalRestaurantName"
        ).innerText =
            restauranteActual.emoji +
            " " +
            restauranteActual.nombre;


        document.getElementById(
            "modalRestaurantInfo"
        ).innerText =
            "⭐ " +
            restauranteActual.rating +
            " · 🛵 " +
            restauranteActual.tiempo;


        const contenedor =
            document.getElementById(
                "menuProducts"
            );


        contenedor.innerHTML = "";


        datos.menu.forEach(producto => {

            const elemento =
                document.createElement("div");


            elemento.className =
                "product";


            elemento.innerHTML = `

                <div class="product-icon">

                    ${producto.emoji}

                </div>


                <div class="product-info">

                    <div class="product-name">

                        ${producto.nombre}

                    </div>


                    <div class="product-description">

                        ${producto.descripcion}

                    </div>


                    <div class="product-price">

                        $${formatoPrecio(
                            producto.precio
                        )}

                    </div>

                </div>


                <button
                    class="add-button"
                    onclick='agregarCarrito(
                        ${JSON.stringify(producto)}
                    )'>

                    +

                </button>

            `;


            contenedor.appendChild(elemento);

        });


        document
            .getElementById("menuModal")
            .classList
            .add("active");

    }

    catch(error) {

        console.error(error);

        alert(
            "No se pudo cargar el menú."
        );

    }

}


/* =========================================================
   CERRAR MENÚ
   ========================================================= */

function cerrarMenu() {

    document
        .getElementById("menuModal")
        .classList
        .remove("active");

}


/* =========================================================
   AGREGAR AL CARRITO
   ========================================================= */

function agregarCarrito(producto) {

    const existente =
        carrito.find(
            item =>
                item.id === producto.id
        );


    if (existente) {

        existente.cantidad++;

    }

    else {

        carrito.push({

            ...producto,

            cantidad: 1

        });

    }


    actualizarCarrito();


    alert(
        producto.nombre +
        " fue agregado al carrito."
    );

}


/* =========================================================
   ACTUALIZAR CARRITO
   ========================================================= */

function actualizarCarrito() {

    const cantidad =
        carrito.reduce(
            (total, item) =>
                total + item.cantidad,
            0
        );


    document.getElementById(
        "cartCount"
    ).innerText = cantidad;


    mostrarCarrito();

}


/* =========================================================
   MOSTRAR CARRITO
   ========================================================= */

function mostrarCarrito() {

    const contenedor =
        document.getElementById(
            "cartItems"
        );


    contenedor.innerHTML = "";


    if (carrito.length === 0) {

        contenedor.innerHTML = `

            <div class="empty">

                🛒

                <br><br>

                Tu carrito está vacío.

            </div>

        `;


        document.getElementById(
            "cartTotal"
        ).innerText = "$0";


        return;

    }


    let total = 0;


    carrito.forEach((item, index) => {

        const subtotal =
            item.precio *
            item.cantidad;


        total += subtotal;


        const elemento =
            document.createElement("div");


        elemento.className =
            "cart-item";


        elemento.innerHTML = `

            <div>

                <strong>

                    ${item.emoji}
                    ${item.nombre}

                </strong>

                <br>

                ${item.cantidad} ×
                $${formatoPrecio(
                    item.precio
                )}

            </div>


            <div>

                <strong>

                    $${formatoPrecio(
                        subtotal
                    )}

                </strong>

                <br><br>

                <button
                    onclick="eliminarProducto(
                        ${index}
                    )">

                    ❌

                </button>

            </div>

        `;


        contenedor.appendChild(elemento);

    });


    document.getElementById(
        "cartTotal"
    ).innerText =
        "$" + formatoPrecio(total);

}


/* =========================================================
   ELIMINAR PRODUCTO
   ========================================================= */

function eliminarProducto(index) {

    carrito.splice(index, 1);

    actualizarCarrito();

}


/* =========================================================
   ABRIR CARRITO
   ========================================================= */

function abrirCarrito() {

    mostrarCarrito();

    document
        .getElementById("cartModal")
        .classList
        .add("active");

}


/* =========================================================
   CERRAR CARRITO
   ========================================================= */

function cerrarCarrito() {

    document
        .getElementById("cartModal")
        .classList
        .remove("active");

}


/* =========================================================
   HACER PEDIDO
   ========================================================= */

function hacerPedido() {

    if (carrito.length === 0) {

        alert(
            "Tu carrito está vacío."
        );

        return;

    }


    alert(

        "🎉 ¡Pedido creado!\n\n" +

        "Esta es una versión inicial.\n\n" +

        "En la siguiente versión " +

        "agregaremos dirección, " +

        "método de pago y seguimiento."

    );


    carrito = [];

    actualizarCarrito();

    cerrarCarrito();

}


/* =========================================================
   LOGIN
   ========================================================= */

function login() {

    alert(

        "🔐 Inicio de sesión\n\n" +

        "Próximamente podrás " +

        "crear una cuenta como:\n\n" +

        "👤 Cliente\n" +

        "🏪 Restaurante\n" +

        "🛵 Domiciliario"

    );

}


/* =========================================================
   FORMATO DE DINERO
   ========================================================= */

function formatoPrecio(numero) {

    return new Intl.NumberFormat(
        "es-CO"
    ).format(numero);

}


/* =========================================================
   CERRAR MODALES AL HACER CLICK AFUERA
   ========================================================= */

window.addEventListener(
    "click",
    function(event) {

        const menuModal =
            document.getElementById(
                "menuModal"
            );


        const cartModal =
            document.getElementById(
                "cartModal"
            );


        if (event.target === menuModal) {

            cerrarMenu();

        }


        if (event.target === cartModal) {

            cerrarCarrito();

        }

    }
);


/* =========================================================
   INICIAR APP
   ========================================================= */

cargarRestaurantes();

</script>


</body>

</html>
"""


# ============================================================
# EJECUTAR SERVIDOR
# ============================================================

if __name__ == "__main__":

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )