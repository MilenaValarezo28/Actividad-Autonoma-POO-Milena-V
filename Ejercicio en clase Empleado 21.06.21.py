from cargos import Cargo

class Empleado:
    secuencia=0
    def _init_(self,nom,ced,sue,cargo):
        self.codigo=self.generarCodigo()
        self.nombre= nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargo
    
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo))
    
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia

cargo1= Cargo("Docente")
empl1= Empleado("Nicole", "5204", 500, cargo1)
empl1.mostrar()
cargo2= Cargo("Analista")
emp2= Empleado("Ana","0914",500,cargo2)
emp2.mostrar()