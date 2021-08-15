from time import sleep, time
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
    state_start = [0]
    state_check = [0]
    state_complete = [1]
    DataBank.set_words(0, [int(uniform(0, 1000))])  # AssyNo
    DataBank.set_words(1, [int(uniform(0, 1000))])  # BodyNo(first 3 digits)
    DataBank.set_words(2, [int(uniform(0, 100))])  # BodyNo(last 2 digits)
    DataBank.set_words(6, [int(uniform(0, 4))])  # Spec info
    #timer = time()
    while True:
        if state_complete != state:
            state_complete = state
            AssyNo = DataBank.set_words(0, [int(uniform(0, 1000))])  # AssyNo
            BodyNo3 = DataBank.set_words(1, [int(uniform(0, 1000))])  # BodyNo(first 3 digits)
            BodyNo2 = DataBank.set_words(2, [int(uniform(0, 100))])   # BodyNo(last 2 digits)
            Spec = DataBank.set_words(6, [int(uniform(0, 4))])     # Spec info
            state_start = DataBank.set_words(3, [int(1)])  # Start point
            print(f"start geldi Assy No: {AssyNo} Body No: {BodyNo3}{BodyNo2} Spek : {Spec}")
            sleep(1)
            state_start = state  # Start point
            print("start noktası resetlendi")
            sleep(9)
            state_check = DataBank.set_words(4, [int(1)])                 # check point
            print("check noktasına geldi")
            sleep(1)
            state_check = state         # check point
            print("check noktası resetlendi")
            sleep(7)
            state_complete = DataBank.set_words(5, [int(1)])                 # complete point
            print("complete nokasına geldi")
            sleep(1)
            #state_complete = state      # complete point
            #timer = time()
            print("complete noktasından geçti")
            sleep(1)


        # if state != DataBank.get_words(1):
        #     state = DataBank.get_words(1)
        #     print(f"register 1'daki deger {state} olarak degisti")
        #sleep(3)
except Exception as e:
    print(e)
    print("server stoplandi")
    server.stop()
    print("server devre disi")