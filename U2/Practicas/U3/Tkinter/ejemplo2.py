import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Acceso al Sistema")
ventana.geometry("300x150")

# Definir la logica de validacion
def validar_datos():
    usuario = caja_usuario.get()
    clave = caja_clave.get()
    
    if usuario == "admin" and clave == "1234":
        messagebox.showinfo("Exito", "Acceso concedido al sistema.")
    else:
        messagebox.showerror("Error", "Credenciales incorrectas.")

# columna 0
etiqueta_usuario = tk.Label(ventana, text="Usuario:")
etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")

etiqueta_clave = tk.Label(ventana, text="Contrasena:")
etiqueta_clave.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# columna 1
caja_usuario = tk.Entry(ventana)
caja_usuario.grid(row=0, column=1, padx=10, pady=10)

# El parametro show oculta el texto
caja_clave = tk.Entry(ventana, show="*")
caja_clave.grid(row=1, column=1, padx=10, pady=10)

# abarca dos columnas
boton_entrar = tk.Button(ventana, text="Entrar", command=validar_datos)
boton_entrar.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()