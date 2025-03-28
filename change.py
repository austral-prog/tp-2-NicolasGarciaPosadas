def change():
    expense = 23.75
    money = 100
    vuelto = money-expense
    pesos = int(vuelto)
    centavos = int((vuelto-pesos)*100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(f"{money}\n")
    print(f"Vuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)





change()