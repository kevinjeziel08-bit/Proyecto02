nombre = str(input("Nombre: "))
edad = int(input("Edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros (ej. 1.70): "))

imc = peso / (estatura ** 2)

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print()
print(f"Hola, {nombre} ({edad} años)")
print(f"Peso: {peso} kg | Estatura: {estatura:.2f} m")
print(f"Tu IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")