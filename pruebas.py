import time
import sys

for i in range(5, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} ".format(i))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rBienvenido!            \n")