#!/usr/bin/env python3

#Ingredientes de Sandwich

ingredientes = ['Pan', 'Jamon', 'Tocino', 'Queso', 'Verdura', 'Aderezos']
print("Los ingredientes del Sandwich son: ")
print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[4], ingredientes[5], sep='\n')

def sandwich(ingredientes):
    i = input("Sin cuantos ingredientes quieres (Max 4): ")
    for i in ingredientes:
        sin = input("Sin: ").split()
#        print(sin, sep='\n')
        return
    return


print(sandwich(ingredientes))