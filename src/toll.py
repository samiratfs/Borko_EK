#from sim import get_data
from get_accell import get_data
from time import sleep

while True:
	print(get_data())
	sleep(0.1)
