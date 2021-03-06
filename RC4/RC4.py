import sys
def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    
    return PRGA(S)


key="0102030405"

plaintext = 'Hello'

if (len(sys.argv)>1):
	plaintext=str(sys.argv[1])

if (len(sys.argv)>2):
	key=str(sys.argv[2])

key =  bytes.fromhex(key)

keystream = RC4(key)
print ("Keystream:\t", end='')
for i in range (0,15):
	print (hex(next(keystream))[2:],end='')

print ("\nPlaintext:\t",plaintext)
print ("Cipher:\t\t",end='')
keystream = RC4(key)

for c in plaintext:
	sys.stdout.write("%02X" % (ord(c) ^ next(keystream)))

print ("\n\nS-box: ",KSA(key))
