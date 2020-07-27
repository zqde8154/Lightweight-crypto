import os
import psutil, time, timeit
from os import urandom
from eccsnacks.curve25519 import scalarmult, scalarmult_base
import binascii
lamb = urandom(32)
a = scalarmult_base(lamb)
eps = urandom(32)
start_time = time.clock()
b = scalarmult_base(eps)
print time.clock() - start_time, "seconds"
start_time = time.clock()

c = scalarmult(eps, a)
print time.clock() - start_time, "seconds"
pid = os.getpid()
py = psutil.Process(pid)
print(psutil.cpu_percent())
memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
print('memory use:', memoryUse)

d = scalarmult(lamb, b)



print ("RFID private key: ",binascii.hexlify(eps))

print ("Reader private key: ",binascii.hexlify(lamb))


print ("A value: ",binascii.hexlify(a))
print ("B value: ",binascii.hexlify(b))

print ("C value: ",binascii.hexlify(c))
print ("D value: ",binascii.hexlify(d))
