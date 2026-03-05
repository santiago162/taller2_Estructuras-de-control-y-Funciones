# Crear un simulador de descuentos que solicite al usuario su categoría (A, B, C) y el monto de compra. Aplicar los siguientes descuentos según categoría: A=20%, B=15%, C=10%. Para cualquier otra categoría no aplicar descuento. Mostrar el monto final a pagar y la cantidad ahorrada.

categoria = input("Ingresa tu categoría (A, B, C): ").upper()
monto = float(input("Ingresa el monto de la compra: "))

descuento = 0

if categoria == "A":
    descuento = 0.20

elif categoria == "B":
    descuento = 0.15

elif categoria == "C":
    descuento = 0.10

else:
    descuento = 0

ahorro = monto * descuento
total = monto - ahorro

print("Descuento aplicado:", descuento * 100, "%")
print(f"Ahorraste: ${ahorro:.2f}")
print(f"Total a pagar: ${total:.2f}")