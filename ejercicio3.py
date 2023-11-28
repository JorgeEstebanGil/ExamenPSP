import subprocess
import multiprocessing
import time
import psutil

def abrir_bloque_notas():
    subprocess.run(["notepad.exe"])

def cambiar_prioridad(pid):
    time.sleep(5)
    try:
        process = psutil.Process(pid)
        process.nice(psutil.HIGH_PRIORITY_CLASS)
        print(f"Prioridad de P1 cambiada")
    except Exception as e:
        print(f"Error al cambiar la prioridad: {e}")

def matar_proceso(pid):
    time.sleep(2)
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"P1 terminado por P3")
    except Exception as e:
        print(f"Error al matar el proceso: {e}")

if __name__ == '__main__':
    # Proceso P1
    p1 = multiprocessing.Process(target=abrir_bloque_notas)
    p1.start()

    # Obtener el PID de P1
    pid_p1 = p1.pid

    # Proceso P2 para cambiar la prioridad de P1
    p2 = multiprocessing.Process(target=cambiar_prioridad, args=(pid_p1,))
    p2.start()

    # Proceso P3 para matar a P1
    p3 = multiprocessing.Process(target=matar_proceso, args=(pid_p1,))
    p3.start()

    # Esperar a que todos los procesos terminen
    p1.join()
    p2.join()
    p3.join()
