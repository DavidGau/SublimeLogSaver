from automatisation import *
import datetime
import time

time.sleep(2)
i = 0
while i < 5:
	print("Test de l'enregistreur de logs")
	print(datetime.datetime.now())

	developpment("C:\\Users\\Dave\\Desktop\\testingit","hg{0}".format(i),False)
	i += 1
