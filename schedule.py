from datetime import datetime
from threading import Timer
import time

x=datetime.today()
# y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
y=x.replace(day=x.day, hour=x.hour, minute=x.minute, second=50, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print("hello world")

t = Timer(secs, hello_world)
t.start()

#Este código se ejecuta en una hora exacta, pero no lo vuelve a ejecutar