entrada = int(input("¿Tienes entrada para el concierto? (1: Sí, 0: No) "))
edad = int(input("¿Qué edad tienes? "))
ropa = int(input("¿Llevas ropa blanca? Esto es una fiesta ibicenca (1: Sí, 0: No): "))

if entrada == 1 and edad >= 18 and ropa == 1:
    print("Adelante, puedes pasar al concierto")
else:
    print("No puedes pasar. Debes tener entrada, ser mayor de edad y vestir de blanco.")