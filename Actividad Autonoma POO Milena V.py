#Estudiante:Milena Valarezo
#Programacion Orientada a Objectos
#Numericos
edad, _peso = 50, 70,5
#String
nombres = 'Daniel Vera'
dirDomiciliaria= "Chile y Guayaquil"
Tipo_sexo = 'M'
#Colecciones
usuario = ('dchiki','1234','chiki@gmail.com')
materias =['Programacion Web','PHP','POO']
docente = {'nombre':'Daniel','edad':50,'fac':'faci'}
# Imprimir 
print("""Mi nombre es {}, tengo {}
años""".format(nombres,edad))
print(usuario,materias,docente)

####
x=int(input("Escriba un numero entero:"))
if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Uno')
else:
    print('Ninguna opcion')

print("Ok") if type(x) == int else print("-")


####
""" uso de while infinito """
c = 1
while True:
    print(C)
# while validacion 
vocal = input("Ingrese la vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal == ',':
        break
    vocal = input("Vocal:")
print('Su vocal o punto es:{}'.format(vocal))


####
# for range(v)-range(vf,vf) -range(vf,vf,inc)
frase = input("Ingrese una frase: ")
for indice in range(len(frase)):
# for in cadena - in(tupla)-in[lista]
 for car in frase:
    if car in ["a","e","i","o","u","A","E","I","O","U"]:
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print('cantidad vocales:{}'.format(cvoc))
# Comprehension - [var for in datos condicion]
[car for car in['a','e','i','o','u'] if car not in ["a","i","o")]


####
# funciones sin retornos #
def vocales(frase):
    for car in frase:
        it car in('a','e','i','o','u'):
           print(car)
# Llamadas a funcion #
oracion = input('Ingrese oracion: ')
vocales(oracion.lower())
# funciones con retorno de valor #
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)
# Llamadas a funcion #
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
print['Promedio: {} = {}'.format(listanotas,prom))

####
# funciones matematicas #
import math
num1, num2, num, men = 12.572, 15.4, 4, '1234'
print(math.cell(num1). '/t',math.floor(num1))
print(round(num1.1),'/t',type(num),'/t',type(men))
# funciones de cadenas #
mensaje= 'Hola' + 'mundo' + 'Python'
men1=mensaje.split()
men2=''.join(men1)
print(mensaje(0),mensaje(0:4),men1.men2)
print(mensaje.find('mundo'),mensaje,lower())
# funciones de fecha #
from datetime import datetime,timedelta,data
hoy,fdia = datetime.now().date.today()
futuro = hoy + timedelta(days=30)
dif, aa, mm, dd = futuro - hoy,hoy:year,hoy.month,hoy.day
fecha = date(aa, mm, dd+2)
print(hoy,fdia,futuro,dif,fecha)
# Sintaxis

# num=20
# if type(num) == int:
#     print("respuesta: ",num*2)
# else:
#     print("El dato no es numerico")

# def mensaje(men):
#     print(men)

# mensaje("Mi primer programa")
# mensaje("Mi segundo programa")

# class Sintaxis:
#     def useVariables(self):
#         edad, _peso = 50, 70.50
#         print(edad,_peso)


class Sintaxis:
    instancia=0 #variables de clases(opcional)
    #__init__ Metodo contructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que presenta la clase creada
    def __init__(self,datos="Inicializacion"):
        self.frase=datos
        Sintaxis.instancia = Sintaxis.instancia+1


    def usoVariable(self):
        edad, _peso = 50, 70.5
        nombres = 'Daniel Vera'
        Tipo_sexo = 'M'
        civil = True
        print(nombres,edad)


# tuplas = () son colecciones de datos de cualquier tipo inmutables
usuario=()
usuario = ('dchiki','1234','chiki@gmail.com')
#usuario[3]="milagro"
#listas = [] colecciones mutables
materias = ['Programacion Web', 'PHP', 'POO']
materias[1]="Python"
materias.append("Go")
# diccionarios = {} colecciones de objetos clave:valor tipo json
docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
# presentacion con format 
print("""Mi nombre es{}, tengo {}
        años""".format(nombres, edad))
usuario = ('dchiki','1234','chiki@gmail.com')
#usuario[3]="milagro"
#listas = [] colecciones mutables
materias = ['Programacion Web', 'PHP', 'POO']
materias[1]="Python"
materias.append("Go")
# diccionarios = {} colecciones de objetos clave:valor tipo json
docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
docente['carrera']='CS"
# presentacion con format
# print("""Mi nombre es {}, tengo {}
#         años""".format(nombres, edad))
#print(usuario,materias,docente)
#print(usuario,usuario[0],usuario[0:2],usuario[-1])
#print(materias,materias[2:],materias[:3],materias[:],materias[-2:] )
print(docente,docente['nombre'])


ejer1 = Sintaxis()
ejer1.usoVariable()
print(ejer1.frase)

# Condiciones y ciclos 

class Sintaxis:
    contador=0 #variables de clases(opcional)
    #__init__ Metodo contructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que presenta la clase creada
    def __init__(self,num1=0,num2=1):
        self.numero1=num1# variables de instancia
        self.numero2=num2
        numero = num1+num2
        self.numero3 = numero
        # variables de instancia 

    def usoIf(self):
        # if ... elif ... else ...: permiten condicionar de uno o varios bloques 
        # de sentencias al cimplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
            print("numero1:{}, numero2:{}: son iguales".format(self.numero1,self.numero2"))
        elif self.numero == self.numero3:
             print("numero1:{}, numero2:{}: son iguales".format(self.numero1,self.numero3)) 
        else:
            print("no son iguales")

# usar clase 
cond1 = Condicion(8)
print(cond1.numero1)
print(codn1.numero2)

cond2 = Condicion(20,45)
cond2.usoIf() # llamada a un metodo de la clase   
print(cond2.numero2) # llamada a un atributo de la clase

##Clase
class Mascota(object):
    def __init__(self,Nombre,Raza,Tamaño)
    self.Nombre= Nombre
    self.Raza= raza
    self.Tamaño= Tamaño
def darNombre(self):
    return self.Nombre

def darRaza(self):
    return self.Raza

def darTamaño(self):
    return self.Tamaño

def __str__(self):
    return "%s es un %s" % (self.Nombre, self.Raza, self.Tamaño)


