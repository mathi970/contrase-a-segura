import random
caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
longitud = int(input("¿cual quieres que sea la longitud de la contraseña?"))
contraseñaS = ""
for i in range(longitud):
    contraseñaS += random.choice(caracteres)

print(contraseñaS)
