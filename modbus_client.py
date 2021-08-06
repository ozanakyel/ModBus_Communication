from pyModbusTCP.client import ModbusClient
from time import sleep
from random import uniform

host = "127.0.0.1"
port = 502   #502

client = ModbusClient(host, port)
print(f"hedef {host} ve {port}")
while True:
    if client.open():
        #print("client oluşturuldu")
        register_sifir = client.read_holding_registers(0)
        print(register_sifir)
        client.write_single_register(1, int(uniform(1, 100)))
    else:
        print("baglanti kurulamadi")
    sleep(2)
