# *-*coding:utf-8 *-*
#qpy:kivy
#import sys
#sys.path.append('Datos')
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import ActionBar, ActionView, ActionButton, ActionPrevious, ActionGroup
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from Screen1 import ScreenLogin1
from comUSER import CompararUsuario
from kivy.clock import Clock
from FileAgregarUser import ScreenAgregarUser
from kivy.uix.label import Label
from FileDeleteUser import ScreenDeleteUser
from kivy.uix.button import Button

class LoginApp(App):
    # Definiendo las variables globales, 
    global BarAc
    global AcView
    global AcPre
    global AcGroup
    global AcBtn1
    global AcBtn2
    global AcBtn3
    global screenLogin1
    global rl
    global rl1
    global rl2
    global rl3
    global rl4
    global rlPaso
    global compara
    global addUSER
    global deleteUSER
    global lblAlerta
    global textIN
    global textINpass
    global btnCambiarpass


    # Deginiendo el layout principal
    rl = RelativeLayout()
    rl1 = RelativeLayout(size_hint_y=0.8, size_hint_x=1, pos=(-80,20))
    rl2 = RelativeLayout(size_hint_y=0.7, size_hint_x=1, pos=(0,20))
    rl3 = RelativeLayout(size_hint_y=1, size_hint_x=1, pos=(0,20))
    rl4 = RelativeLayout()

    rlPaso = RelativeLayout(size_hint_y=0.7, size_hint_x=0.7, pos=(150,250))
    AcBtn1 = ActionButton(text="Añadir Usuario.")
    AcBtn2 = ActionButton(text="Quitar Usuario.")
    AcBtn3 = ActionButton(text="Cambiar Contraseña")
    
    BarAc = ActionBar(pos_hint={'top':1})
    AcView = ActionView()    
    AcPre = ActionPrevious(title= '   APP DE LOGIN LooginTooth ', important= True,with_previous= False )
    AcGroup = ActionGroup(text='Configuraciones', mode= 'spinner', size_hint_x= None, width= 90)
    screenLogin1 = ScreenLogin1()
    compara = CompararUsuario()
    addUSER = ScreenAgregarUser()
    deleteUSER = ScreenDeleteUser()
    
    lblAlerta = Label( pos_hint={'center_x': .7, 'center_y': .25}, text="", font_size="20dp", markup=True)

