class For:
    def _init_(self):
        pass
    #ciclo repetitivo de incrementos o decrementos se ejecutan por verdadero
    def usoFor(self):
        datos=["Nicole", 20,True]
        numeros=(2,5,6,4,1)
        docente= {'nombre': 'Nicole', 'Edad':20, 'Fac': 'faci'}
        listaNotas=[(30,40),[20,40],(50,40)]
        listaAlumnos=[{"nombre": "Joel","final":70},{"nombre": "natanael","final":80},{"nombre": "Joao","final":50}]
        #? range([inicio=0],limite,[inc/dec=1]). genera un rago de valores desde un valor inicial a un valor 
        #* se ejecuta desde inicio hasta el limite
        # for i in range (S):  # rango (0,1,2,3,4)
        #     print("i={}".format(i))
        # for i in range (2,10): rango(2,3,4,5,6,7,8,9)
        #     print("i={}".format(i))
        # for i in range(4,10,2): # rango(4,6,8)
        #     print("i={}".format(i),end=" ")
        # for i in range(12,3,-3): # rango(4,6,8)
        #     print("i={}".format(i),end=" ")
        # longitud= len(datos)
        # print(datos[0])
        # print(datos[1])
        # print(datos[2])
        # j=0
        # while j< longitud:
        #     print("for", datos[j])
        #     j=j+1

        # for i in range(longitud-1,-1,-1):
        #     print("for",datos[i])
        # for i, dato in enumerate(datos):
        #     print("for",i,dato)
        #     #dato toma cada elemento de la coleccion numeros (cadena, list,tupla)
        # for dato in numeros:
        #     print(dato)
        # for dato in ['H','o','l','a','que', 'tal']:
        #         print(dato)
        print("/n diccionario de notas")
        # for clave,valor in docente.items():
        #     print(clave,":",valor,end="")
        # for alumnos in listaAlumno:
        #     for clave, valor in alumnos.items():
        #         print(clave,":",valor,end="")
        # listaNotas= [(30,40),[20,40,20],(50,40,20,10,5)]
        # acum=0
        # long=0 
        # for notas in listaNotas:
        #     parcial=0
        #     print(notas, end=="  ")
        #     for  nota in notas:
        #         print(nota)
        #         long= long+1
        #         acum= acum+ nota
        #         parcial+= nota
        #         promParcial= parcial/len(notas)
        #     print("Notas parciales ={} Promedio Parcial={}".format(parcial,promParcial))
        #     prom= acum/long
        #     print("Total de promedio={} - notas={}: Promedio={} ".format(acum, long, prom))
#         listaAlumnos=[{"nombre": "Joel","final":70},{"nombre": "natanael","final":80},{"nombre": "Joao","final":50}]
#         acum=0
#         cont=0
#         for alumnos in listaAlumnos:
#             print(alumnos)
#             for clave, valor in alumnos.items():
#                 print(clave,":", valor, end="")
#                 if clave== "final": acum= acum+ valor 
#             cont+=1
#             print(acum/cont)

        frase = "Hola como estas"
        # vocales=[]
        # for car in frase :
        #     if car in ('a','e','i','o','u'):
        #         vocales.append(car)
        #     print(vocales)
            
        print([car for car in "Hola como estas" if car in('a','e','i','o','u')] )



bucle1= For()
bucle1.usoFor()