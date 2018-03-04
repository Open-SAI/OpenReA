#*-*coding:utf-8*-*
#qpy:kivy
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label 
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.image import Image 

class ScreenLogin(RelativeLayout):
#class ScreenLogin(App):
    def build(self):
        self.rl = RelativeLayout()
        self.img = Image()
        self.lb  = Label(font_size="18dp", pos= (10, -180) , markup=True)
        self.opc = False
        self.opc1 = False
        self.cont1 = 0
        self.img.source = "Imagenes/Screen1.png"
  #      self.img.size = (880, 440)
        self.img.pos=(0,0)
        self.rl.add_widget(self.img)
        self.rl.add_widget(self.lb)
        self.Procesos_Bluetooth()
        self.mensaje1 = "[color=ff3333] Coloque su llave en el lector por favor."
        self.blueRequest = "Nada"
        Clock.schedule_interval(self.Cont1, 0.45) 
        Clock.schedule_interval(self.IDENTIFICADOR_P, 0.3)
        return self.rl


    # FUNCIÓN TIPO RELOJ PARA COLOCAR Y QUITAR LOS AVISOS
    def Cont1(self, dt):
        print self.cont1
        Mensaje = "a \r\n"
        try:
            ArduinoB.Escribir(Mensaje)
        except:
            pass
        
        try:            
            self.blueRequest =  ArduinoB.LeerCADENA() # LECTURA DEL BLUETOOTH ALMACENDA EN UNA VARIABLE            
        except:
            pass
        if ((self.blueRequest== "Nada")or(len(self.blueRequest)<5)):

            if (self.cont1 <= 2):
                print "Llamando el aviso"
                self.AvisON()
                self.cont1 = self.cont1 + 1
                
            if ((self.cont1 > 2)or(self.cont1 == 4)):
                print "Quitando el aviso"
                self.AvisOFF()
                self.cont1 = self.cont1 + 1
            
            if (self.cont1 > 4):
                self.cont1 = 0
                self.opc = False
                self.opc1 = False

                
        if ((len(self.blueRequest) != 0) and (self.blueRequest!= "Nada")):
            print "===========> la longitud de la puta variable es: " + str(len(self.blueRequest))
            print "NUID encontrada, Deteneiendo el hilo"
            Clock.unschedule(self.Cont1)
            print type(self.blueRequest)
            self.opc = False
            dataBlue = []
            dataBlue = self.blueRequest.split(" ")
            print dataBlue[0]
            print len(dataBlue)
            mensaje = ""
            for i in range (1, len(dataBlue), 1):
                mensaje = mensaje + str(dataBlue[i])
            print mensaje                
            self.mensaje1 = " [color=ff3333] NUID encontrada: " + str(mensaje)
            self.AvisON()
            self.blueRequest = str(mensaje)
            self.bufferLectura()

    # DEFINO UN BUFFER PARA LA LECTURA DEL BLUETOOTH
    def bufferLectura(self):
        lectura_del_Bluetooth = str(self.blueRequest)
        return lectura_del_Bluetooth

    # FUNCIÓN PARA ENCENDER LA LECTURA DE LA TARJETA NUEVAMENTE
    def ReiniciarLectura(self):
        self.blueRequest = "Nada"
        self.mensaje1 = "[color=ff3333] Coloque su llave en el lector por favor."
        try:
            Clock.unschedule(self.Cont1)
        except:
            pass
        try:
            Clock.schedule_interval(self.Cont1, 0.45)
        except:
            pass


            
    #PONER EL AVISO
    def AvisON(self):
        if (self.opc == False):
            self.lb.text = str(self.mensaje1)
            self.opc = True

        if (self.opc == True):
            pass


    # QUITAR EL AVISO
    def AvisOFF(self):
        if (self.opc1 == False):
            self.lb.text = " "
            self.opc1 = True

        if (self.opc1 == True):
            pass


    #IDENTIFICADOR DE PROCESOS DEL BLUETOOTH
    def Procesos_Bluetooth(self):
        try:
            from Ardutooth import ArduinoBluetooth 
            global ArduinoB
            ArduinoB = ArduinoBluetooth()
            Mensaje = "Procesos Bluetooth Activados "
            print Mensaje 
            self.EncenderBluetooth()
        except:
            Mensaje = "Fallo al activar los procesos Arduino"
            print Mensaje
        pass
        
    #FUNCIÓN PARA ENCENDER EL BLUETOOTH     
    def EncenderBluetooth(self, *args):
        print "Llamado a prender"
        try:
            Dispo = "HC-05"
            ArduinoB.obtenerCorrienteEnchufe('HC-05')
            Mensaje = "Dispositivo conectado"
            print Mensaje
        except:
            Mensaje = "Dispositivo NO CONECTADO revise su conexion "
            print Mensaje
            ArduinoB.obtenerCorrienteEnchufe("HC-05")



    def ApagarBluetooth(self):
        try:
            ArduinoB.Cerrar()
        except:
            print "No se pudo cerrar el bluetooth."
        try:
            ArduinoB.__del__()
        except:
            pass

            
    #DECIDE CUANDO DEJAR O QUITAR LOS PROCESOS DEL SCREEN
    def IDENTIFICADOR_P(self, dt):
        #ABRO UN ARCHIVO Y LO ALMACENO EN UNA VARIABLE
        var = open("Datos/SCREEN.text", "r")
        self.lec = var.readline()
        print self.lec
        var.close()
        

        #PERMITE QUE EL SCREEN PERMANEZCA VIVO
        if self.lec == "True\n":
            print "Lectura verdadera desde El escreen de verificacion de llaves"
            pass

        if(self.lec == "False\n"):
            print "Lectura Falsa"
            try:
                self.blueRequest = "Nada"
                self.bufferLectura()
            except:
                pass
            try:                
                #QUITO EL HILO QUE DECIDE CUANDO DEJAR O QUITAR LOS PROCESOS DEL SCREEN
                Clock.unschedule(self.IDENTIFICADOR_P)
            except:
                pass
            try:
                #QUITO EL HILO DE LA FUNCIÓN TIPO RELOJ PARA COLOCAR Y QUITAR LOS AVISOS
                Clock.unschedule(self.Cont1)
            except: 
                pass
            try:
                ArduinoB.__del__()
            except:
                pass
            


class ScreenLogin1(RelativeLayout):
    def build(self):
        return  ScreenLogin()


#if __name__ =="__main__":
 #   ScreenLogin().run()
