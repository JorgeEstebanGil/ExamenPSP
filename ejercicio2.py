import os
import tempfile
import threading
import subprocess
import time

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
lock = threading.Lock()

def code(name):
    time.sleep(10)
    with lock:
        with open(file_name, 'a') as f:  # Cambiado 'w' a 'a' para escribir en lugar de sobrescribir
            print("Guardando en " + file_name)
            f.write("Código limpio fue escrito por " + str(name) + '\n') 
        subprocess.run(["ping", "google.com"])

# Creacion hilos
threads = []
for i in range(5):
    thread = threading.Thread(target=code, args=(i,))
    thread.start()
    threads.append(thread)

# Terminar hilos
for thread in threads:
    thread.join()

# Leer el archivo
with open(file_name, 'r') as f:
    content = f.read()
    print("Contenido del archivo:")
    print(content)
