## For source code of clefia cipher in Python see clefia_2.py
from clefia_2 import setKey, encrypt, decrypt, ksTable
import os, sys, psutil, timeit
from time import time, process_time
import binascii, codecs
import numpy as np 

if __name__ == "__main__":

    def memory_usage():
        process = psutil.Process(os.getpid())
        memory = process.memory_info()[0] / float(2 ** 20)
        return memory

    mess = int('0x000102030405060708090a0b0c0d0e0f', 16) # 8 bytes message converted to int
    key = 0xffeeddccbbaa99887766554433221100f0e0d0c0b0a090807060504030201000

    def my_function_clefia(mess, key, keySize = "SIZE_256"):
        #key schedule
        setKey(key, keySize)
        #encryption
        ctext = encrypt(mess)
        #decryption
        ptext = decrypt(ctext)
        return 0

    if (1==1):
        my_function_clefia(mess, key)
        pid = os.getpid()
        py = psutil.Process(pid)

    print("RAM usage :",memory_usage())
    print("CPU usage in percenage:",psutil.cpu_percent())
    start_time_1 = time()
    start_time = process_time()
    my_function_clefia(mess, key)
    print("Excution time--- %s seconds ---" % (time() - start_time_1))
    print("CPU time --- %s seconds ---" % (process_time() - start_time))

    clock_time_sum = 0
    cpu_time_sum = 0
    for i in range(1000):
        start_time_1 = time()
        start_time = process_time()
        my_function_clefia(mess, key)
        pid = os.getpid()
        py = psutil.Process(pid)
        cpu_time_sum += (process_time() - start_time)
        clock_time_sum += (time() - start_time_1)
    print("CPU usage in percenage:",psutil.cpu_percent())
    print("Clock time measured over 1000 iteration = ", clock_time_sum)
    print("CPU time measured over 1000 iteration:", cpu_time_sum)
