from datetime import datetime
from threading import Timer
import time

class MyTemporizador():


    def __init__(self) -> None:
        super().__init__()
        self.dia = 0
        self.hello_world()

    def hello_world(self):
        self.dia = self.dia +1

        if self.dia == 2:
            print("Ya paga culero, es tu último día.")
        elif self.dia > 2:
            print("Ya mamaste we, cancelado")
            self.dia = 0
        else :
            print("llevas " + str(self.dia) + " días")


        x = datetime.today()
        # y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
        y = x.replace(day=x.day, hour=x.hour, minute=x.minute+1, second=50, microsecond=0)
        delta_t = y - x
        secs = delta_t.seconds
        print(x)
        print("-----")
        print(y)
        print("hello world")
        print(secs)
        print(" ")
        timer = Timer(secs, self.hello_world())
        timer.start()

temporizador = MyTemporizador()


#Este código se ejecuta en una hora exacta, pero no lo vuelve a ejecutar