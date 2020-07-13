from os import urandom
from eccsnacks.curve25519 import scalarmult, scalarmult_base
import binascii

lamb = urandom(32)
a = scalarmult_base(lamb)

eps = urandom(32)
b = scalarmult_base(eps)

c = scalarmult(eps, a)

d = scalarmult(lamb, b)

print ("RFID private key: ",binascii.hexlify(eps))

print ("Reader private key: ",binascii.hexlify(lamb))


print ("A value: ",binascii.hexlify(a))
print ("B value: ",binascii.hexlify(b))

print ("C value: ",binascii.hexlify(c))
print ("D value: ",binascii.hexlify(d))
