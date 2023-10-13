import numpy as np
import tkinter as tk

# Function based on https://neurostars.org/t/heudiconv-no-extraction-of-slice-timing-data-based-on-philips-dicoms/2201/12
def calcular_tiempo_de_corte():
    TRsec = float(tr_entry.get())
    nSlices = int(slices_entry.get())
    TA = TRsec / nSlices  # asume que no hay espacio temporal entre volúmenes
    bidsSliceTiming = np.arange(0, TRsec, TA)

    if not slice_order_var.get():
        bidsSliceTiming = np.flip(bidsSliceTiming)

    if interleave_var.get():
        order = np.concatenate((np.arange(1, nSlices + 1, 2), np.arange(2, nSlices + 1, 2)))
        reorderedTiming = np.empty_like(bidsSliceTiming)
        reorderedTiming[order - 1] = bidsSliceTiming
        bidsSliceTiming = reorderedTiming

    # Mostrar los resultados en la interfaz gráfica
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, '"SliceTiming": [\n')
    for i in range(nSlices):
        result_text.insert(tk.END, f'    {bidsSliceTiming[i]:g}')
        if i < nSlices - 1:
            result_text.insert(tk.END, ',\n')
        else:
            result_text.insert(tk.END, '],')
    result_text.config(state=tk.DISABLED)

# Crear la ventana principal
window = tk.Tk()
window.title("Slice Timing Calculator")

# Crear etiquetas y campos de entrada
tr_label = tk.Label(window, text="TR (s):")
tr_label.pack()
tr_entry = tk.Entry(window)
tr_entry.pack()

slices_label = tk.Label(window, text="Slices number:")
slices_label.pack()
slices_entry = tk.Entry(window)
slices_entry.pack()

slice_order_var = tk.BooleanVar()
slice_order_checkbox = tk.Checkbutton(window, text="Ascending Order?", variable=slice_order_var)
slice_order_checkbox.pack()

interleave_var = tk.BooleanVar()
interleave_checkbox = tk.Checkbutton(window, text="Interleaved?", variable=interleave_var)
interleave_checkbox.pack()

calculate_button = tk.Button(window, text="Slice Timing calculation", command=calcular_tiempo_de_corte)
calculate_button.pack()

result_text = tk.Text(window, height=10, width=40, state=tk.DISABLED)
result_text.pack()

window.mainloop()
