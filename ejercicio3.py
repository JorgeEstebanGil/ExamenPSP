import subprocess
import multiprocessing
import time
import psutil

def P1_Abrir_Bloc():
    subprocess.run(["cmd.exe"])

def P2_CambioPrioridad(pid):
    time.sleep(5)
    try:
        process = psutil.Process(pid)
        process.nice(psutil.HIGH_PRIORITY_CLASS)
        print(f"Prioridad de P1 cambiada")
    except Exception as e:
        print(f"Error al cambiar la prioridad: {e}")

def P3_KillProceso(pid):
    time.sleep(10)
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"P1 terminado por P3")
    except Exception as e:
        print(f"Error al matar el proceso: {e}")

if __name__ == '__main__':
    # Proceso P1
    p1 = multiprocessing.Process(target=P1_Abrir_Bloc)
    p1.start()

    # Obtener el PID de P1
    pid_p1 = p1.pid

    # Proceso P2 para cambiar la prioridad de P1
    p2 = multiprocessing.Process(target=P2_CambioPrioridad, args=(pid_p1,))
    p2.start()

    # Proceso P3 para matar a P1
    p3 = multiprocessing.Process(target=P3_KillProceso, args=(pid_p1,)) 
    p3.start()

    # Esperar a que todos los procesos terminen
    p1.join()
    p2.join()
    p3.join()

#El programa no corre correctamente ya que no encuentra el proceso P1, esto se debe a que el proceso P3 lo mata antes de que P2 pueda cambiar su prioridad.
#Para solucionarlo, se debe de cambiar el tiempo de espera en el proceso P3 para que P2 pueda cambiar la prioridad de P1 antes de que P3 lo mate.   
#Si el tiempo dado por el enunciado entre P2 y p2 es de 2, la solucion sería poner uno mayor teniendo en cuenta que en P2 se espera 5 segundos.
#Por ejemplo si ponemos 10 segundo de sleep a P3, entonces P2 tendrá el tiempo suficeinte para cambiar la prioridad de P1 antes de que P3 lo mate.
#opr matemática el sleep de P3 debería ser mayor a 5 segundos, ya que P2 tarda 5 segundos en cambiar la prioridad de P1.