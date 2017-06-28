import time, threading
def foo():
    print(time.ctime())
    threading.Timer(10, foo).start()

foo()

#Este codigo se ejecuta cada 10 segundos, pero queda corriendo el proceso y puede consumir memoria de más