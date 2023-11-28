import threading
import queue
import random
import time

#Clase productor
class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, queue, PT):
        """
        ConstruCTor.

        @param integers list of integers
        @param event event synchronization objeCT
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
    
    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        while True:
            for _ in range(15):
                num = random.randint(100, 500)
                self.queue.put(num)
                print(f"Producido: {num}")
                time.sleep(self.PT) # @PT Producer time

#Clase consumidor
class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, queue,CT,X):
        """
        ConstruCTor.

        @param integers list of integers
        @param event event synchronization objeCT
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.CT = CT
        self.X = X
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            numeros = []
            for i in range(self.X):
                numeros.append(self.queue.get())
                print(f"Consumiendo: {numeros[i]}")

            print(f"Consumidos: {numeros}")
            Multiplicacion = self.multiplicar(numeros)
            print(f"Consumidos: {numeros}, Multiplicacion: {Multiplicacion}")
            time.sleep(self.CT) #CT Consumer time
    
    def multiplicar(self, lista):
        resultado = 1
        for numero in lista:
            resultado *= numero
        return resultado

#Clase main
class ProductorConsumidor:

    def __init__(self, relacion_pc, PT, CT, X):
        self.queue = queue.Queue()
        self.relacion_pc = relacion_pc
        self.PT = PT
        self.CT = CT
        self.X = X

    def iniciar_simulacion(self):
        for _ in range(self.relacion_pc[0]):
            produCTor = Producer(self.queue, self.PT)
            produCTor_thread = threading.Thread(target=produCTor.run)
            produCTor_thread.start()
            time.sleep(1)
            
        for _ in range(self.relacion_pc[1]):
            consumidor = Consumer(self.queue, self.CT, self.X)
            consumidor_thread = threading.Thread(target=consumidor.run)
            consumidor_thread.start()
            time.sleep(1)

# Relación 1:1, PT=1, CT=4, X=3
pc1 = ProductorConsumidor(relacion_pc=(1, 1), PT=1, CT=4, X=3)
pc1.iniciar_simulacion()

# Relación 4:2, PT=2, CT=2, X=2
pc2 = ProductorConsumidor(relacion_pc=(4, 2), PT=2, CT=2, X=2)
pc2.iniciar_simulacion()

# Relación 2:6, PT=1, CT=10, X=4
pc3 = ProductorConsumidor(relacion_pc=(2, 6), PT=1, CT=10, X=4)
pc3.iniciar_simulacion()
