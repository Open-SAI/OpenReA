#*-*coding:utf-8 *-*
#qpy:kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
import jnius

class WifiOpensai(App):

    def build(self):        
        wg = Widget()
        lbl= Label(pos=(100,100), font_size="10sp", markup=True)
        wg.add_widget(lbl)
        PythonActivity = jnius.autoclass('org.renpy.android.PythonActivity')
        activity = PythonActivity.mActivity
        WifiManager = jnius.autoclass('android.net.wifi.WifiManager')
        WifiName= jnius.autoclass('android.net.wifi.WifiInfo')
        network_name = WifiName()
        wifi_service = activity.getSystemService(PythonActivity.WIFI_SERVICE)
        network= wifi_service.getConnectionInfo()
        network_name = network.getBSSID()
        wifiList = WifiManager.getScanResults()
        lbl.text = "Hola mundo"
        try:
            variables_wifi = []
            for i in range (0, wifiList.size(), 1):
                lbl.text = str( wifiList.get(i).toString())
                lst = wifiList.get(i).toString()
                variables_wifi.append(lst)
        
            print  variables_wifi[0]
            lbl.text =  variables_wifi[0]
            ssid, bssid, hessid, capabilities, level, frecuency, timeStand, distance, distancex = variables_wifi[0].split(",")
            lbl.text = str(ssid) + str(level)
        except:
            pass
        return wg

'''
if __name__ == "__main__":
    WifiOpensai().run()
'''
