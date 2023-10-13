import subprocess
import tkinter as tk
from tkinter import filedialog

def convert_to_bids():
    participant = entry.get()
    pthr = directory_raw.get()
    pthheu = file_heuristic.get()
    pthbids = directory_bids.get()

    cmd = f"heudiconv -d {pthr}/{{subject}}/*/* -s {participant} -f {pthheu} -b -o {pthbids}"
    subprocess.run(cmd, shell=True)

    result_label.config(text=f"Done {participant}")

# Crear la ventana principal
window = tk.Tk()
window.title("Dicom to BIDS Heudiconv")

# Ajustar el ancho de la ventana
window.geometry("400x200")

# Crear y configurar etiquetas y campos de entrada
tk.Label(window, text="Enter code:").pack()
entry = tk.Entry(window)
entry.pack()

tk.Label(window, text="Directory for raw data:").pack()
directory_raw = tk.Entry(window)
directory_raw.pack()
directory_raw.insert(0, "/media/pablo/Kirk/REDLATMA/raw") # chagen this

tk.Label(window, text="Path to heuristic file:").pack()
file_heuristic = tk.Entry(window)
file_heuristic.pack()
file_heuristic.insert(0, "/media/pablo/Kirk/REDLATMA/heuristic2023.py") #change this

tk.Label(window, text="Directory for BIDS data:").pack()
directory_bids = tk.Entry(window)
directory_bids.pack()
directory_bids.insert(0, "/media/pablo/Kirk/REDLATMA/bids") #change this

# Botón para ejecutar la conversión
convert_button = tk.Button(window, text="Convert to BIDS", command=convert_to_bids)
convert_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text="")
result_label.pack()

# Iniciar la ventana principal
window.mainloop()
