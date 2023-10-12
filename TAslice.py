"""
Autor: Pablo Reyes
Fecha: Octubre 2023
Correo: pabloreyesg@gmail.com
Descripción: Este script realiza ciertas operaciones relacionadas con el tiempo de adquisición 
de imágenes de resonancia magnética. 

"""

#
# El siguiene script esta basado en la version original de Chris Rorden 2019 para MATLAB
# Se requiere ingresar:
# TR = Tiempo de repetición
# nSlices = numero de slices o cortes
# se debe cambiar los valores de False o True dependiendo de si es ascendente, descendente o intervalar. 

# Estos valores deben buscarse directamente en la pantalla de la estacion del tyrabajo del resonador
# https://neurostars.org/t/heudiconv-no-extraction-of-slice-timing-data-based-on-philips-dicoms/2201/12

import numpy as np
import sys

# Redirige la salida estándar al archivo 'slicetiming.txt'
sys.stdout = open('slicetiming.txt', 'w')

TRsec = 2.5 #realice el cambio en esta sección y digite el TR de su secuencia.
nSlices = 66 #realice el cambio de esta sección y digite el numero de cortes de sus secuencia.
TA = TRsec / nSlices  # asume que no hay espacio temporal entre volúmenes
bidsSliceTiming = np.arange(0, TRsec, TA)  # ascendente

if False:  # En False significa que el orden sera ascendente, en True sera descendente
    bidsSliceTiming = np.flip(bidsSliceTiming)

if True:  # Si esta en TRUE significa que hay intercalado o intervalar. Si esta en FALSE se omitirá.
    order = np.concatenate((np.arange(1, nSlices + 1, 2), np.arange(2, nSlices + 1, 2)))
    reorderedTiming = np.empty_like(bidsSliceTiming)
    reorderedTiming[order - 1] = bidsSliceTiming
    bidsSliceTiming = reorderedTiming

# reportar resultados
print('"SliceTiming": [')
for i in range(nSlices):
    print(f'    {bidsSliceTiming[i]:g}', end='')
    if i < nSlices - 1:
        print(',')
    else:
        print('],')

# Cierra el archivo después de redirigir la salida
sys.stdout.close()
