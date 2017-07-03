from datetime import datetime
from threading import Timer
import os
os.environ["NLS_LANG"] = ".AL32UTF8"
from bdoracle import Orabd

class Recordatorio():

    def __init__(self):
        super().__init__()
        self.ora = Orabd()
        self.hilo()

    def seconds(self):
        x = datetime.today()
        y = x.replace(day=x.day, hour=x.hour, minute=x.minute + 1, second=0, microsecond=0)
        delta_t = y - x
        secs = delta_t.seconds + 1
        return secs

    def checkNotify(self):
        data = self.ora.recordatorio()
        print("checkNotify . . . . . . . .")
        for row in data:
            print(row)
            self.notifyAlert(row)
            print("   -------------------------------   ")
            print("   ")
        return True

    def notifyAlert(self, row):
        if self.ora.updateNotificado(row['folio']):
            print("folio: " + str(row['folio']))
            print("senderID: "+ str(row['senderID']))
            print("beneficiario: "+ str(row['beneficiaryName']))
            print("fecha generada: " + str(row['fechaGenerado']))
            print("fecha caducidad: " + str(row['fechaCaducidad']))
            print("El usuario: "+ str(row['userName']) + "ha sido notificado")
            return True
        else:
            return False

    def hilo(self):
        print(self.seconds())
        self.checkNotify()
        timer = Timer(self.seconds(), self.hilo)
        timer.start()

temporizador = Recordatorio()