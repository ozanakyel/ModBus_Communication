from time import sleep
from random import uniform
from pyModbusTCP.server import ModbusServer, DataBank

host = "127.0.0.1"
port = 502
server = ModbusServer(host, port, no_block=True)

try:
    print("server is starting....")
    server.start()
    print(f"server IP: {host} {port}")
    state = [0]
    while True:
        DataBank.set_words(0, [int(uniform(0,100))])
        if state != DataBank.get_words(1):
            state = DataBank.get_words(1)
            print(f"register 1'daki deger {state} olarak degisti")
            sleep(0.5)
except:
    print("server stoplandi")
    server.stop()
    print("server devre disi")