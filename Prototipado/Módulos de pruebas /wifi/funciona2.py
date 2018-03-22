#*-*coding:utf-8*-*
#qpy:kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from jnius import autoclass, cast

class WifiOpensai(App):

    def build(self):        
        wg = Widget()
        lbl= Label(pos=(300,100), font_size="22sp", markup=True)
        wg.add_widget(lbl)
        print "-----------------------1----------------------------"
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        print "-----------------------2----------------------------"
        activity = PythonActivity.mActivity
        print "-----------------------3----------------------------"
        WifiManager = autoclass('android.net.wifi.WifiManager')
        print "-----------------------4----------------------------"
        WifiName= autoclass('android.net.wifi.WifiInfo')
        print "-----------------------5----------------------------"
        network_name = WifiName
        print "-----------------------6----------------------------"
        wifi_service = activity.getSystemService(PythonActivity.WIFI_SERVICE)
        print "-----------------------7----------------------------"
        network= wifi_service.getConnectionInfo()
        print "-----------------------8----------------------------"
        network_name = network.getBSSID()
        print "-----------------------9----------------------------"
        wifiList = WifiManager.getScanResults()
        print "-----------------------10----------------------------"
        lbl.text = "Hola mundo"
        print "-----------------------11----------------------------"
        variables_wifi = []
        print "-----------------------12----------------------------"

        for i in range (0, wifiList.size(), 1):
            print "-----------------------13----------------------------"
            lbl.text = str( wifiList.get(i).toString())
            print "-----------------------14----------------------------"
            lst = wifiList.get(i).toString()
            print "-----------------------15----------------------------"
            variables_wifi.append(lst)
            print "-----------------------16----------------------------"
            
        try:
            opcion = False
            i = 0
            while(opcion == False):
                print  variables_wifi[i]        
                tor = str(variables_wifi[i])
                print "-----------------------17----------------------------"
                lbl.text =  str(variables_wifi[i])
                print "-----------------------18----------------------------"
                lol = []
                lol = tor.split(',')
                print "-----------------------18A----------------------------"
                print lol
                print "-----------------------19----------------------------"
                lolo = []
                lolo = lol[0].split(' ')
                SSID = lolo[1]
                if (SSID == '56995517'):
                    print "Red_Wifi_detectada:  "+ str(SSID)
                    lolo = []
                    lolo = lol[3].split(' ')
                    Intensidad = lolo[2]
                    print "Intensidad_Red_Wifi_detectada:  "+ str(Intensidad)
                    lbl.text = "Red_Wifi_detectada: " + str(SSID) + "\n" +  "Intensidad_Red_Wifi_detectada:  " + str(Intensidad)
                
                    print "-----------------------20 ----------------------------"
                    opcion = True
                i = i+1
        except:
            print "-----------------------21 ----------------------------"
            lbl.text =  str(variables_wifi[0]) +  "\nFallo el split"
        return wg


if __name__ == "__main__":
    WifiOpensai().run()
