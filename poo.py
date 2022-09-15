class Humano:
    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre
        
    def hablar(self):
        print('hola', nombre, ',te doy un gran saludo y no puedo creer que tienes', edad , 'años')

nombre = input('Escriba su nombre: ')
edad = int(input('Hola escriba su edad: '))

sujeto = Humano(nombre, edad)

sujeto.hablar()

