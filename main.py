from pyswip import Prolog
prolog = Prolog()

prolog.consult("animales.pl")

def identificar_animal(animal):
    resultado = list(prolog.query(f"identificar_animal({animal}, Tipo)"))
    if resultado:
        tipo = resultado[0]['Tipo']
        print(f"El animal es un {tipo}.")
    else:
        print("No se pudo identificar el animal.")

if __name__ == "__main__":
    print("Sistema de Identificación de Animales\n")
    while True:
        animal = input("Introduce el nombre del animal (en minúsculas): ")
        identificar_animal(animal)
        continuar = input("¿Deseas consultar otro animal? (s/n): ")
        if continuar.lower() != 's':
            break