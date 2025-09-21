# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primera llamada: solo monto total (usa 10% por defecto)
monto1 = 200
descuento1 = calcular_descuento(monto1)
total1 = monto1 - descuento1

# Segunda llamada: monto total y porcentaje específico
monto2 = 350
descuento2 = calcular_descuento(monto2, 15)  # 15% de descuento
total2 = monto2 - descuento2



print("Primera compra:")
print(f"  Monto total: ${monto1}")
print(f"  Descuento aplicado: ${descuento1:.2f}")
print(f"  Total a pagar: ${total1:.2f}\n")

print("Segunda compra:")
print(f"  Monto total: ${monto2}")
print(f"  Descuento aplicado: ${descuento2:.2f}")
print(f"  Total a pagar: ${total2:.2f}")