#*-*coding:utf-8*-*
# Modulo para eliminar un usuario
# Esto es software libre, licencia GPL3
# Diego Alberto Parra Garzón
# Bogotá D.C., Colombia
#________________________________________________
# Para saber si ya fue eliminada o no la variable
# hay que llamar primero a la función:
#              Asi_Va()
# La cual devuelve 0 "Si no se ha eliminado al usuario"
# o el devuelve el nuid del usuario (NUID) 
#:::::::::::::::::::::::::::::::::::::::::::::::

from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from  kivy.adapters.listadapter import ListAdapter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class ScreenDeleteUser(RelativeLayout):
    '''Implementation of a simple list view with 100 items.
    '''
    def build(self):
        global array
        global list_view
        global bl
        global btn
        bl = RelativeLayout()
        bl.size_hint_y=0.8
        bl.pos = (0,10)
        btn = Button(size_hint_y=0.1, text="Eliminar Usuario", font_size="24 dp")
        btn.bind(on_press=self.acbtn)
        bl.orientation = "vertical"
        
        lbl = Label(text="Seleccione un usuario para eliminar", font_size="24 dp", pos=(20,170))
        
        array = []
        array2 = []
        paso1 = []

        self.asiva = "0"
        self.Asi_Va()
        
        with open("Datos/DataBase.text", "r") as f:
            for line in f:
                array2.append(line)
        for i in range(2, len(array2), 1):
            paso1 = array2[i].split("\n")
            print paso1
            array.append(paso1[0])
            
        list_view = ListView(size_hint_x=1, size_hint_y= 0.6, pos= (0,80))
  #      ListItemButton.selected_color= [0, 0, 1, 1]
   #     ListItemButton.deselected_color= [0, 0, 0, 1]
        list_view.adapter =  ListAdapter(data=array,
                                         selection_mode='single',
                                         cls=ListItemButton)
        bl.add_widget(lbl)        
        bl.add_widget(list_view)
        bl.add_widget(btn)
        return bl

        
    def acbtn(self, *args):
        if (len(list_view.adapter.selection) == 0):
            print "No selected item"
        else:
            btn.bind(on_press=self.acbtn)
            varI = []
            varI = list_view.adapter.selection[0].text.split(",")
            print varI[0]
            self.asiva = varI[0]
            self.Asi_Va()

            
    def Asi_Va(self):
        asiva = self.asiva
        return asiva

#class principal(App):
 #   def build(self):
  #      return ScreenDeleteUser().build()
    
#if __name__ == '__main__':
 #   principal().run()
