#!/usr/bin/env python3

#Menu


plate1 = "Hamburguesa"
plate2 = "Hotdog"
plate3 = "Sandwich"

print("¡Bienvenido! Este es nuestro menu: \n ")
print(plate1, plate2, plate3, sep='\n')

try:
    pick = input("Elige platillo: ")
    if pick == "Hamburguesa":
	    from test_hamburguesa.py import hamburguesa
	    print(hamburguesa)
    elif pick == "Sandwich":
	    from test_sandwich.py import sandwich
	    print(sandwich)
    elif pick == "Hotdog":
	    from test_hotdog.py import hotdog
	    print(hotdog)
    else:
	    print("No hay eso")
except EOFError as e:
	print(end="")