# ________________ defino los textInput    
    textIN = TextInput(size_hint_y=0.2, size_hint_x=0.7, pos_hint={'center_x': .45, 'center_y': .25}, font_size="20dp", multiline=False)
    textINpass = TextInput(size_hint_y=0.2, size_hint_x=0.5, pos_hint={'center_x': .45, 'center_y': .65}, font_size="20dp", multiline=False)

    btnCambiarpass = Button(text="Cambiar \n Contraseña", pos_hint={'center_x': .85, 'center_y': .65}, size_hint_y=0.2, size_hint_x=0.2,font_size=20 )
    
    def build(self):
        self.UsuarioROOT = 0
        #Añadir widget y funciones al action view
        AcView.add_widget(AcPre)
        AcView.use_separator=True
        AcView.add_widget(AcGroup)

        #Añadir las funcionalidades de los botones
        #     Añadir los botones al action group
        AcGroup.add_widget(AcBtn1)
        AcGroup.add_widget(AcBtn2)
        AcGroup.add_widget(AcBtn3) 


        
        #Añadir el action view al action bar
        BarAc.add_widget(AcView)

        # iniciando el screen de login    
        rl.add_widget(BarAc)
        rl.add_widget(lblAlerta)
        
        #Añadiendo los layouts de las librerias al layout principal
        rl.add_widget(rl1)
        rl.add_widget(rl2)
        rl.add_widget(rl3)
        rl.add_widget(rl4)        


        AcGroup.bind(on_press=self.identifiquese)
        self.cuenta = 0
        self.AgregarScreenComparar()
        return rl

    def identifiquese(self, *args):
        global soyROOT
        print "Hola me llamaste para identificar el nuevo ingreso"
        try:
            AcGroup.unbind(on_press=self.identifiquese)
        except:
            pass

        AcPre.title= "Regresar al inicio"
        try:
            AcPre.unbind(on_press=self.acPre1)
        except:
            pass
        try:
            AcPre.bind(on_press=self.acPre1)
        except:
            pass
        
        if self.UsuarioROOT == 0 :
            rl1.pos=(-1000, 0)
            #añado un layout de paso
            rl.add_widget(rlPaso)
            rlPaso.add_widget(textIN)
            textIN.text=""
            Mensaje = "Ingrese su clave administrador"
            lblAlerta.pos = (0, 0)
            lblAlerta.pos_hint={'center_x': .5, 'center_y': .5}
            lblAlerta.text = Mensaje
            var = open("Datos/pass.text","r")
            soyROOT = var.read()
            var.close()
            soyroot = soyROOT.split("\n")
            print soyroot[0]
            soyROOT = soyroot[0] 
            Clock.schedule_interval(self.quienERES, 0.2)
            
        if self.UsuarioROOT == 1:
            AcBtn1.bind(on_press=self.acAcBtn1)            
            AcBtn2.bind(on_press=self.acAcBtn2)
            self.UsuarioROOT = 2

        if self.UsuarioROOT == 2:
            pass


            
    def quienERES(self, dt):
        print textIN.text
        if (str(textIN.text) == (soyROOT)):
            Clock.unschedule(self.quienERES)
            self.UsuarioROOT = 1
            self.valorsleep = 0
            Mensaje = "bienvenido usuario root, espere un momento"
            lblAlerta.pos_hint={'center_x': .5, 'center_y': .5}
            lblAlerta.text = Mensaje
            Clock.schedule_interval(self.timeSleep, 1)

    def AgregarScreenComparar(self):        
        global SL
        global sl
        global comp
        global cp1
#        Clock.unschedule(self.ScreenComparar)
        #añadiendo el screen1 al relative layout
        var = open("Datos/SCREEN.text", "w")
        var.write("True\n")
        var.close()
        SL = screenLogin1.build()
        sl = SL.build()
        rl1.add_widget(sl)
       
        #iniciando la clase de comparación y añadiendola al layout principal
        comp = compara.build()
        rl1.add_widget(comp)
        Clock.schedule_interval(self.EsperarIdentificacion, 0.45)
        

    def AgregarScreenAddUsser(self):
        global addUser
        addUser = addUSER.build()
        rl1.size_hint_y = 0.6
        rl1.size_hint_x=0.6
        rl1.pos=(-10,100)
        Clock.schedule_interval(self.EsperarIdentificacion1, 0.45)

        
    def AgregarScreenDeleteUsser(self):
        global deleteUser
        deleteUser = deleteUSER.build()
        rl1.size_hint_y = 0.6
        rl1.size_hint_x=0.6
        rl1.pos=(-1500,100)
        rl3.add_widget(deleteUser)
        Clock.schedule_interval(self.EsperarIdentificacion2, 0.5)

    def AgregarScreenCambiarPass(self):
        print "Me llamaste para cambiar contrasenhas"
        rl1.pos=(-1000, 0)
        rl4.add_widget(btnCambiarpass)
        rl4.add_widget(textINpass)
        textINpass.text = ""
        Mensaje = "Ingrese su nueva contraseña."
        lblAlerta.pos_hint={'center_x': .45, 'center_y': .5}
        lblAlerta.text = Mensaje
        btnCambiarpass.bind(on_press=self.cambiarpass)
        pass


    def cambiarpass(self, *args):
        if (len(textINpass.text) >= 4):
            btnCambiarpass.unbind(on_press=self.cambiarpass)
            var = open("Datos/pass.text", "w")
            var.write(textINpass.text)
            var.close()
            self.valorsleep = 0
            Mensaje = "Su contraseña de root ha sido actuailizada."
            lblAlerta.pos_hint={'center_x': .45, 'center_y': .5}
            lblAlerta.text = Mensaje
            Clock.schedule_interval(self.timeSleep, 1)
            
        if (len(textINpass.text) < 4):
            Mensaje = "Ingrese su nueva contraseña.\n La contraseña no puede ser tan corta."
            lblAlerta.pos_hint={'center_x': .45, 'center_y': .5}
            lblAlerta.text = Mensaje
            
