class Operaciones:
    def __init__(self,num1,num2):
        self.numero1= num1
        self.numero2= num2

    def Suma(self):
        Suma= self.numero1 + self.numero2
        return Suma

    def Resta(self):
        if self.numero1 >= self.numero2:
            return self.numero1 - self.numero2
        else:
            return 0

    def Multiplicacion(self):
        return self.numero1 * self.numero2

    def Division(self):
        if self.numero2 != 0: return self.numero1 / self.numero2
        return 0

    def DivisionEntera(self):
        if self.numero2 != 0: return self.numero1 // self.numero2
        return 0

    def Residuo(self):
        return self.numero1 % self.numero2

    def Exponente(self):
        return self.numero1 ** self.numero2

    def Mostrar(self):
        print("Operando:={}","Operando2:={}".format(self.numero1,self.numero2))

print("Menu Operaciones Matematicas")
print("1) Suma/n2) Resta/n3) Multiplicacion/n4) Division/n5) DivisionEntera/n6) Residuo/n7) Exponente/n8) Salir")
opc= "0"
while opc!="8":
    opc= input("Elija una opcion[1...8]: ")
    num1= int(input("Ingrese Numero1: "))
    num2= int(input("Ingrese Numero2: "))
    opc= Operaciones(num1,num2)
    if opc == "1":
        print(opc.Suma())

    elif opc == "2":
        print(opc.Resta())

print("Gracias por su visita!!!")
