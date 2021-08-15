from client_thread import ClientThreading
from time import sleep, time
from random import uniform

client = ClientThreading()
client.start()
timer = time()

state = [0]
state1 = [1]



while True:
    start_time = time()
    registers_values = client.get_registers_value()
    end_time = time()
    zaman = end_time-start_time
    print(f"gelen deger={registers_values} gecen zaman= {str(round(zaman, 2))}")

