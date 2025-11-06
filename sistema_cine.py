# sistema_cine.py

# ===============================================
# ESTRUCTURAS DE DATOS PERSONALIZADAS
# ===============================================

## LISTA ENLAZADA SIMPLE
class NodoLista:
    """Nodo básico para la implementación de MiLista."""
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class MiLista:
    """Implementación de una Lista Enlazada Simple."""
    def __init__(self):
        self.primero = None
        self.contador = 0
    
    def agregar(self, valor):
        """Agrega un nuevo nodo al final de la lista (O(n))."""
        nuevo = NodoLista(valor)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            # Recorre hasta el último nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.contador += 1
    
    def mostrar(self):
        """Devuelve una lista estándar de Python con los valores."""
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
    
    def __len__(self):
        return self.contador

## ÁRBOL BINARIO DE BÚSQUEDA (BST)
class NodoArbol:
    """Nodo básico para el Árbol Binario."""
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolFunciones:
    """Implementación de un Árbol Binario de Búsqueda para almacenar Funciones."""
    def __init__(self):
        self.raiz = None
    
    def insertar(self, dato):
        """Método público para insertar un dato (una Funcion) en el BST."""
        self.raiz = self._insertar(self.raiz, dato)
    
    def _insertar(self, nodo, dato):
        """Método recursivo para insertar. Ordena según el método __lt__ de la clase Funcion (por hora)."""
        if nodo is None:
            return NodoArbol(dato)
        
        # Si el dato es menor que el dato del nodo (usa __lt__ en Funcion) va a la izquierda
        if dato < nodo.dato:
            nodo.izq = self._insertar(nodo.izq, dato)
        # Si es mayor o igual, va a la derecha
        else:
            nodo.der = self._insertar(nodo.der, dato)
        
        return nodo
    
    def en_orden(self):
        """Realiza un recorrido In-Order para obtener las Funciones ordenadas (por hora)."""
        resultado = MiLista() # Utiliza la lista enlazada personalizada
        self._en_orden(self.raiz, resultado)
        return resultado
    
    def _en_orden(self, nodo, lista):
        """Método recursivo para el recorrido In-Order (Izquierda -> Raíz -> Derecha)."""
        if nodo:
            self._en_orden(nodo.izq, lista)
            lista.agregar(nodo.dato)
            self._en_orden(nodo.der, lista)

## DICCIONARIO SIMPLE (HASH MAP)
class DiccionarioSimple:
    """Clase envoltorio para el diccionario nativo de Python."""
    def __init__(self):
        self.datos = {}
    
    def poner(self, clave, valor):
        """Inserta o actualiza un par clave-valor."""
        self.datos[clave] = valor
    
    def obtener(self, clave):
        """Devuelve el valor asociado a la clave o None si no existe."""
        return self.datos.get(clave)
    
    def existe(self, clave):
        """Verifica si una clave está en el diccionario."""
        return clave in self.datos

# ===============================================
# CLASES DE ENTIDADES DEL CINE
# ===============================================

class Pelicula:
    """Representa una película."""
    def __init__(self, id, titulo, genero, duracion):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
    
    def __str__(self):
        return f"{self.titulo} ({self.duracion}min) - ID: {self.id}"
    
    def __lt__(self, otro):
        """Define el criterio de comparación (menor que) basado en el título."""
        return self.titulo < otro.titulo

class Sala:
    """Representa una sala de cine con sus asientos."""
    def __init__(self, numero, filas, columnas):
        self.numero = numero
        self.filas = filas
        self.columnas = columnas
        # Matriz 2D: Inicializa todos los asientos como False (libres)
        self.asientos = [[False] * columnas for _ in range(filas)]
        
    
    def reservar(self, fila, columna):
        """Intenta reservar un asiento (coordenadas numéricas). Devuelve True si fue exitoso."""
        if 0 <= fila < self.filas and 0 <= columna < self.columnas and not self.asientos[fila][columna]:
            self.asientos[fila][columna] = True
            return True
        return False
    
    def liberar(self, fila, columna):
        """Libera un asiento previamente reservado."""
        if 0 <= fila < self.filas and 0 <= columna < self.columnas and self.asientos[fila][columna]:
            self.asientos[fila][columna] = False
            return True
        return False
    
    def disponibles(self):
        """Calcula el número de asientos disponibles (libres)."""
        contador = 0
        for fila in self.asientos:
            for asiento in fila:
                if not asiento:
                    contador += 1
        return contador
    
    def dibujar_asientos(self):
        """Imprime una representación visual de la sala (O=libre, X=reservado)."""
        print("   " + " ".join(str(i+1) for i in range(self.columnas)))
        for i, fila in enumerate(self.asientos):
            # Convierte el índice de fila (0, 1, 2...) a letra (A, B, C...)
            print(f"{chr(65+i)} " + " ".join("X" if a else "O" for a in fila))

