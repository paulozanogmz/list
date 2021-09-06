#!/usr/bin/env python3

ingredientes = ['Pan', 'Salchica', 'Verdura', 'Aderezos']
#print("Los ingredientes del Hotdog son: ")
#print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], sep='\n')

def hotdog(ingredientes):
	print("Los ingredientes del Hotdog son: ")
	print(ingredientes[0], ingredientes[1], ingredientes[2], ingredientes[3], sep='\n')
	i = input("Elige ingredientes (Max 4): ")
	for i in ingredientes:
		sin = input("Sin: ").split()
		return
	
	
	
print(hotdog(ingredientes))