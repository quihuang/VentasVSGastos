import os
import utilidades as util
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

messageExit = "\nSaliendo del programa..."
messageDataInvalid = "\nEl valor ingresado no es valido."
messageOptionInvalid = "\nLa opción ingresada no es valida."
messageRange = "\nDebe diligenciar las ventas y gastos de todas las sedes para poder visualizar la tabla"
messageRangeGrapih = "\nDebe diligenciar las ventas y gastos de todas las sedes para poder visualizar el grafico"

option = ""

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# salesOne = [random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000)]
# salesTwo = [random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000)]
# salesThree = [random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000)]
# expensesOne = [random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000)]
# expensesTwo = [random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000)]
# expensesThree = [random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000),random.randint(0, 500000)]

salesOne = []
salesTwo = []
salesThree = []
expensesOne = []
expensesTwo = []
expensesThree = []

while option !="6":

    print("\n===========================================================")
    print("   Bienvenido al software de gestion de ventas y gastos     ")
    print("===========================================================")
    print("1. Capturar Ventas.")
    print("2. Capturar Gastos.")
    print("3. Visualizar Tabla de ventas y gastos.")
    print("4. Visualizar grafico de barras de ventas y gastos.")
    print("5. Visualizar grafico de lineas y gastos.")
    print("6. Salir.")
    print("===========================================================")

    option = input("\nPorfavor ingrese una opción : ")

    if option == "1":
        salesSite = ""
        os.system("clear")
        while salesSite != "4":
            print("\n=========================================")
            print("   Captura de ventas mes a mes por sede   ")
            print("==========================================")
            print("1. ventas sede 1.")
            print("2. ventas sede 2.")
            print("3. ventas sede 3.")
            print("4. salir.")
            print("==========================================")

            salesSite = input("\nPorfavor seleccione la sede : ")

            if salesSite == "1":
                os.system("clear")
                
                for month in months: 
                    validateNumeric = False  

                    while validateNumeric == False:
                        sale = input(f"\nIngrese la venta del mes {month} : ")
                        validateNumeric, message = util.validateIsNumeric(sale)

                        if message !="":
                            os.system("clear")
                            print(message)
                        else:
                            os.system("clear")

                    salesOne.append(sale)

            elif salesSite == "2":
                os.system("clear")
                
                for month in months: 
                    validateNumeric = False  

                    while validateNumeric == False:
                        sale = input(f"\nIngrese la venta del mes {month} : ")
                        validateNumeric, message = util.validateIsNumeric(sale)
                        
                        if message !="":
                            os.system("clear")
                            print(message)
                        else:
                            os.system("clear")

                    salesTwo.append(sale)

            elif salesSite == "3":
                os.system("clear")
                
                for month in months: 
                    validateNumeric = False  

                    while validateNumeric == False:
                        sale = input(f"\nIngrese la venta del mes {month} : ")
                        validateNumeric, message = util.validateIsNumeric(sale)
                        
                        if message !="":
                            os.system("clear")
                            print(message)
                        else:
                            os.system("clear")

                    salesThree.append(sale)

            elif salesSite == "4": 
                os.system("clear")
            else:
                os.system("clear")
                print(messageOptionInvalid)
            
    elif option == "2":  
        expensesSite = ""
        os.system("clear")
        while expensesSite != "4":
            print("\n=========================================")
            print("   Captura de gastos mes a mes por sede   ")
            print("==========================================")
            print("1. gastos sede 1.")
            print("2. gastos sede 2.")
            print("3. gastos sede 3.")
            print("4. salir.")
            print("==========================================")

            expensesSite = input("\nPorfavor seleccione la sede : ")

            if expensesSite == "1":
                os.system("clear")
                
                for month in months: 
                    validateNumeric = False  

                    while validateNumeric == False:
                        expenses = input(f"\nIngrese el gasto del mes {month} : ")
                        validateNumeric, message = util.validateIsNumeric(expenses)
                        
                        if message !="":
                            os.system("clear")
                            print(message)
                        else:
                            os.system("clear")

                    expensesOne.append(expenses)

            elif expensesSite == "2":
                os.system("clear")
                
                for month in months: 
                    validateNumeric = False  

                    while validateNumeric == False:
                        expenses = input(f"\nIngrese el gasto del mes {month} : ")
                        validateNumeric, message = util.validateIsNumeric(expenses)
                        
                        if message !="":
                            os.system("clear")
                            print(message)
                        else:
                            os.system("clear")

                    expensesTwo.append(expenses)

            elif expensesSite == "3":
                os.system("clear")
                
                for month in months: 
                    validateNumeric = False  

                    while validateNumeric == False:
                        expenses = input(f"\nIngrese el gasto del mes {month} : ")
                        validateNumeric, message = util.validateIsNumeric(expenses)
                        
                        if message !="":
                            os.system("clear")
                            print(message)
                        else:
                            os.system("clear")

                    expensesThree.append(expenses)

            elif expensesSite == "4": 
                os.system("clear")
            else:
                os.system("clear")
                print(messageOptionInvalid)

    elif option == "3":  

        os.system("clear")
        try:
            df = util.createDataFrame (months, salesOne, salesTwo, salesThree, expensesOne, expensesTwo, expensesThree)
            print(f"\n\t\t\t\t\tTABLA DE GATOS Y VENTAS\n\n{df}")
        except:
            os.system("clear")
            print(messageRange)

    elif option == "4": 
        os.system("clear")
        try:
            df = util.createDataFrame (months, salesOne, salesTwo, salesThree, expensesOne, expensesTwo, expensesThree) 
            ejeX = months[0:6]

            lista_indices = np.arange(len(ejeX))
            ancho_columna = 0.35

            sale1 = df["Ventas sede1"].iloc[0:6].values.tolist()
            expenses1 = df["Gastos sede1"].iloc[0:6].values.tolist()

            plt.bar(lista_indices, sale1, width=ancho_columna, label="Ventas", color="orange")
            plt.bar(lista_indices + ancho_columna, expenses1, width=ancho_columna, label="Gastos", color="blue")
            plt.legend(loc='best')

            plt.xticks(lista_indices, ejeX)
            plt.xlabel("Meses")
            plt.ylabel("Valor")
            plt.title("VENTAS Y GASTOS SEDE 1 PRIMER SEMESTRE")

            plt.show()
        except:
            os.system("clear")
            print(messageRangeGrapih)

    elif option == "5":  
        os.system("clear")
        try:
            df = util.createDataFrame (months, salesOne, salesTwo, salesThree, expensesOne, expensesTwo, expensesThree) 
            ejeX = months

            sale1 = df["Ventas sede1"]
            sale2 = df["Ventas sede2"]
            sale3 = df["Ventas sede3"]

            plt.plot(ejeX, sale1, "b-", label="sede 1")
            plt.plot(ejeX, sale2, "r-", label="sede 2")
            plt.plot(ejeX, sale3, "g-", label="sede 3")
            plt.legend()

            plt.xlabel("Meses")
            plt.ylabel("Valor venta")
            plt.title("VENTAS DE LAS SEDES")
            plt.show()
        except:
            os.system("clear")
            print(messageRangeGrapih)

    elif option == "6": 
        os.system("clear")
        print(messageExit)
    else:
        os.system("clear")
        print(messageOptionInvalid)
