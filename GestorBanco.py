import statistics
import math
import csv
import os

clientes_banco = [
    {"nombre": "Alma",
    "saldo": 200000},
    
    {"nombre": "Bernardo",
    "saldo": 1500000},
    
    {"nombre": "Claudio",
    "saldo": 10000},
    
    {"nombre": "Diego",
    "saldo": 500000},
    
    {"nombre": "Esperanza",
    "saldo": 3000000},
    
    {"nombre": "Francisca",
    "saldo": 200000},
    
    {"nombre": "Gabriel",
    "saldo": 40000000},
    
    {"nombre": "Hector",
    "saldo": 100},
    
    {"nombre": "Ines",
    "saldo": 60000},
    
    {"nombre": "Javier",
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
        opcion = int(input("Ingrese una opcion:"))
        return opcion

    def clasificacion_datos():
        print("Clasificacion saldos")
        for nombre in clientes_banco:
            saldo = nombre['saldo']
            nombre = nombre['nombre']
            if saldo > 0 and saldo <= 300000:
                print("Clasificacion: Saldo bajo")
                print(f"{nombre} cliente con saldo {saldo}")
            elif saldo > 300000 and saldo <= 2000000:
                print("Clasificacion: Saldo medio")
            else:
                print("Clasificacion: Saldo alto")
                
    
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            clasificacion_datos()
        if opcion == 2:
            saldo_alto()
        if opcion == 3:
            saldo_bajo()
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

