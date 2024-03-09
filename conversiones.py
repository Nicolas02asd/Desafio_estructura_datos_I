import sys

'''Digitar tasas de conversion: tasa  sol, tasa peso argentino, tasa dolar 
y finalmente el monto en pesos chilenos a convertir'''

tasa_sol = float(sys.argv[1])
tasa_peso_argentino = float(sys.argv[2])
tasa_dolar = float(sys.argv[3])
monto_en_pesos = float(sys.argv[4])

monto_en_soles = monto_en_pesos * tasa_sol
monto_en_pesos_argentinos = monto_en_pesos * tasa_peso_argentino
monto_en_dolares = monto_en_pesos * tasa_dolar

print(f"Los {monto_en_pesos:.0f} pesos equivalen a:")
print(monto_en_soles, "Soles")
print(monto_en_pesos_argentinos, "Pesos Argentinos")
print(monto_en_dolares, "Dólares")
