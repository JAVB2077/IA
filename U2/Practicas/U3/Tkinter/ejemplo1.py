import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera App")
ventana.geometry("350x250")
ventana.config(bg="#f4f7f6")

# Definir la logica del boton
def saludar_usuario():
    nombre = caja_texto.get()
    
    if nombre == "":
        # Alerta si el campo esta vacio
        messagebox.showwarning("Atencion", "Por favor, escribe tu nombre.")
    else:
        # Mostrar el saludo y limpiar la caja
        etiqueta_resultado.config(text=f"Bienvenido a la clase, {nombre}.", fg="#27ae60")
        caja_texto.delete(0, tk.END)

# Crear y posicionar los widgets
etiqueta_instruccion = tk.Label(ventana, text="¿Cual es tu nombre?", font=("Arial", 12), bg="#f4f7f6")
etiqueta_instruccion.pack(pady=15)

caja_texto = tk.Entry(ventana, font=("Arial", 12), width=20, justify="center")
caja_texto.pack(pady=5)

boton_saludar = tk.Button(ventana, text="Saludar", command=saludar_usuario, font=("Arial", 11, "bold"))
boton_saludar.pack(pady=15)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#f4f7f6")
etiqueta_resultado.pack(pady=20)

# Iniciar la aplicacion
ventana.mainloop()