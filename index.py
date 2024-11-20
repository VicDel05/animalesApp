
import tkinter as tk
from tkinter import ttk
from pyswip import Prolog

# Inicializar Prolog
prolog = Prolog()

prolog.consult("animales.pl")

respuestas = []
indice_pregunta = 0
preguntas = [
    {"pregunta": "¿Tiene plumas?", "propiedad": "tiene_plumas"},
    {"pregunta": "¿Puede volar?", "propiedad": "puede_volar"},
    {"pregunta": "¿Puede nadar?", "propiedad": "puede_nadar"},
    {"pregunta": "¿Es mamífero?", "propiedad": "es_mamifero"},
    {"pregunta": "¿Es carnívoro?", "propiedad": "es_carnivoro"},
    {"pregunta": "¿Vive en tierra?", "propiedad": "vive_en_tierra"},
    {"pregunta": "¿Vive en agua?", "propiedad": "vive_en_agua"}
]


# Función para cambiar entre frames
def mostrar_frame(frame):
    frame.tkraise()

# Iniciar el juego
def iniciar_juego():
    global respuestas, indice_pregunta, preguntas  # Asegurarte de que preguntas sea accesible
    respuestas.clear()
    indice_pregunta = 0
    actualizar_pregunta()
    resultado_label.pack_forget()
    volver_inicio_boton.pack_forget()
    si_boton.pack(side=tk.LEFT, padx=20)
    no_boton.pack(side=tk.RIGHT, padx=20)
    historial_text.config(state='normal')
    historial_text.delete(1.0, tk.END)
    historial_text.config(state='disabled')
    mostrar_frame(frame_juego)

# Hacer consulta a Prolog
def hacer_consulta():
    # Requiere al menos 2 respuestas antes de intentar identificar el animal
    if len(respuestas) < 2:
        return None

    consulta_prolog = ",".join(respuestas)
    consulta_completa = f"identificar_animal(Animal, Tipo), {consulta_prolog}"
    
    resultado = list(prolog.query(consulta_completa))
    if resultado:
        return resultado[0]["Tipo"]
    return None

# Manejar respuesta Sí
def responder_si():
    global indice_pregunta
    propiedad = preguntas[indice_pregunta]["propiedad"]
    respuestas.append(f"{propiedad}(Animal)")
    
    # Intenta identificar el animal
    tipo_animal = hacer_consulta()
    if tipo_animal:
        mostrar_resultado(tipo_animal)
        return

    # Si no se identificó, pasa a la siguiente pregunta
    indice_pregunta += 1
    actualizar_pregunta()

# Manejar la respuesta "No"
def responder_no():
    global indice_pregunta
    indice_pregunta += 1
    actualizar_pregunta()

# Actualizar pregunta en pantalla
def actualizar_pregunta():
    global preguntas, indice_pregunta  # Asegurarte de que preguntas sea accesible
    if indice_pregunta < len(preguntas):
        pregunta_label.config(text=preguntas[indice_pregunta]["pregunta"])
    else:
        mostrar_resultado(None)

# Actualizar historial
def actualizar_historial(pregunta, respuesta):
    historial_text.config(state='normal')
    historial_text.insert(tk.END, f"{pregunta}: {respuesta}\n")
    historial_text.config(state='disabled')

# Mostrar resultado final
def mostrar_resultado(tipo_animal):
    if tipo_animal:
        resultado_label.config(text=f"¡El animal es un {tipo_animal}!", fg="blue")
        img_path = f"imagenes/{tipo_animal}.png"
        try:
            animal_img = tk.PhotoImage(file=img_path)
            resultado_imagen.config(image=animal_img)
            resultado_imagen.image = animal_img
            resultado_imagen.pack(pady=10)
        except Exception:
            resultado_imagen.pack_forget()
    else:
        resultado_label.config(text="No se pudo identificar el animal.", fg="red")
    
    si_boton.pack_forget()
    no_boton.pack_forget()
    resultado_label.pack()
    volver_inicio_boton.pack(pady=20)

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Akinator de Animales")
ventana.geometry("500x400")

# Crear frames
frame_bienvenida = tk.Frame(ventana)
frame_juego = tk.Frame(ventana)
frame_bienvenida.grid(row=0, column=0, sticky="nsew")
frame_juego.grid(row=0, column=0, sticky="nsew")

# Pantalla de bienvenida
bienvenida_label = tk.Label(frame_bienvenida, text="¡Bienvenido al Akinator de Animales!", font=("Arial", 16))
bienvenida_label.pack(pady=40)

iniciar_boton = ttk.Button(frame_bienvenida, text="Iniciar el Juego", command=iniciar_juego)
iniciar_boton.pack(pady=10)

cerrar_boton = ttk.Button(frame_bienvenida, text="Cerrar la Aplicación", command=ventana.quit)
cerrar_boton.pack(pady=10)

# Pantalla del juego
pregunta_label = tk.Label(frame_juego, text="", font=("Arial", 16))
pregunta_label.pack(pady=20)

si_boton = ttk.Button(frame_juego, text="Sí", command=responder_si)
no_boton = ttk.Button(frame_juego, text="No", command=responder_no)

resultado_label = tk.Label(frame_juego, text="", font=("Arial", 18), fg="green")
resultado_imagen = tk.Label(frame_juego)

volver_inicio_boton = ttk.Button(frame_juego, text="Volver al Inicio", command=lambda: mostrar_frame(frame_bienvenida))

# Historial
historial_label = tk.Label(frame_juego, text="Historial de Respuestas:", font=("Arial", 12))
historial_label.pack()
historial_text = tk.Text(frame_juego, height=10, width=40, state='disabled')
historial_text.pack(pady=5)

# Mostrar frame inicial
mostrar_frame(frame_bienvenida)

# Iniciar aplicación
ventana.mainloop()
