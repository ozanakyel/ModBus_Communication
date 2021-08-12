from client_thread import ClientThreading
from time import sleep, time
from random import uniform

client = ClientThreading()
client.start()

while True:
    start_time = time()
    register_zero = client.get_registersifir()
    end_time = time()
    zaman = end_time-start_time
    print(f"gelen deger={register_zero} gecen zaman= {str(round(zaman, 2))}")