class Funcion:
    """Representa una proyección específica de una película en una sala y hora."""
    def __init__(self, id, pelicula, sala, hora, precio):
        self.id = id
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora
        self.precio = precio
    
    def __str__(self):
        return f"[ID: {self.id}] {self.pelicula.titulo} - Sala {self.sala.numero} - {self.hora.strftime('%d/%m %H:%M')} - Precio: ${self.precio}"
    
    def __lt__(self, otro):
        """Define el criterio de ordenamiento del BST (por hora de inicio)."""
        return self.hora < otro.hora

class Usuario:
    """Representa un usuario del sistema."""
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.reservas = MiLista() # Almacena las reservas del usuario en una lista enlazada
    
    def agregar_reserva(self, reserva):
        """Añade una reserva a la lista personal del usuario."""
        self.reservas.agregar(reserva)

class Reserva:
    """Representa una reserva de entradas."""
    def __init__(self, id, usuario, funcion, asientos):
        self.id = id
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos # Lista de strings de asientos (ej: ['A1', 'B2'])
        self.total = len(asientos) * funcion.precio
        self.activa = True
    
    def cancelar(self):
        """Marca la reserva como inactiva."""
        self.activa = False

# ===============================================
# CLASE PRINCIPAL DEL SISTEMA
# ===============================================

