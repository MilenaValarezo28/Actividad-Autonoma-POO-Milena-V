class Ejercicios_Deber:
    def __init__(self):
        pass
    
    #1) Diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera.
    def CalcularRadio(self):
        Re = float(input("ingrese el radio del circulo: "))
        pi = 3.1416
        s = pi*Re**2
        print("La superficie obtenida del circulo es:{} ".format(s))

    #2) En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
    # cuánto deberá pagar finalmente por su compra
    def DescuentoT(self):
        To = float(input("Escriba el total de la compra: "))
        d = To*0.15
        Fc = To-d
        print("El total a pagar es: {} ".format(Fc))

    #3) Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
    #El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por
    #las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta 
    #su sueldo base y sus comisiones.
    def Ventas(self):
        for x  in range(4):
            Sa = float(input("Ingrese su Salario Mensual: "))
            v1 = float(input("Igrese el valor de mi primer venta: "))
            v2 = float(input("Ingrese el segundo valor de la venta: "))
            v3 = float(input("Ingrese el tercer valor de la venta: "))
            To = v1+v2+v3
            Co = To*0.1
            Tv = round(To+Co,2) 
            print("El total obtenido por comision es:{} ".format(Tv))

    #4) Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen.
    def CalificacionEx(self):
        c = float(input("Ingrese su calificacion: "))
        if c >= 7:
            print("Has aprobado ")
        
    #5) Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación 
    # es mayor o igual que 7 y “Reprobado” en caso contrario.
    def CalificacionEx2(self):
        c = float(input("Ingrese su calificacion: "))
        if c >= 7:
            print("Aprobado")
        else:
            print("Reprobado")

    #6) Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
    # si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
    def SueldoEmpl(self):
        s = float(input("Ingrese el sueldo del empleado: "))
        if s < 600:
            n = s+s*0.1
            print("El sueldo nuevo a pagar es {}".format(n))
        else:
            print("Su sueldo sigue siendo de {}".format(s))

    #7) Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas 
    # en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas 
    # extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras 
    # exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.
    def HorasExtras(self):
        H = int(input("Ingrese el numero de horas trabjadas: "))
        P = float(input("Ingrese el valor a pagar por hora: "))
        if H > 48:
            t = H - 48
            d = 8
            s = 40*P + d*P*2 + t*P*3
            print("El Total a pagar por las horas trabajadas es : {}".format(s))
        elif H < 40:
            d = H-40
            s = 40*P + d*P*2
            print("El Total a pagar por las horas trabajadas es : {}".format(s))
        else:
            s = H*P
            print("El Total a pagar por las horas trabajadas es : {}".format(s))
           
    #8) Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
    def NumEnteros(self):
        N1=float(input("Ingrese el primer numero: "))
        N2=float(input("Ingrese el segundo numero: "))
        N3=float(input("Ingrese el tercer numero: "))
        if N2<N1>N3:
            print('El numero mayor de los 3 es: {}'.format(N1))
        elif N1<N2>N3:
            print('El numero mayor de los 3 es: {}'.format(N2))
        elif N1<N3>N2:
            print('El numero mayor de los 3 es: {}'.format(N3))
        else:
            print('Todos los numeros son iguales')

    #9) Diseñar un algoritmo tal que, dados como datos dos variables de tipo entero,obtenga el resultado de la 
    #siguiente función.
    def Variables(self):
        v= int(input('Ingrese el valor dado de v: '))
        num= int(input('Ingrese el valor de num: '))
        if num == 1:
            C= 100 * v
        elif num == 2:
            C= 100 ^ v
        elif num == 3:
            C= 100 / v 
        else:
            C = 0
        print('La respuesta es {}'.format(C))

    #10) Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones 
    #denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes 
    #es aceptado; en caso contrario es rechazado.
    def ExamAs(self):
        C1=int(input('Ingrese la primera calificacion: '))
        C2=int(input('Ingrese la segunda calificacion: '))
        if C1 >= 80 and C2 >= 80:
            print('Usted a sido Aceptado')
        else:
            print('Usted a sido Rechazado')

    #11) Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
    def SumaCuadrados(self):
        Suma= 0
        i= 1
        for i in range (100):
            Suma= Suma + i * i 
        i= 2
        Suma= Suma + i * i
        i= 3
        Suma= Suma + i * i
        print(Suma)

    #12) Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100.
    def Number(self):
        i = 0
        while i<100:   
            i += 1
            print(i)

    #13) Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
    #utilizando un bucle controlado por el usuario.
    def Bucle(self):
        Suma= 0
        P= 1
        n= 'y'
        while n != "n" and n != "N":
            num= int(input('Ingrese el valor de N: '))
            Suma += num
            P *= num
            n = input('Desea continuar calculando(S/N)' )
        print("El total de la suma es:{}".format(P))
        print("El producto total es:{}".format(Suma))

    #14) Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
    #utilizando un bucle controlado por centinela.
    def Enteros(self):
        sum = 0
        P = 1
        n = int(input("Ingrese el valor de N: "))
        while n != -1:
            sum += 1
            P = P*n            
        print("El total de la suma es :{}".format(P))
        print("El total del producto es :{}".format(sum))

    #15) Determinar si un número entero proporcionado por el usuario es primo. 
    #Un número primo es un entero que no tiene más divisores que él mismo y la unidad. 
    def NumerosPri(self):
        primo = "True"
        div = 2
        r = int(input("Ingrese su numero: "))
        while div < r and primo == "True":
            res = r % div
            if res == 0:
                pr = "False"
                div = div+1
        if pr == "True":
            print("Su numero {} es primo " .format(r))
        else:
            print("Su numero {} no es primo".format(r))
        
    #16) Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y 
    #calcular el resultado de la siguiente serie: 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema 
    #utilizando bucle Repeat controlado por contador y usando banderas.
    def Metod(self):
        from fractions import Fraction
        serie = 0
        I = 1
        r = int(input("Ingrese cualquier numero entero: "))
        b = "T"
        # while I>r:
        for x in range (r):
            if b == "T":
                serie = serie + Fraction(1,I)
                b ="F"               
            else:
                serie = serie - Fraction(1,I)
                b = "T"
            I += 1           
        print(serie) 

    #17) Calcular el factorial de N números enteros leídos de teclado.
    def Factorial(self):
        num= int(input('Ingrese su Rango: '))
        for i in range(1, num+1):
            m = int(input('Ingrese un Numero: '))
            Fact = 1
            for j in range(1,m+1):
                Fact= Fact * j
            print(f'El factorial es: {Fact}')

    #18) Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a 
    #continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos 
    #o iguales a cero. Imprimir dichos vectores.
    def Vectores(self,nulos,posit,negat,n):
        n=format(input('Ingrese la cantidad de datos: '))
        if n>0:
            nulos(0)
            posit(0)
            negat(0)
        for i in range(n):
            Datos= int(input('Ingrese un numero: '))
            if Datos > 0:
                posit += 1
            elif Datos < 0:
                negat += 1
            else:
                nulos += 1
            print('La cantidad de numeros positivos es: ',posit,
            '/nLa cantidad de numeros negativos es: ',negat,'/nLa cantidad de numeros nulos es: ',nulos)
        else:
            print('Los numeros ingresados no son correctos',n)

    #19) Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos.
    # a)El promedio de calificaciones de cada uno de los 6 exámenes.
    # b)El promedio de cada alumno.
    # c)El tipo (número) de examen que tuvo el mayor promedio de calificación. Escriba también dicho promedio.
    def Alumnos(self):
        import random as rd
        promd = []
        cal = [[rd.randint(0,10)for e in range(6)]for e in range(30)]
        for i in range(30):
            sum = 0
            for j in range(6):
                sum = sum + cal[i][j]
                pd = round(sum/6,2)
                promd.append(pd)
            print(f'promedio del alumno: {i+1} : {round(sum/6,2)}')
        promd.sort(reverse=True)
        print(f'La mayor nota es: {promd[0]}')

    


cal1=Ejercicios_Deber()
cal1.CalcularRadio()
cal1.DescuentoT()
cal1.Ventas()
cal1.CalificacionEx()
cal1.CalificacionEx2()
cal1.SueldoEmpl()
cal1.HorasExtras()
cal1.NumEnteros()
cal1.Variables()
cal1.ExamAs()
cal1.SumaCuadrados()
cal1.Number()
cal1.Bucle()
cal1.Enteros()
cal1.NumerosPri()
cal1.Metod()
cal1.Factorial()
cal1.Vectores()
cal1.Alumnos()