import tkinter as tk
from pyswip import Prolog
prolog = Prolog()

prolog.consult("animales.pl")

preguntas = [
    {"pregunta": "¿Tiene plumas?", "propiedad": "tiene_plumas"},
    {"pregunta": "¿Puede volar?", "propiedad": "puede_volar"},
    {"pregunta": "¿Puede nadar?", "propiedad": "puede_nadar"},
    {"pregunta": "¿Es mamífero?", "propiedad": "es_mamifero"},
    {"pregunta": "¿Es carnívoro?", "propiedad": "es_carnivoro"},
    {"pregunta": "¿Vive en tierra?", "propiedad": "vive_en_tierra"},
    {"pregunta": "¿Vive en agua?", "propiedad": "vive_en_agua"}
]

respuestas = []
indice_pregunta = 0

# Función para cambiar entre frames (pantallas)
def mostrar_frame(frame):
    frame.tkraise()

# Función para iniciar el juego (limpia respuestas y muestra el primer frame)
def iniciar_juego():
    global respuestas, indice_pregunta
    respuestas = []
    indice_pregunta = 0
    actualizar_pregunta()
    resultado_label.pack_forget()
    volver_inicio_boton.pack_forget()
    si_boton.pack(side=tk.LEFT, padx=20)
    no_boton.pack(side=tk.RIGHT, padx=20)
    mostrar_frame(frame_juego)

# Función para hacer la consulta a Prolog
def hacer_consulta():
    consulta_prolog = ",".join(respuestas)
    consulta_completa = f"identificar_animal(Animal, Tipo), {consulta_prolog}"
    
    resultado = list(prolog.query(consulta_completa))
    if resultado:
        return resultado[0]["Tipo"]
    return None

# Función para manejar la respuesta del usuario y avanzar a la siguiente pregunta
def responder_si():
    global indice_pregunta
    propiedad = preguntas[indice_pregunta]["propiedad"]
    respuestas.append(f"{propiedad}(Animal)")
    
    tipo_animal = hacer_consulta()
    if tipo_animal:
        mostrar_resultado(tipo_animal)
        return
    
    indice_pregunta += 1
    actualizar_pregunta()

def responder_no():
    global indice_pregunta
    indice_pregunta += 1
    actualizar_pregunta()

def actualizar_pregunta():
    if indice_pregunta < len(preguntas):
        pregunta_label.config(text=preguntas[indice_pregunta]["pregunta"])
    else:
        mostrar_resultado(None)

# Mostrar el resultado final
def mostrar_resultado(tipo_animal):
    if tipo_animal:
        resultado_label.config(text=f"¡El animal es un {tipo_animal}!")
    else:
        resultado_label.config(text="No se pudo identificar el animal.")
    
    si_boton.pack_forget()
    no_boton.pack_forget()
    resultado_label.pack()
    volver_inicio_boton.pack(pady=20)

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Akinator de Animales")
ventana.geometry("400x300")
# ventana.configure(bg="lightblue")

# Crear los frames para las diferentes "pantallas"
frame_bienvenida = tk.Frame(ventana)
frame_juego = tk.Frame(ventana)
frame_bienvenida.grid(row=0, column=0, sticky="nsew")
frame_juego.grid(row=0, column=0, sticky="nsew")

# Contenido de la pantalla principal (bienvenida)
bienvenida_label = tk.Label(frame_bienvenida, text="¡Bienvenido al Akinator de Animales!", font=("Arial", 16))
bienvenida_label.pack(pady=40)

iniciar_boton = tk.Button(frame_bienvenida, text="Iniciar el Juego", command=iniciar_juego, width=20, font=("Arial", 14))
iniciar_boton.pack(pady=10)

cerrar_boton = tk.Button(frame_bienvenida, text="Cerrar la Aplicación", command=ventana.quit, width=20, font=("Arial", 14))
cerrar_boton.pack(pady=10)

# Contenido de la pantalla del juego
pregunta_label = tk.Label(frame_juego, text=preguntas[indice_pregunta]["pregunta"], font=("Arial", 16))
pregunta_label.pack(pady=20)

si_boton = tk.Button(frame_juego, text="Sí", command=responder_si, width=10, font=("Arial", 14))
si_boton.pack(side=tk.LEFT, padx=20)

no_boton = tk.Button(frame_juego, text="No", command=responder_no, width=10, font=("Arial", 14))
no_boton.pack(side=tk.RIGHT, padx=20)

resultado_label = tk.Label(frame_juego, text="", font=("Arial", 18), fg="green")

volver_inicio_boton = tk.Button(frame_juego, text="Volver al Inicio", command=lambda: mostrar_frame(frame_bienvenida), width=20, font=("Arial", 14))

# Mostrar el frame de bienvenida al inicio
mostrar_frame(frame_bienvenida)

# Iniciar la interfaz gráfica
ventana.mainloop()