import statistics
import math
import csv

clientes_banco = [
    {"nombre": "Alma Leon",
    "saldo": 200000},
    
    {"nombre": "Bernardo Serrano",
    "saldo": 1500000},
    
    {"nombre": "Claudio Tolosa",
    "saldo": 10000},
    
    {"nombre": "Diego Sanchez",
    "saldo": 500000},
    
    {"nombre": "Esperanza Solar",
    "saldo": 3000000},
    
    {"nombre": "Francisca Osorio",
    "saldo": 200000},
    
    {"nombre": "Gabriel Reyes",
    "saldo": 40000000},
    
    {"nombre": "Hector Silva",
    "saldo": 100},
    
    {"nombre": "Ines Poblete",
    "saldo": 60000},
    
    {"nombre": "Javier Lopez",
    "saldo": 600000}
]

def main():
    
    def mostrar_menu():
        print("Gestor Financieros Clientes.")
        print("1. Clasificacion de saldos.")
        print("2. Saldo mas alto.")
        print("3. Saldo mas bajo.")
        print("4. Saldo promedio.")
        print("5. Media Geometrica.")
        print("6. Reporte de saldos.")
        print("7. Salir del menu.") 
        print("")
        opcion = int(input("Ingrese una opcion:"))
        return opcion

    def clasificacion_datos():
        print("Clasificacion saldos")
        for nombre in clientes_banco:
            saldo = nombre['saldo']
            nombre = nombre['nombre']
            if saldo > 0 and saldo <= 300000:
                print(f"{nombre} cliente con saldo {saldo}")
                print("Clasificacion: Saldo bajo")
                print("")
                
            elif saldo > 300000 and saldo <= 2000000:
                print(f"{nombre} cliente con saldo {saldo}")
                print("Clasificacion: Saldo medio")
                print("")
            else:
                print(f"{nombre} cliente con saldo {saldo}")
                print("Clasificacion: Saldo alto")
                print("")
                
    
    def saldo_mayor():
        
        saldo_maximo = max(cliente['saldo'] for cliente in clientes_banco)
        print(f"El saldo mayor es: {saldo_maximo}")
        print("")
        
    def saldo_menor():
        saldo_minimo = min(cliente['saldo'] for cliente in clientes_banco)
        print(f"El saldo mínimo entre todos los clientes es: {saldo_minimo}")
        print("")
        
    def saldo_promedio():
        promedio = [cliente['saldo'] for cliente in clientes_banco]
        saldo_promedio = statistics.mean(promedio)
        print(f"El saldo promedio es: {saldo_promedio}")
        print("")
    
    def media_geometrica():
        saldos = [cliente['saldo'] for cliente in clientes_banco]
        log_sum = sum(math.log(saldo) for saldo in saldos)
        saldo_media_geometrica = math.exp(log_sum / len(saldos))
        print(f"La media geométrica es: {saldo_media_geometrica}")
        print("")
    
    def reporte_saldos():
            deduccion = float(10)
            deduccion /= 100
            with open('reporte_saldos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nombre", "Saldo Neto", "Saldo con Deduccion"])
                for cliente in clientes_banco:
                    saldo_neto = cliente['saldo']
                    saldo_deducido = round(saldo_neto * (1 - deduccion))
                    writer.writerow([cliente['nombre'], saldo_neto, saldo_deducido])
                print("Reporte de saldos guardado en 'reporte_saldos.csv'")
                print("")
            
    def salir_menu():
        print("Ha salido del programa con exito")
    
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            clasificacion_datos()
        if opcion == 2:
            saldo_mayor()
        if opcion == 3:
            saldo_menor()
        if opcion == 4:
            saldo_promedio()
        if opcion == 5:
            media_geometrica()
        if opcion == 6:
            reporte_saldos()
        if opcion == 7:
            salir_menu()
            break
main()
