import psutil
import struct

#Programa diseñado para consola. 


#Lista de las ids de procesos totales mediante psutil.pids(), presentado como cantidad con el len().
process_count = len(psutil.pids())

# La cantidad de hilos (Usando el calculo ya que python no tiene ninguna librería directa para esto.)

threads_count = psutil.cpu_count(logical=False)*psutil.cpu_count(logical=True)

#Con psutil.cpu_count() obtengo la cantidad de nucleos de cpu.

cpus_count = psutil.cpu_count(logical=False)

#Con psutil.virtual_memory() obtengo toda la información de la memoria.

memory_size = psutil.virtual_memory().total

#Con Struct, sacamos el bus de datos.
#Este devuelve 4 u 8 punteros.
#Multiplicamos por 8 para presentar la cantidad referente de bits. 

databus = struct.calcsize('P')*8

#print() para presentar la data por pantalla. 

print(
	f"Bus de Datos = {databus}",
	f"Cantidad de Hilos = {threads_count}",
	f"Cantidad de Procesos = {process_count}",
	f"Cantidad de Procesadores = {cpus_count}",
	f"Cantidad de Memoria Ram = {memory_size} GB", sep='\n'
	)
