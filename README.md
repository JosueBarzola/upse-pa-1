
# Documentación del Proyecto: Sistema de Gestión de Cine

## 1. Descripción del Proyecto

[cite_start]El proyecto **Sistema de Gestión de Cine** es una aplicación de consola en Python diseñada para simular la operación de un cine universitario, enfocándose en la gestión de **películas, funciones, usuarios y el proceso de reserva de asientos**[cite: 3].

[cite_start]La solución implementa diversas **Estructuras de Datos Abstractas (TDA)** fundamentales (Lista Enlazada, Árbol Binario de Búsqueda y Tablas Hash/Diccionarios) [cite: 4] [cite_start]para cumplir con objetivos pedagógicos y de rendimiento[cite: 4]. [cite_start]Permite a los usuarios registrarse, ver la cartelera ordenada por hora, reservar asientos en tiempo real (utilizando una matriz 2D para la sala) y cancelar reservas[cite: 5].

[cite_start]**Problemática abordada:** Gestionar eficientemente la disponibilidad de funciones, el *mapping* de asientos en salas y el registro de transacciones de reserva, priorizando la **rapidez de acceso** a las entidades clave[cite: 6].

***

## 2. Diagrama de Clases UML

[cite_start]El sistema está compuesto por clases que representan las estructuras de datos y las entidades de negocio[cite: 8].

### Relaciones Clave:

* [cite_start]**Composición (Fuerte):** [cite: 10]
    * [cite_start]`MiLista` $\longleftarrow$ `NodoLista`: La lista no existe sin sus nodos[cite: 12, 13].
    * [cite_start]`ArbolFunciones` $\longleftarrow$ `NodoArbol`: El árbol no existe sin sus nodos[cite: 14].
    * [cite_start]`Usuario` $\longleftarrow$ `MiLista` (de Reservas): El listado interno de reservas pertenece exclusivamente al usuario[cite: 15].
* **Agregación (Débil):**
    * [cite_start]`Funcion` $\longrightarrow$ `Pelicula`, `Sala`: Una Función utiliza una Película y una Sala, pero estas existen independientemente[cite: 17, 18, 19].
    * [cite_start]`Reserva` $\longrightarrow$ `Usuario`, `Funcion`: Una Reserva se asocia a un Usuario y una Función, pero estas entidades existen por separado[cite: 20].
* **Asociación/Uso:**
    * [cite_start]`Cine` utiliza las estructuras `DiccionarioSimple` y `ArbolFunciones` para gestionar sus colecciones de entidades[cite: 22].


***

## 3. Justificación de Diseño

### A. Jerarquía de Herencia

[cite_start]Se optó por una estructura de **composición e implementación modular** en lugar de una jerarquía de herencia profunda[cite: 25].

[cite_start]**Justificación:** Se consideró que la herencia no aportaba un beneficio significativo, ya que las entidades de negocio (`Pelicula`, `Sala`, `Funcion`, etc.) son conceptualmente distintas y no comparten un comportamiento base complejo que requiera ser generalizado[cite: 26].

* [cite_start]En su lugar, se utilizó la **composición** (ej: `Funcion` tiene una `Pelicula` y una `Sala`, `Usuario` tiene una `MiLista` de Reservas) para modelar las relaciones del mundo real de manera más clara y flexible[cite: 27].
* [cite_start]Las estructuras de datos (`MiLista`, `ArbolFunciones`) son clases independientes diseñadas para ser reutilizadas por las clases del negocio (`Usuario`, `Cine`)[cite: 28].

### B. Selección de Estructuras de Datos (TDA)

[cite_start]Se seleccionó cada TDA con el objetivo principal de optimizar la **velocidad de acceso** y el **ordenamiento automático** de los datos según los requerimientos de la aplicación[cite: 30].

