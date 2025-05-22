# Los Mad Libs son historias con espacios en blanco que el lector puede rellenar con sus propias palabras. El resultado suele ser una historia divertida (o extraña).
#
# Mad Libs requiere:
#
# Palabras del lector (para los espacios en blanco)
# Una historia para conectar las palabras
# Para este proyecto, le proporcionaremos la historia (siéntase libre de modificarla), pero dependerá de usted crear un programa que haga lo siguiente:
#
# Solicitar al usuario que ingrese información
# Imprima la historia completa de Mad Libs con la entrada del usuario en los lugares correctos


historia = "Esta mañana me desperté y me sentí % porque % finalmente iba a % sobre el gran % %. Al otro lado del % había muchos % protestando para mantener a % en las tiendas. La multitud comenzó a % al ritmo del %, lo que hizo que todos los % se pusieran muy %. % intentó % en las alcantarillas y encontró % ratas. Necesitando ayuda, % llamó rápidamente a %. % apareció y salvó a % volando hacia % y arrojando a % en un charco de %. % luego se durmió y despertó en el año %, en un mundo donde % gobernaba el mundo."

# Solicitar al usuario que ingrese información
while True:
    print(historia)
    for i in historia:
        if i == "%":
            palabra = input("Ingrese una palabra: ")
            historia = historia.replace(i, palabra, 1)
    break
print(historia)
