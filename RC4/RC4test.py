#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: @manojpandey

# Python 3 implementation for RC4 algorithm
# Brief: https://en.wikipedia.org/wiki/RC4
import os, sys, psutil, timeit
from time import time, process_time

import codecs


def memory_usage():
        process = psutil.Process(os.getpid())
        memory = process.memory_info()[0] / float(2 ** 20)
        return memory



MOD = 256


def KSA(key):
    ''' Key Scheduling Algorithm (from wikipedia):
        for i from 0 to 255
            S[i] := i
        endfor
        j := 0
        for i from 0 to 255
            j := (j + S[i] + key[i mod keylength]) mod 256
            swap values of S[i] and S[j]
        endfor
    '''
    key_length = len(key)
    # create the array "S"
    S = list(range(MOD))  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def PRGA(S):
    ''' Psudo Random Generation Algorithm (from wikipedia):
        i := 0
        j := 0
        while GeneratingOutput:
            i := (i + 1) mod 256
            j := (j + S[i]) mod 256
            swap values of S[i] and S[j]
            K := S[(S[i] + S[j]) mod 256]
            output K
        endwhile
    '''
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K


def get_keystream(key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(key)
    return PRGA(S)


def encrypt_logic(key, text):
    ''' :key -> encryption key used for encrypting, as hex string
        :text -> array of unicode values/ byte string to encrpyt/decrypt
    '''
    # For plaintext key, use this
    # key = [ord(c) for c in key]
    # If key is in hex:
    key = codecs.decode(key, 'hex_codec')
    key = [c for c in key]
    keystream = get_keystream(key)

    res = []
    for c in text:
        val = ("%02X" % (c ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return ''.join(res)


def encrypt(key, plaintext):
    ''' :key -> encryption key used for encrypting, as hex string
        :plaintext -> plaintext string to encrpyt
    '''
    plaintext = [ord(c) for c in plaintext]
    return encrypt_logic(key, plaintext)


def decrypt(key, ciphertext):
    ''' :key -> encryption key used for encrypting, as hex string
        :ciphertext -> hex encoded ciphered text using RC4
    '''
    ciphertext = codecs.decode(ciphertext, 'hex_codec')
    res = encrypt_logic(key, ciphertext)
    return codecs.decode(res, 'hex_codec').decode('utf-8')

def main():

    key = '536563726574'  # plaintext

    plaintext = 'Attack at dawn'  # plaintext
    # encrypt the plaintext, using key and RC4 algorithm

    start_time_1 = time()
    start_time = process_time()

    ciphertext = encrypt(key, plaintext)
    pid = os.getpid()
    py = psutil.Process(pid)

    print("RAM usage :",memory_usage())
    print("CPU usage in percenage:",psutil.cpu_percent())
    print('plaintext:', plaintext)
    print('ciphertext:', ciphertext)
    print("Excution time--- %s seconds ---" % (time() - start_time_1))
    print("CPU time --- %s seconds ---" % (process_time() - start_time))
   
    clock_time_sum = 0
    cpu_time_sum = 0
    for i in range(1000):
        start_time_1 = time()
        start_time = process_time()
        ciphertext = encrypt(key, plaintext)
        pid = os.getpid()
        py = psutil.Process(pid)
        cpu_time_sum += (process_time() - start_time)
        clock_time_sum += (time() - start_time_1)
    print("CPU usage in percenage:",psutil.cpu_percent())
    print("Clock time measured over 1000 iteration = ", clock_time_sum)
    print("CPU time measured over 1000 iteration:", cpu_time_sum)


    start_time_2 = time()
    start_time_3 = process_time()

    decrypted = decrypt(key, ciphertext)
    pid = os.getpid()
    py = psutil.Process(pid)




    print('decrypted:', decrypted)
    print("RAM usage :",memory_usage())
    print("CPU usage in percenage:",psutil.cpu_percent())
    print("Excution time--- %s seconds ---" % (time() - start_time_1))
    print("CPU time --- %s seconds ---" % (process_time() - start_time))
   
    clock_time_sum = 0
    cpu_time_sum = 0
    for i in range(1000):
        start_time_1 = time()
        start_time = process_time()
        decrypted = decrypt(key, ciphertext)
        pid = os.getpid()
        py = psutil.Process(pid)
        cpu_time_sum += (process_time() - start_time)
        clock_time_sum += (time() - start_time_1)
    print("CPU usage in percenage:",psutil.cpu_percent())
    print("Clock time measured over 1000 iteration = ", clock_time_sum)
    print("CPU time measured over 1000 iteration:", cpu_time_sum)
    
    # key = '4B6579' # 'Key' in hex
    # key = 'Key'
    # plaintext = 'Plaintext'
    # ciphertext = 'BBF316E8D940AF0AD3'

    # Test case 2
    # key = 'Wiki' # '57696b69'in hex
    # plaintext = 'pedia'
    # ciphertext should be 1021BF0420

    # Test case 3
    # key = 'Secret' # '536563726574' in hex
    # plaintext = 'Attack at dawn'
    # ciphertext should be 45A01F645FC35B383552544B9BF5

if __name__ == '__main__':
    main()
