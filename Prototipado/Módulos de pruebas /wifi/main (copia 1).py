#!/usr/bin/kivy
#qpy:kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
import jnius
from jnius import autoclass

class WifiOpensai(App):

    def build(self):        
        wg = Widget()
        lbl= Label(pos=(100,100), font_size="10sp", markup=True)
        wg.add_widget(lbl)
        print "-----------------------1----------------------------"
        PythonActivity = jnius.autoclass('org.renpy.android.PythonActivity')
        print "-----------------------2----------------------------"
        activity = PythonActivity.mActivity
        print "-----------------------3----------------------------"
        WifiManager = jnius.autoclass('android.net.wifi.WifiManager')
        print "-----------------------4----------------------------"
        WifiName= jnius.autoclass('android.net.wifi.WifiInfo')
        print "-----------------------5----------------------------"
        network_name = WifiName()
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
        for i in range (0, wifiList.size(), 1):
            lbl.text = str( wifiList.get(i).toString())
            lst = wifiList.get(i).toString()
            variables_wifi.append(lst)
        
        print  variables_wifi[0]
        lbl.text =  variables_wifi[0]
        ssid, bssid, hessid, capabilities, level, frecuency, timeStand, distance, distancex = variables_wifi[0].split(",")
        lbl.text = str(ssid) + str(level)
        return wg

if __name__ == "__main__":
    WifiOpensai().run()