| Entidad Gestionada | TDA Seleccionado | Justificación de Rendimiento |
| :--- | :--- | :--- |
| **Películas, Usuarios, Reservas** | **Diccionario Simple (Tabla Hash)** | [cite_start]Permite un tiempo de acceso, inserción y verificación de existencia (**Búsqueda $O(1)$**) para estas entidades[cite: 31]. [cite_start]Se utiliza la clave (ID para Películas/Reservas, Email para Usuarios) para una recuperación instantánea[cite: 31]. |
| **Funciones** | **Árbol Binario de Búsqueda (BST) (`ArbolFunciones`)** | [cite_start]Las funciones deben mostrarse al usuario **ordenadas por hora**[cite: 31]. [cite_start]El BST mantiene automáticamente el orden a medida que se insertan[cite: 31]. [cite_start]El recorrido **In-Order** garantiza una lista de funciones cronológicamente ordenada con un coste de $O(n)$[cite: 31]. |
| **Asientos de Sala** | **Matriz 2D (`Sala.asientos`)** | [cite_start]La representación física de la sala es una cuadrícula[cite: 31]. [cite_start]La matriz 2D proporciona un **acceso directo** ($O(1)$) a cualquier asiento por sus coordenadas (fila, columna), esencial para la reserva y liberación rápida[cite: 32]. |
| **Reservas por Usuario** | **Lista Enlazada (`MiLista`)** | [cite_start]Se eligió una lista enlazada simple por su simplicidad[cite: 32]. [cite_start]Las operaciones principales son solo **agregar al final** ($O(n)$ pero rápido para listas pequeñas) y **mostrar** (recorrido $O(n)$), sin requerir una búsqueda eficiente en la colección personal[cite: 32]. |

***

## 4. Manual de Usuario

### Requisitos

* [cite_start]**Python 3.x** instalado[cite: 35].

### Ejecución del Programa

1.  **Clonar/Descargar el Repositorio:**
    ```bash
    git clone [https://github.com/luvitovi/upse-pa-1](https://github.com/luvitovi/upse-pa-1)
    cd upse-pa-1
    ```
2.  **Ejecutar el Script Principal:**
    [cite_start]El sistema se ejecuta directamente desde la terminal[cite: 41].
    ```bash
    python sistema_cine.py
    ```

### Interfaz y Operación

[cite_start]Al ejecutar el programa, se mostrará el menú principal[cite: 44]:

````

\=== CINE UNIVERSITARIO ===

1.  [cite\_start]Ver películas [cite: 46]
2.  [cite\_start]Ver funciones [cite: 47]
3.  [cite\_start]Registrarse [cite: 48]
4.  [cite\_start]Hacer reserva [cite: 49]
5.  [cite\_start]Cancelar reserva [cite: 50]
6.  [cite\_start]Ver asientos [cite: 51]
7.  [cite\_start]Salir [cite: 52]
    Opción:

<!-- end list -->

```

### Pasos Típicos:

1.  [cite_start]**Registrarse (Opción 3):** Es necesario antes de reservar[cite: 55]. [cite_start]El email se usa como clave única[cite: 56].
2.  **Ver Funciones (Opción 2):** Muestra la cartelera. [cite_start]Las funciones están **ordenadas cronológicamente** (gracias al BST) y se muestra su ID (ej: F1, F2)[cite: 57].
3.  [cite_start]**Hacer Reserva (Opción 4):** [cite: 58]
    * [cite_start]Se solicita el Email del usuario[cite: 59].
    * [cite_start]Se pide el ID de la función (ej: F1)[cite: 61].
    * [cite_start]Se muestra el mapa de asientos ($\text{O}=$ Libre, $\text{X}=$ Reservado)[cite: 62].
    * [cite_start]Se ingresan los asientos deseados separados por coma (ej: `A3, B4`)[cite: 63]. [cite_start]**Importante:** Las filas se nombran con letras (A, B, C...) y las columnas con números (1, 2, 3...)[cite: 64].
4.  [cite_start]**Ver Asientos (Opción 6):** Muestra el estado de la Sala 1 y la Sala 2 para una revisión general de la ocupación[cite: 65].

***

Puedes guardar este contenido en un archivo llamado **`README.md`** y subirlo a tu repositorio para que la documentación sea visible inmediatamente en GitHub.
```