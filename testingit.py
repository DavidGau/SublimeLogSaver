from automatisation import *
import datetime
import time

time.sleep(2)
i = 0
while i < 1:
	print("Test de l'enregistreur de logs")
	print(datetime.datetime.now())

	developpment("automatisation","C:\\Users\\Dave\\Desktop\\testingit","hdg{0}".format(i),False,True)
	i += 1