# ----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#                              quitar screens
#

    def QuitarScreenComparar(self):
        try:
            Clock.unschedule(self.EsperarIdentificacion)
        except:
            pass

        try:
            Clock.unschedule(self.EsperarComparacion)
        except:
            pass
        

    def QuitarScreenAddUsser(self):
        self.QuitarScreenComparar()
        try:
            Clock.unschedule(self.EsperarIdentificacion1)
        except:
            pass

        try:
            Clock.unschedule(self.EsperarComparacion1)
        except:
            pass

        try:
            Clock.unschedule(self.PreguntarFormulario)
        except:
            pass

        try:
            rl2.clear_widgets()
        except:
            pass


# ----------------------------------------------------------------------------
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
#---------------------------------------Controla EL SCREEN DE QUITAR USUARIO
    def EsperarIdentificacion2(self, dt):
        print ">>>>>>>>>>>>>>>>>>> otro puto problema <<<<<<<<<<<<<<<<<<<<<<<<<" + str(deleteUSER.Asi_Va())
        if (str(deleteUSER.Asi_Va()) != "0"):
            Clock.unschedule(self.EsperarIdentificacion2)
            compara.CompararArray(str(deleteUSER.Asi_Va()))
            Clock.schedule_interval(self.EsperarComparacion2, 0.3)

    def EsperarComparacion2(self, dt):        
        estado = compara.estadoCom()
        print "este es el estado del coroto " + str(estado)
        if estado != 2:
            Clock.unschedule(self.EsperarComparacion2)
            self.valorsleep = 0
            Clock.schedule_interval(self.timeSleep, 1)

            pass
        
        if estado == 2:
            print "Se encontro coincidencia deteniendo el hilo"
            Clock.unschedule(self.EsperarComparacion2)
            compara.quitarUsuario()
            self.valorsleep = 0
            Clock.schedule_interval(self.timeSleep, 1)
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

         
        
