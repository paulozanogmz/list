#!/usr/bin/env python3

ingredientes = ['Pan', 'Jamon', 'Tocino', 'Queso', 'Verdura', 'Aderezos']
#print("Los ingredientes del Sandwich son: ")
#print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[4], ingredientes[5], sep='\n')

def sandwich(ingredientes):
	print("Los ingredientes del Sandwich son: ", end='\n')
	print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], ingredientes[4], ingredientes[5], sep='\n', end='\n')
	i = input("Elige ingredientes (Max 6): ").split()
	print(i, end='\n')
	for i in ingredientes:
		sin = input("Sin: ").split()
		return
	
	
	
print(sandwich(ingredientes))