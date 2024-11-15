import tkinter as tk
from pyswip import Prolog
prolog = Prolog()

prolog.consult("animales.pl")

def identificar_animal():
    animal = entrada.get()
    resultado = list(prolog.query(f"identificar_animal({animal}, Tipo)"))
    if resultado:
        tipo = resultado[0]['Tipo']
        resultado_label.config(text=f"El animal es un {tipo}.")
    else:
        resultado_label.config(text="No se pudo identificar el animal.")

# Crear la ventana de la interfaz
ventana = tk.Tk()
ventana.title("Identificación de Animales")

# Crear los widgets
entrada_label = tk.Label(ventana, text="Introduce el nombre del animal:")
entrada_label.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Identificar", command=identificar_animal)
boton.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()

# if __name__ == "__main__":
#     print("Sistema de Identificación de Animales\n")
#     while True:
#         animal = input("Introduce el nombre del animal (en minúsculas): ")
#         identificar_animal(animal)
#         continuar = input("¿Deseas consultar otro animal? (s/n): ")
#         if continuar.lower() != 's':
#             break