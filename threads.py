import threading
from time import sleep as delay

def func(arg):
	print("1")
	delay(20)
	print("3")
	
thread = threading.Thread(target=func, args=("a"))
thread.start()
print("2")
thread.join()
print("4")