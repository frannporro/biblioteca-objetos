class libro:
    def __init__(self, titulo, autor ):#constructor
        self.titulo=titulo
        self.autor=autor
        self.disponible=True
    
    def prestado(self):
        if self.disponible:
            self.disponible=False
            print(f"el libro {self.titulo} ha sido prestado")
        else:
            print("no está disponible")
    
    def devolver(self):
        self.disponible=True
        print(f"el libro {self.titulo} ha sido devuelto")

class usuario:
    def __init__(self, nombre, id):
        self.nombre= nombre
        self.id= id
        self.librosprestados=[]
    
    def prestar(self, libro):
        if libro.disponible:
            libro.disponible=False
            self.librosprestados.append(libro)
        else:
            print(f"el libro {libro.titulo} no está disponible")

class biblioteca:
    def __init__(self):
        self.libros=[]
        self.usuarios=[]
    
    def añadirlibro(self, libro):
        self.libros.append(libro)
        print(f"el libro {libro.titulo} ha sido agregado")

    def registrousuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"el usuario {usuario.nombre} ha sido registrado") 
    
    def disponibles(self):
        print("libros disponibles: ")
        for libro in self.libros:    
            if libro.disponible:
                print(f"{libro.titulo} por autor: {libro.autor}")

#creo los libros
libro1=libro("otras inquisiciones", "jorge luis borges")
libro2=libro("bestiario", "cortazar")
libro3=libro("sueño de una noche de verano", "shakespeare")

#creo los usuarios
usuario1= usuario("francisco", "0001")
usuario2=usuario("pedro", "0002")
usuario3=usuario("juana", "0003")

#crear biblioteca

biblioteca=biblioteca()
biblioteca.añadirlibro(libro1)
biblioteca.añadirlibro(libro2)
biblioteca.añadirlibro(libro3)
biblioteca.registrousuario(usuario1)
biblioteca.registrousuario(usuario2)

#muestra libros
biblioteca.disponibles()

#prestamo

usuario1.prestar(libro1)
usuario2.prestar(libro2)
#chequear
biblioteca.disponibles()

#chequear
usuario3.prestar(libro1)

#devolver

libro.devolver(libro1)
#chequeo
biblioteca.disponibles()