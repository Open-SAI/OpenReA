#*-*coding:utf-8 *-*
#qpy:kivy
#python
from jnius import autoclass
from jnius import *
class WifiOpensai:

    def __init__(self):        
        try: 
            #            self.Variables()
            self.ScanRedes()
        except: 
            pass
        


    def ScanRedes(self):
        print "_____------------ 1 ------------------"
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        print "_____------------ 2 ------------------"
        activity = PythonActivity.mActivity
        print "_____------------ 3 ------------------"
        WifiManager = autoclass('android.net.wifi.WifiManager')
        print "_____------------ 4 ------------------"
#        self.WifiName = autoclass('android.net.wifi.WifiInfo')
 #       self.network_name = self.WifiName()
#        self.wifi_service = activity.getSystemService(PythonActivity.WIFI_SERVICE)
     #   self.network = self.wifi_service.getConnectionInfo()
      #  self.networkname = self.network.getBSSID()
        print "_____------------ 5 ------------------"
        wifiList = WifiManager.getScanResults()
        print  wifiList.size()
        print "_____------------ 6 ------------------"
        variables_wifi = []
        print "_____------------ 7 ------------------"
        for i in range (0, wifiList.size(), 1):                
            #                lbl.text = str( wifiList.get(i).toString())
            lst = wifiList.get(i).toString()
            variables_wifi.append(lst)
        
        print "_____------------ 8 ------------------"

        print  variables_wifi[0]
        #            lbl.text =  variables_wifi[0]
        ssid, bssid, hessid, capabilities, level, frecuency, timeStand, distance, distancex = variables_wifi[0].split(",")
        print str(ssid) + " " + str(level)
        return str(ssid)
        #            lbl.text = str(ssid) + str(level)

        

'''
if __name__ == "__main__":
    WifiOpensai().run()
'''
