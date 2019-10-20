import threading
from time import sleep
import time, random
n_sem = 1
semaforo = threading.Semaphore(n_sem)
produtos = [0,0,0,0]

class Produtor(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		

	def run(self):
		semaforo.acquire()
		a = random.randint(1,3)
		b = random.randint(1,3)
		while(a==b):
			b = random.randint(1,3)
		print ("Produtor produz "+str(a)+" e " +str(b))
		produtos[a] = 1
		produtos[b] = 1
		sleep(2)
		semaforo.release()

class Fumante(threading.Thread):
	def __init__(self, id):
		threading.Thread.__init__(self)
		self.id = id

	def run(self):
		if (produtos[self.id] == 0):
			fumar(self.id)

def fumar(id):
	semaforo.acquire()
	global produtos
	for i in range(0,4):
		produtos[i] = 0
	print("Fumante %i consumindo..." %id)
	time.sleep(random.randint(1,10))
	print("Fumante %i terminou de fumar e acordou o vendendor..." %id)
	semaforo.release()

Produtor().start()

fumantes = [Fumante(1), Fumante(2), Fumante(3)]
for f in fumantes:
	f.start()

while 1:
	pass


