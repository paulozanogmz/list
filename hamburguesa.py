#!/usr/bin/env python3
#Ingredientes de Hamburguesa

ingredientes = ['Pan', 'Carne', 'Lechuga', 'Ketchup', 'Mostaza']
#print("Los ingredientes de la Hamburguesa son: ")
#print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[4], sep='\n')

def hamburguesa(ingredientes):
    print("Los ingredientes de la Hamburguesa son: ")
    print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[4], sep='\n')
    i = input("Elige ingredientes (Max 5): ")
    for i in ingredientes:
        sin = input("Sin: ").split()
        return



print(hamburguesa(ingredientes))