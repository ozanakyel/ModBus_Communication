from pyModbusTCP.client import ModbusClient
from time import sleep
from threading import Thread
from random import uniform


class ClientThreading(Thread):
    """This is a client with threading for ModBusTCP communication."""

    def __init__(self):
        Thread.__init__(self)
        self.host = "127.0.0.1"
        self.port = 502  # 502
        self.client = ModbusClient(self.host, self.port)
        print(f"hedef {self.host} ve {self.port}")
        self.register_0 = None
        self.register_1 = None
        self.register_2 = None
        self.register_3 = None
        self.register_4 = None
        self.register_5 = None
        self.register_6 = None
        self.register_sifir_old = 0

    def run(self):
        while True:
            if self.client.open():
                # print("client canli")
                self.register_0 = self.client.read_holding_registers(0)
                self.register_1 = self.client.read_holding_registers(1)
                self.register_2 = self.client.read_holding_registers(2)
                self.register_3 = self.client.read_holding_registers(3)
                self.register_4 = self.client.read_holding_registers(4)
                self.register_5 = self.client.read_holding_registers(5)
                self.register_6 = self.client.read_holding_registers(6)
                # print(f"run:{self.register_sifir}")
                # client.write_single_register(1, int(uniform(1, 100)))
            else:
                print("baglanti kurulamadi")
            # sleep(2)

    def get_registers_value(self):
        while True:
            if self.register_sifir != self.register_sifir_old:
                self.register_sifir_old = self.register_sifir
                return [self.register_sifir,
                        self.register_1,
                        self.register_2,
                        self.register_3,
                        self.register_4,
                        self.register_5,
                        self.register_6]

"""    def get_registers_value(self):
        while True:
            if self.register_sifir != self.register_sifir_old:
                self.register_sifir_old = self.register_sifir
                return [self.register_sifir,
                        self.register_1,
                        self.register_2,
                        self.register_3,
                        self.register_4,
                        self.register_5,
                        self.register_6]"""


#    https://pymodbustcp.readthedocs.io/en/latest/examples/modbus_thread.html    ////  burdaki adreste güzel bir register yoklama örneği var incelenmeli ona göre revizyon yapılabilir