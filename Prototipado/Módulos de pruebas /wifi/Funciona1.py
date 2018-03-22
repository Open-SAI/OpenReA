#!/usr/bin/kivy
#*-*coding:utf-8*-*
#qpy:kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from jnius import autoclass, cast

class WifiOpensai(App):

    def build(self):        
        wg = Widget()
        lbl= Label(pos=(200,100), font_size="10sp", markup=True)
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

        
        print  variables_wifi[0]
        tor = str(variables_wifi[0])
        print "-----------------------17----------------------------"
        lbl.text =  str(variables_wifi[0])
        print "-----------------------18----------------------------"
        try:
            lol = []
            lol = tor.split(',')
#            ssid, bssid, hessid, capabilities, level, frecuency = tor.split(',')
            print "-----------------------19----------------------------"
            lbl.text = str(lol[0]) + str(lol[3])
            print "-----------------------20 ----------------------------"
        except:
            lbl.text =  str(variables_wifi[0]) +  "\nFallo el split"
        return wg

if __name__ == "__main__":
    WifiOpensai().run()
