import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout


class ScrollViewApp(App):

    def build(self):
        global btn
        global layout
        global root
        global lbl
        global rl
        global btn1
        global array

        array = []
        array2 = []
        paso1 = []
        with open("Datos/DataBase.text", "r") as f:
            for line in f:
                array2.append(line)
        for i in range(2, len(array2)-1, 1):
            paso1 = array2[i].split("\n")
            print paso1
            array.append(paso1[0])


        rl = RelativeLayout(size_hint_y=1)
                
        btn1 = Button(text="Eliminar usuario", size_hint=(1, 0.1), id="eiminar", font_size=26,  pos_hint={'center_x': .5, 'center_y': .1})
        
        
        # create a default grid layout with custom width/height
        layout = GridLayout(cols=1, padding=10, spacing=20,
                size_hint=(None, None), width=500)
        
        lbl = Label(text="[color=ff3333] Seleccione un usuario para eliminar:", pos_hint={'center_x': .5, 'center_y': .85},  font_size="30 dp", markup=True)

        layout.bind(minimum_height=layout.setter('height'))
        
        # add button into that grid
        for i in range(0, len(array), 1):
            layout.add_widget(Button(text=str(array[i]), size=(480, 40), size_hint=(None, None), id=str(i), on_press=self.acbtn, font_size=18))
#            print btn.id
   #         btn.bind(on_press=self.acbtn)
            
        # create a scroll view, with a size < size of the grid
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                          pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)


        
        root.add_widget(layout)
        rl.add_widget(btn1)
        rl.add_widget(root)
        rl.add_widget(lbl)
        return rl

    def acbtn(self, *args):
#        for i in args:
 #           print i
        lss=[]
        ls1 =[]
        cm = str(args[0:1])
        lss = cm.split(" ")
        ls1 = lss[3].split(">")
        print ls1[0]
        print type(args)
        chn = []
        cn = str(layout.children)
        chn = cn.split(", ")
        print len(chn)
        posicion = ""
        for i in range(0, len(chn), 1):
            ulss=[]
            uls1 =[]
            ucm = str(chn[i])
            ulss = ucm.split(" ")
            uls1 = ulss[3].split(">")
 #           print uls1[0]
            if (str(ls1[0]) == str(uls1[0])):
                #                print "item: " + str(i) 
                posicion = len(chn) - i
                
        print "Esta en la posicion: "+ str(posicion)
        print "la fruta es: " + array[posicion-1]
        mensaje = "Ha pulsado: " +"[color=ff3333] " +  array[posicion-1]
        lbl.text = mensaje
        pass
    
if __name__ == '__main__':
    ScrollViewApp().run()
