import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo_origen():
    global archivo_origen
    archivo_origen = filedialog.askopenfilename(title="Selecciona el archivo de origen", filetypes=[("Archivos de texto", "*.txt")])
    archivo_origen_label.config(text=f"Archivo de origen: {archivo_origen}")

def seleccionar_archivo_destino():
    global archivo_destino
    archivo_destino = filedialog.askopenfilename(title="Selecciona el archivo de destino", filetypes=[("Archivos de texto", "*.txt")])
    archivo_destino_label.config(text=f"Archivo de destino: {archivo_destino}")

def insertar_archivo():
    if not archivo_origen or not archivo_destino:
        resultado_label.config(text="Debes seleccionar ambos archivos.")
        return

    try:
        with open(archivo_origen, 'r') as origen_file:
            contenido_origen = origen_file.read()

        with open(archivo_destino, 'r') as destino_file:
            contenido_destino = destino_file.readlines()

        linea_insertar = 13  # Línea en la que deseas insertar el archivo
        contenido_destino.insert(linea_insertar - 1, contenido_origen)

        with open(archivo_destino, 'w') as destino_file:
            destino_file.writelines(contenido_destino)

        resultado_label.config(text=f"Archivo insertado en la línea {linea_insertar} de '{archivo_destino}'.", fg="green")

    except Exception as e:
        resultado_label.config(text=f"Error: {str(e)}", fg="red")

def cerrar_aplicacion():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Inserción de Archivos")
root.configure(bg="#f0f0f0")  # Fondo gris claro

archivo_origen = None
archivo_destino = None

# Botón para seleccionar el archivo de origen
seleccionar_origen_button = tk.Button(root, text="Seleccionar Archivo de Origen", command=seleccionar_archivo_origen)
seleccionar_origen_button.pack(pady=10)
seleccionar_origen_button.configure(bg="#ffcc99")  # Fondo color melocotón

# Botón para seleccionar el archivo de destino
seleccionar_destino_button = tk.Button(root, text="Seleccionar Archivo de Destino", command=seleccionar_archivo_destino)
seleccionar_destino_button.pack(pady=10)
seleccionar_destino_button.configure(bg="#ffcc99")  # Fondo color melocotón

# Etiquetas para mostrar los nombres de los archivos seleccionados
archivo_origen_label = tk.Label(root, text="Archivo de origen: ", wraplength=300, bg="#f0f0f0")
archivo_origen_label.pack()
archivo_destino_label = tk.Label(root, text="Archivo de destino: ", wraplength=300, bg="#f0f0f0")
archivo_destino_label.pack()

# Botón para iniciar la inserción
insertar_button = tk.Button(root, text="Insertar Archivo", command=insertar_archivo)
insertar_button.pack(pady=20)
insertar_button.configure(bg="#99ffcc")  # Fondo color verde menta

# Botón para cerrar la aplicación
cerrar_button = tk.Button(root, text="Cerrar", command=cerrar_aplicacion)
cerrar_button.pack(pady=10)
cerrar_button.configure(bg="#ff9999")  # Fondo color rosa claro

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="", bg="#f0f0f0")
resultado_label.pack()

root.mainloop()
