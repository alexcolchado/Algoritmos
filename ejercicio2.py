#Hacer q sistema genere un # aleatorio
#entre 1 y 10. Luego hacer q el usuario adivine el numero.
#La app debe terminar cuando el usuario adivine.

import random

s = random.randint(1, 10)

while True:
    n = int(input("Adivina codigo de sistema(1 al 10):"))


    if n==s:
        print("Adivinaste!")
        break
    else:
        print("mala suerte")