class Cine:
    """Clase principal que gestiona el sistema completo del cine."""
    def __init__(self):
        # Diccionario: clave=ID/Email, valor=Objeto (acceso rápido)
        self.peliculas = DiccionarioSimple()
        self.usuarios = DiccionarioSimple()
        self.reservas = DiccionarioSimple()
        
        # Árbol Binario de Búsqueda: almacena funciones ordenadas por hora
        self.funciones = ArbolFunciones() 
        
        # Contadores para IDs
        self.proxima_reserva = 1
        self.proximo_usuario = 1
        
        self._cargar_datos_prueba()
    
    def _cargar_datos_prueba(self):
        """Inicializa algunas películas, salas y funciones de ejemplo."""
        # Películas
        pelis = [
            Pelicula("P1", "Avengers", "Acción", 150),
            Pelicula("P2", "Toy Story", "Animación", 100),
            Pelicula("P3", "El Rey León", "Animación", 118)
        ]
        for p in pelis:
            self.peliculas.poner(p.id, p)
        
        # Salas (Matriz 2D 4x6 y 5x8)
        self.sala1 = Sala(1, 4, 6) # Filas: A-D, Columnas: 1-6
        self.sala2 = Sala(2, 5, 8) # Filas: A-E, Columnas: 1-8
        
        # Funciones
        from datetime import datetime, timedelta
        
        funciones = [
            # Se almacenan en el BST y se ordenan por el objeto 'hora'
            Funcion("F1", pelis[0], self.sala1, datetime.now() + timedelta(hours=2), 10.0),
            Funcion("F2", pelis[1], self.sala2, datetime.now() + timedelta(hours=4), 8.5),
            Funcion("F3", pelis[2], self.sala1, datetime.now() + timedelta(days=1), 9.0)
        ]
        
        for f in funciones:
            self.funciones.insertar(f) # Inserta en el BST
    
    def registrar_usuario(self, nombre, email):
        """Registra un nuevo usuario si el email no existe (búsqueda O(1) en el diccionario)."""
        if self.usuarios.existe(email):
            return None
        
        id_usuario = f"U{self.proximo_usuario}"
        self.proximo_usuario += 1
        
        usuario = Usuario(id_usuario, nombre, email)
        self.usuarios.poner(email, usuario) # Almacena por email para un fácil inicio de sesión
        return usuario
    
    def hacer_reserva(self, email, id_funcion, asientos):
        """
        Procesa la lógica de reserva:
        1. Valida usuario.
        2. Busca la función (recorrido del BST O(n) en el peor caso si el BST está desequilibrado).
        3. Intenta reservar los asientos en la matriz 2D de la sala.
        4. Crea la reserva y la asocia al usuario.
        """
        usuario = self.usuarios.obtener(email)
        if not usuario:
            print("Error: Usuario no encontrado.")
            return None
        
        # Búsqueda de la función: Itera sobre el resultado en orden del BST
        funcion_encontrada = None
        todas_funciones = self.funciones.en_orden() # Obtiene MiLista con funciones ordenadas
        for funcion in todas_funciones.mostrar():
            if funcion.id == id_funcion:
                funcion_encontrada = funcion
                break
        
        if not funcion_encontrada:
            print("Error: Función no encontrada.")
            return None
        
        # Verificar y reservar asientos
        for asiento in asientos:
            try:
                # Conversión de A1 -> (0, 0)
                letra = asiento[0].upper()
                numero = int(asiento[1:]) - 1 # Columna (0-index)
                fila = ord(letra) - ord('A') # Fila (0-index)
                
                # Intenta reservar en la matriz de la sala
                if not funcion_encontrada.sala.reservar(fila, numero):
                    print(f"Error: Asiento {asiento} no disponible o inválido.")
                    # Lógica de rollback: si falla, se liberan los asientos ya reservados en esta operación
                    for rollback_asiento in asientos:
                         if rollback_asiento != asiento: # Solo liberar los anteriores
                            rb_letra = rollback_asiento[0].upper()
                            rb_numero = int(rollback_asiento[1:]) - 1
                            rb_fila = ord(rb_letra) - ord('A')
                            funcion_encontrada.sala.liberar(rb_fila, rb_numero)
                    return None
            except (ValueError, IndexError):
                print(f"Error: Formato de asiento {asiento} incorrecto.")
                return None
        
        # Crear reserva
        id_reserva = f"R{self.proxima_reserva}"
        self.proxima_reserva += 1
        
        reserva = Reserva(id_reserva, usuario, funcion_encontrada, asientos)
        self.reservas.poner(id_reserva, reserva)
        usuario.agregar_reserva(reserva)
        
        return reserva
    
    def cancelar_reserva(self, id_reserva):
        """Cancela una reserva y libera los asientos en la matriz de la sala."""
        reserva = self.reservas.obtener(id_reserva)
        if reserva and reserva.activa:
            reserva.cancelar()
            # Liberar asientos en la sala (Matriz 2D)
            for asiento in reserva.asientos:
                letra = asiento[0].upper()
                numero = int(asiento[1:]) - 1
                fila = ord(letra) - ord('A')
                # La función libera el asiento en la matriz de la sala
                reserva.funcion.sala.liberar(fila, numero)
            return True
        return False
    
    # Métodos de menú y visualización (sin cambios relevantes)
    def mostrar_menu(self):
         # ... (código del menú)
        while True:
            print("\n=== CINE UNIVERSITARIO ===")
            print("1. Ver películas")
            print("2. Ver funciones")
            print("3. Registrarse")
            print("4. Hacer reserva")
            print("5. Cancelar reserva")
            print("6. Ver asientos")
            print("7. Salir")
            
            op = input("Opción: ")
            
            if op == "1":
                self.mostrar_peliculas()
            elif op == "2":
                self.mostrar_funciones()
            elif op == "3":
                self.registrar_usuario_menu()
            elif op == "4":
                self.reservar_menu()
            elif op == "5":
                self.cancelar_menu()
            elif op == "6":
                self.mostrar_asientos()
            elif op == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida")
    
    def mostrar_peliculas(self):
        print("\n--- PELÍCULAS ---")
        for clave in self.peliculas.datos:
            peli = self.peliculas.datos[clave]
            print(f"- {peli}")
    
    def mostrar_funciones(self):
        print("\n--- FUNCIONES ---")
        # El recorrido en orden garantiza que las funciones salgan ordenadas por hora
        funciones = self.funciones.en_orden()
        for funcion in funciones.mostrar():
            print(f"- {funcion}")
    
    def registrar_usuario_menu(self):
        print("\n--- REGISTRO ---")
        nombre = input("Nombre: ")
        email = input("Email: ")
        
        usuario = self.registrar_usuario(nombre, email)
        if usuario:
            print(f"✅ Usuario {usuario.id} registrado")
        else:
            print("❌ Email ya existe")
    
    def reservar_menu(self):
        print("\n--- RESERVA ---")
        email = input("Tu email: ")
        self.mostrar_funciones()
        
        id_funcion = input("ID función: ")
        self.mostrar_asientos_funcion(id_funcion)
        
        asientos_str = input("Asientos (ej: A1,B2): ")
        asientos = [a.strip().upper() for a in asientos_str.split(",")]
        
        reserva = self.hacer_reserva(email, id_funcion, asientos)
        if reserva:
            print(f"✅ Reserva {reserva.id} creada - Total: ${reserva.total}")
        else:
            print("❌ Error en reserva (Usuario/Función no existe, o asientos ya ocupados/inválidos).")
    
    def cancelar_menu(self):
        print("\n--- CANCELAR ---")
        id_reserva = input("ID reserva: ")
        if self.cancelar_reserva(id_reserva):
            print("✅ Reserva cancelada")
        else:
            print("❌ No se pudo cancelar (ID no encontrado o ya cancelada)")
    
    def mostrar_asientos(self):
        print("\n--- ASIENTOS SALA 1 ---")
        self.sala1.dibujar_asientos()
        print("\n--- ASIENTOS SALA 2 ---")
        self.sala2.dibujar_asientos()
    
    def mostrar_asientos_funcion(self, id_funcion):
        funcion_encontrada = None
        todas_funciones = self.funciones.en_orden()
        for funcion in todas_funciones.mostrar():
            if funcion.id == id_funcion:
                funcion_encontrada = funcion
                break
        
        if funcion_encontrada:
            print(f"\nAsientos para {funcion_encontrada.pelicula.titulo} (O=Libre, X=Reservado):")
            funcion_encontrada.sala.dibujar_asientos()
        else:
            print("Función no encontrada.")

# Ejecutar el sistema
if __name__ == "__main__":
    mi_cine = Cine()
    mi_cine.mostrar_menu()