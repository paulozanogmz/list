#!/usr/bin/env python3
#Ingredientes de Hamburguesa

ingredientes = ['Pan', 'Carne', 'Lechuga', 'Ketchup', 'Mostaza']
print("Los ingredientes de la Hamburguesa son: ")
print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[4], sep='\n')

def hamburguesa(ingredientes):
    i = input("Sin cuantos ingredientes quieres (Max 3): ")
    for i in ingredientes:
        sin = input("Sin: ").split()
#        print(sin, sep='\n')
        return
    return


print(hamburguesa(ingredientes))