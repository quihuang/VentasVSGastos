import pandas as pd

messageNotNumeric = "\nError : El valor ingresado debe ser un numero entero."

def createDataFrame (months: list, salesOne: list, salesTwo: list, salesThree: list, expensesOne: list, expensesTwo: list, expensesThree: list) -> pd.DataFrame:

    """
    Función encargada armar la estructura del DataFrame.

    Parameters
    ------------------
    months : list
        Lista de meses.
    salesOne : list
        Lista de las ventas sede 1.
    salesTwo : list
        Lista de las ventas sede 2.
    salesThree : list
        Lista de las ventas sede 3.
    expensesOne : list
        Lista de los gastos sede 1.
    expensesTwo : list
        Lista de los gastos sede 2.
    expensesThree : list
        Lista de los gastos sede 3.

    Returns
    ------------------
    dataFrame : DataFrame
        Retorna una tabla con las ventas y gastos de las diferentes sedes por cada uno de los meses del año.
    """

    datos = {
        "Mes" : months,
        "Ventas sede1" : salesOne,
        "Ventas sede2" : salesTwo,
        "Ventas sede3" : salesThree,
        "Gastos sede1" : expensesOne,
        "Gastos sede2" : expensesTwo,
        "Gastos sede3" : expensesThree    
    }

    dataFrame = pd.DataFrame(datos)

    return dataFrame


def validateIsNumeric(number: str) -> tuple:

    """
    Función encargada de validar que el numero sea entero positivo.

    Parameters
    ------------------
    number : str
        cadena de texto a evaluar.

    Returns
    ------------------
    tuple : tuple
        Retorna en caso de ser verdadero (True,"") de lo contrario (False,messageNotNumeric).
    """

    if not number.isnumeric():
        return(False,messageNotNumeric)
    else:
        return(True, "")