#-------------------------------------------------------------------------------------
# ----------------------------- controla EL SCREEN DE AGREGAR USUARIO --------------------
    def EsperarIdentificacion1(self, dt):
        if (str(SL.bufferLectura()) != "Nada"):
            Clock.unschedule(self.EsperarIdentificacion1)
            compara.CompararArray(str(SL.bufferLectura()))
            Clock.schedule_interval(self.EsperarComparacion1, 0.1)

    def EsperarComparacion1(self, dt):        
        estado = compara.estadoCom()
        print "este es el estado del coroto " + str(estado)
        if estado == 1:
            pass
        
        if estado == 2:
            print "Se encontro coincidencia deteniendo el hilo"
            Clock.unschedule(self.EsperarComparacion1)
            Mensaje = " El usuario ya existe \n en el registro de la B.D."
            lblAlerta.pos_hint={'center_x': .75, 'center_y': .5}
            lblAlerta.text= Mensaje
            self.valorsleep = 0
            Clock.schedule_interval(self.timeSleep, 1)


        if estado == 3:
            print "No Se encontro coincidencia deteniendo el hilo"
            Clock.unschedule(self.EsperarComparacion1)
            rl2.add_widget(addUser)
            rl2.add_widget(rlPaso)
            Clock.schedule_interval(self.PreguntarFormulario, 0.4)
            
    def PreguntarFormulario(self, dt):
        valores = []
        valores = addUSER.Como_va_la_cosa()
        if(valores[1] != "nada"):
           Clock.unschedule(self.PreguntarFormulario)
           compara.agregarUsuario(str(SL.bufferLectura()), valores[0], valores[1])
           Mensaje = "    Usuario  agregado al \n    registro."
           lblAlerta.pos_hint={'center_x': .75, 'center_y': .5}
           lblAlerta.text= Mensaje
           self.valorsleep = 0
           Clock.schedule_interval(self.timeSleep, 1)             
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
            
            
#-------------------------------------------------------------------------------------
# ----------------------------- controla EL SCREEN DE LOGIN ------------------------------
    def EsperarIdentificacion(self, dt):
        if (str(SL.bufferLectura()) != "Nada"):
            Clock.unschedule(self.EsperarIdentificacion)
            compara.CompararArray(str(SL.bufferLectura()))
            Clock.schedule_interval(self.EsperarComparacion, 0.1)
            
    def EsperarComparacion(self, dt):        
        estado = compara.estadoCom()
        print "este es el estado del coroto " + str(estado)
        if estado == 1:
            
            pass
        
        if estado == 2:
            print "Se encontro coincidencia deteniendo el hilo"
            Clock.unschedule(self.EsperarComparacion)
            self.ClaveEncontrada()

        if estado == 3:
            print "No Se encontro coincidencia deteniendo el hilo"
            Clock.unschedule(self.EsperarComparacion)
            SL.ReiniciarLectura()
            Clock.schedule_interval(self.EsperarIdentificacion, 0.1)
              
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
#-------------------Defino la función clave encontrada

    def ClaveEncontrada(self):
        self.timexit = 0
        try:
            from jnius import autoclass
            import time 
            Env = autoclass('android.os.Environment')
            env = Env
            infoTIME = str(time.strftime("%c"))
            msj1 = str(SL.bufferLectura()) + " "+ infoTIME + "\n"
            print "======================================================="
            print "======================================================="
            print "======================================================="
            print "======================================================="
            print "======================================================="
            print 
            svar = "../../../../../storage/sdcard0/"+env.DIRECTORY_DOWNLOADS + "/LoginApp.text"
            sd = open(svar, "w")
            sd.write("True")
            sd.close()
            svar2 = "../../../../../storage/sdcard0/"+env.DIRECTORY_DOWNLOADS + "/infoLoginApp.text"
            sd1 = open(svar2, "a")
            sd1.write(msj1)
            sd.close()
            print "======================================================="
            print "======================================================="
            print "======================================================="
            print "======================================================="
            print "======================================================="
            Clock.schedule_interval(self.timeExit, 1)
            rl1.pos=(-1000, 0)
            textINpass.text = ""
            Mensaje = "Usuario aceptado, cerrando la App.\n Espere por favor ..."
            lblAlerta.pos_hint={'center_x': .45, 'center_y': .5}
            lblAlerta.text = Mensaje

        except:
            rl1.pos=(-1000, 0)
            textINpass.text = ""
            Mensaje = " Usuario aceptado, cerrando la App. \n Espere por favor ..."
            lblAlerta.pos_hint={'center_x': .45, 'center_y': .5}
            lblAlerta.text = Mensaje
            Clock.schedule_interval(self.timeExit, 1)
#            LoginApp().exit()

            #                print env.DIRECTORY_DOWNLOADS
            pass

    def timeExit(self, dt):      
        if self.timexit == 4:
            LoginApp().get_running_app().stop()
        else:
            self.timexit = self.timexit  + 1

