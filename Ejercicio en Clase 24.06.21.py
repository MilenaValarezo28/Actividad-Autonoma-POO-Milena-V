class Tarea:
    def __init__(self):
        pass
    def pagoJornadaExtra(self):
        horas_trabajadas, horas_extras, horas_extras_triples = 0,0,0
        valor_hora, pago_hpora_extra, pago_horas_triple = 0,0,0
        horas_trabajadas=int(input("Ingrese horas trabajadas"))
        valor_hora= float(input("Ingrese valor hora"))
        if(horas_trabajadas > 40):
            horas_extras= horas_trabajadas -40
            if (horas_extras>8):
                horas_extras_triple= horas_extras-8
                pago_horas_extras= valor_hora * 2 * 8 + valor_hora * 3 * horas_extras_triple
            else: 
                pago_horas_extras= valor_hora * 2 + horas_extras
            pago_total = valor_hora * 40 + pago_horas_extras
        else:
            pago_total = valor_hora * horas_trabajadas
        print("""Horas trabajadas:{} Horas Extras: {} Horas triples: {} Valor Hora:{} Pago Valor Extra:{} Pago total:{}""".format(horas_trabajadas, horas_extras,horas_extras_triple,valor_hora,pago_horas_extras,pago_total))
        def mayor(self):
            n1,n2,n3= 0,0,0
            n1 = int(input("ingrese Numero 1: "))
            n2 = int(input("ingrese Numero 2: "))
            n3 = int(input("ingrese Numero 3: "))
            if (n1>n2>n3):
                print(n1)
            elif (n2>n1>n3):
                print(n2)
            else:
                print(n3)

tarea1= Tarea()

pago1= Tarea()
pago1.pagoJornadaExtra()