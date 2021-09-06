#!/usr/bin/env python3

#Ingredientes de Hotdog

ingredientes = ['Pan', 'Salchica', 'Verdura', 'Aderezos']
print("Los ingredientes del Hotdog son: ")
print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], sep='\n')

def hotdog(ingredientes):
    i = input("Sin cuantos ingredientes quieres (Max 2): ")
    for i in ingredientes:
        sin = input("Sin: ").split()
#        print(sin, sep='\n')
        return
    return


print(hotdog(ingredientes))