#------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
#------------------------ FUNCIÓN DORMIR, quita todos los procesos y vuelve al login--
    def timeSleep(self, dt):
        if self.valorsleep == 1:
            Clock.unschedule(self.timeSleep)
            try:
                AcGroup.bind(on_press=self.identifiquese)
            except:
                pass

            try:
                Clock.unschedule(self.quienERES)
            except:
                pass
            try:
                rlPaso.clear_widgets()
            except:
                pass
            try:
                rl.remove_widget(rlPaso)
            except:
                pass
            try:
                Clock.unschedule(self.EsperarIdentificacion)
            except:
                pass
            try:
                Clock.unschedule(self.EsperarComparacion)
            except:
                pass
            try:
                Clock.unschedule(self.EsperarIdentificacion1)
            except:
                pass
            try:
                Clock.unschedule(self.EsperarComparacion1)
            except:
                pass
            
            try:
                Clock.unschedule(self.EsperarIdentificacion2)
            except:
                pass
            try:
                Clock.unschedule(self.EsperarComparacion2)
            except:
                pass
            try:
                Clock.unschedule(self.PreguntarFormulario)
            except:
                pass

            try:
                rl3.clear_widgets()
            except:
                pass
            try:
                rl2.clear_widgets()
            except:
                pass

            try:
                rl4.clear_widgets()
            except:
                pass
            try:
                btnCambiarpass.unbind(on_press=self.cambiarpass)
            except:
                pass
            Mensaje = ""
            lblAlerta.pos  = (180, 0)
            lblAlerta.text= Mensaje
            rl1.size_hint_y = 0.8
            rl1.size_hint_x=  1
            rl1.pos=(-80,20)
            AcBtn1.bind(on_press=self.acAcBtn1)
            AcBtn2.bind(on_press=self.acAcBtn2)
            AcBtn3.bind(on_press=self.acAcBtn3)
            SL.ReiniciarLectura()
            compara.CargarArray()
            AcPre.title= '   APP DE LOGIN LooginTooth '
            Clock.schedule_interval(self.EsperarIdentificacion, 0.45)
            
        if self.valorsleep < 1:
            print ">>>>>>>>>>>>>>>>> Durmiendo <<<<<<<<<<<<<<<<<<<<<<"
            self.valorsleep = self.valorsleep + 1
            pass
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------        


#-------------------------------------------------------------------------------------
#-------------------------- BOTONES DEL ACTION VIEW ----------------------------------
    def acPre1(self, *args):
        print "Llamado 1"
        print SL.bufferLectura()
        self.valorsleep = 0
        Clock.schedule_interval(self.timeSleep, 1)
        AcPre.unbind(on_press=self.acPre1)
        AcPre.bind(on_press=self.acPre2)


    def acPre2(self, *args):
        print "Llamado 2"
        AcPre.unbind(on_press=self.acPre2)
#        AcPre.bind(on_release=self.acPre1)


#---------------------------- Botón para agregar usuario --------------------------------                
    def acAcBtn1(self, *args):
        print "iniciando el screen de actualizar usuario"
        self.QuitarScreenComparar()
        self.AgregarScreenAddUsser()
        AcPre.title= "Regresar al inicio"
        #Añafir una acción a la imgen de ir al widget actionprenious
        try:
            AcPre.unbind(on_press=self.acPre1)
        except:
            pass
        try:
            AcPre.bind(on_press=self.acPre1)
        except:
            pass
        AcBtn1.unbind(on_press=self.acAcBtn1)
        AcBtn2.unbind(on_press=self.acAcBtn2)
        AcBtn3.unbind(on_press=self.acAcBtn3)

        pass

#----------------------------Botón para quitar usuario -----------------------------------    

    def acAcBtn2(self, *args):
        print "iniciando el screen de quitar usuario"
        self.QuitarScreenAddUsser()
        self.AgregarScreenDeleteUsser()
        AcPre.title= "Regresar al inicio"
        try:
            AcPre.unbind(on_press=self.acPre1)
        except:
            pass
        try:
            AcPre.bind(on_press=self.acPre1)
        except:
            pass
        AcBtn1.unbind(on_press=self.acAcBtn1)
        AcBtn2.unbind(on_press=self.acAcBtn2)
        AcBtn3.unbind(on_press=self.acAcBtn3)

        pass

#---------------------------- Botón para cambiar contraseña --------------------------------                
    def acAcBtn3(self, *args):
        print "iniciando el screen de actualizar usuario"
        self.QuitarScreenComparar()
        self.AgregarScreenCambiarPass()
        AcPre.title= "Regresar al inicio"
        #Añafir una acción a la imgen de ir al widget actionprenious
        try:
            AcPre.unbind(on_press=self.acPre1)
        except:
            pass
        try:
            AcPre.bind(on_press=self.acPre1)
        except:
            pass
        AcBtn1.unbind(on_press=self.acAcBtn1)
        AcBtn2.unbind(on_press=self.acAcBtn2)
        AcBtn3.unbind(on_press=self.acAcBtn3)

        pass
        
if __name__ =="__main__":
    LoginApp().run()
