import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo_origen():
    global archivo_origen
    archivo_origen = filedialog.askopenfilename(title="Selecciona el archivo de origen")
    archivo_origen_label.config(text=f"Archivo de origen: {archivo_origen}")

def seleccionar_archivo_destino():
    global archivo_destino
    archivo_destino = filedialog.askopenfilename(title="Selecciona el archivo de destino")
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

        resultado_label.config(text=f"Archivo insertado en la línea {linea_insertar} de '{archivo_destino}'.")

    except Exception as e:
        resultado_label.config(text=f"Error: {str(e)}")

def cerrar_aplicacion():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Inserción de Archivos")

archivo_origen = None
archivo_destino = None

# Botón para seleccionar el archivo de origen
seleccionar_origen_button = tk.Button(root, text="Archivo Slicetiming", command=seleccionar_archivo_origen)
seleccionar_origen_button.pack(pady=10)

# Botón para seleccionar el archivo de destino
seleccionar_destino_button = tk.Button(root, text="Archivo json func", command=seleccionar_archivo_destino)
seleccionar_destino_button.pack(pady=10)

# Etiquetas para mostrar los nombres de los archivos seleccionados
archivo_origen_label = tk.Label(root, text="Archivo de origen: ", wraplength=300)
archivo_origen_label.pack()
archivo_destino_label = tk.Label(root, text="Archivo de destino: ", wraplength=300)
archivo_destino_label.pack()

# Botón para iniciar la inserción
insertar_button = tk.Button(root, text="Insertar Archivo", command=insertar_archivo)
insertar_button.pack(pady=20)

# Botón para cerrar la aplicación
cerrar_button = tk.Button(root, text="Cerrar", command=cerrar_aplicacion)
cerrar_button.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="", fg="green")
resultado_label.pack()

root.mainloop()
