from time import sleep
from random import uniform
from pyModbusTCP.server import ModbusServer, DataBank

host = "127.0.0.1"
port = 502
server = ModbusServer(host, port, no_block=True)
spec = ["corolla_black", "corolla_white", "chr_balck", "chr_white"]
try:
    print("server is starting....")
    server.start()
    print(f"server IP: {host} {port}")
    state = [0]
    while True:
        DataBank.set_words(0, [int(uniform(0, 1000))])       # AssyNo
        DataBank.set_words(1, [int(uniform(0, 1000))])       # BodyNo(first 3 digits)
        DataBank.set_words(2, [int(uniform(0, 100))])        # BodyNo(last 2 digits)
        DataBank.set_words(3, [int(1)])                     # Start point
        DataBank.set_words(4, [int(1)])                     # check point
        DataBank.set_words(5, [int(1)])                     # Complete point
        DataBank.set_words(6, [int(uniform(0, 4))])         # Spec info
        # if state != DataBank.get_words(1):
        #     state = DataBank.get_words(1)
        #     print(f"register 1'daki deger {state} olarak degisti")
        sleep(3)
except Exception as e:
    print(e)
    print("server stoplandi")
    server.stop()
    print("server devre disi")