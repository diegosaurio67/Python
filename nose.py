
matri = 120000
seg = 25000
edad = 0



edad = int(input("Ingrese su edad ugu: "))

plan = str(input("Ingrse plan de gym (Basico, Pro, Elite): "))


descuento_matri = 0

#Reglas de descuento de matricula

if edad >= 25:
  if plan in ["Elite", "Pro"]:
    descuento_matri = (matri * 0.20)
  elif plan == "Basico":
    descuento_matri = (matri * 0.10)

  elif 26 <= edad <= 50:
    if plan in ["Elite", "Pro"]:
      descuento_matri = (matri * 0.15)
    elif plan == "Basico":
      
      descuento_matri = (matri * 0.05)

valor_matri = matri - descuento_matri

#Reglas seguro de salud


if plan == "Elite":
  descuento_seg = 0.50
  if edad >= 40:
   descuento_seg += 0.10

#Algo esta mal en valor de seguro

valor_seg = seg * (1 - descuento_seg)

print("Valor de su matricula: $", valor_matri )

print("Valor de su seguro: $", valor_seg )

