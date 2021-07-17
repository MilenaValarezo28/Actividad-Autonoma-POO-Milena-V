class Cargo:
    secuencia=0
    def _init_(self, des="Sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des

if __name__ == "__main__":
    cargo1= Cargo()
    print(cargo1.codigo,cargo1.descripcion)
    cargo2= Cargo()
    cargo2.descripcion= "Director"
    print(cargo2.codigo,cargo2.descripcion)
    cargo3= Cargo("Analista")
    print(cargo3.codigo,cargo3.descripcion)    
    # print(Cargo.secuencia)
    # print(Cargo1.secuencia)
    # print(Cargo2.secuencia)
    # print(Cargo3.secuencia)