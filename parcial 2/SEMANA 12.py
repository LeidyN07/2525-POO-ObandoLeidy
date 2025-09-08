# ============================================
# Sistema de Gestión de Biblioteca Digital
# Autor: Leidy
# ============================================

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para (título, autor), porque no cambian después de ser creados
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"[{self.isbn}] {self.info[0]} - {self.info[1]} ({self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}        # diccionario {isbn: Libro}
        self.usuarios = {}      # diccionario {id_usuario: Usuario}
        self.ids_usuarios = set()  # conjunto de IDs únicos

    # ---------------------------
    # Métodos de gestión de libros
    # ---------------------------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro con este ISBN ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No se encontró un libro con ese ISBN.")

    # ---------------------------
    # Métodos de gestión de usuarios
    # ---------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {eliminado}")
        else:
            print("No existe un usuario con ese ID.")

    # ---------------------------
    # Métodos de préstamos
    # ---------------------------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("El libro no está disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # se retira del catálogo de disponibles
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro  # vuelve a la biblioteca
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}")
                return
        print("El usuario no tiene este libro en préstamo.")

    # ---------------------------
    # Métodos de búsqueda
    # ---------------------------
    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            if "titulo" in kwargs and kwargs["titulo"].lower() in libro.info[0].lower():
                resultados.append(libro)
            elif "autor" in kwargs and kwargs["autor"].lower() in libro.info[1].lower():
                resultados.append(libro)
            elif "categoria" in kwargs and kwargs["categoria"].lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # ---------------------------
    # Listar libros prestados
    # ---------------------------
    def listar_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# ============================
# Prueba del sistema
# ============================
if __name__ == "__main__":
    # Crear la biblioteca
    biblio = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "123")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "456")
    libro3 = Libro("Python para Todos", "Raúl González", "Programación", "789")

    # Agregar libros a la biblioteca
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Leidy", "U001")
    usuario2 = Usuario("Carlos", "U002")

    # Registrar usuarios
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Prestar libros
    biblio.prestar_libro("U001", "123")
    biblio.prestar_libro("U002", "456")

    # Listar libros prestados
    biblio.listar_prestados("U001")

    # Devolver libros
    biblio.devolver_libro("U001", "123")

    # Buscar libros
    resultados = biblio.buscar_libro(autor="Raúl")
    print("Resultados de búsqueda:", [str(libro) for libro in resultados])

