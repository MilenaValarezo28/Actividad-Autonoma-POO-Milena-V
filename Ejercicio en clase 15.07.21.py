class Logica:
    def __init__(self, lista= None):
        self._lista= lista
        
    @property
    def lista(self):
        return self._lista
    @lista.setter
    def lista(self,value):
        self._lista= value

    def parImpar(self, numero):
        rec= numero%2
        if rec == 0:
            print("{} es par".format(numero))
        else:
            print("{} es Impar".format(numero))

    def perfecto(self, num):
        acu= 0
        for contador in range(1, num):
            rec= num % contador
            if rec == 0:
                acu= acu + contador
        if acu == num:
            print("{} Es perfecto".format(num))
        else:
            print("{} No es perfecto".format(num))

class Ejercicio(Logica):
    def __init__(self,lista,numeros):
        super().__init__(lista)
        self.dato= numeros

    def Sumar(Self,n1,n2):
        return n1, n2

    def parImpar(self, numero):
        super().parImpar(numero)
        return numero%2

ejer = Ejercicio([1,3,5],20)
ejer.perfecto(6)

        