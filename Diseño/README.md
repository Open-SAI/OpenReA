## DISEÑO PROTOTIPO
### Documento de diseño con la arquitectura e información utilizada asociada a la especificación del prototipo

* Integración API navegación/posicionamiento bajo techo

[![Indoor NAV](http://img.youtube.com/vi/puzDdvE8Y-0/0.jpg)](http://www.youtube.com/watch?v=puzDdvE8Y-0)

* Arquitectura general del sistema.
  * Componentes de la aplicación.
    * WifiList: 
      * Tipo: Módulo.
      * Funcionalidad: Escaneo de las redes disponibles, con SSID y BSSID.
      * Precondiciones:  Habilitado el WIFI.
      * Recibe: Ningún parámetro.
      * Entrega: Array de redes disponibles incluyendo el SSID y BSSID, para cada item de la lista.      
    * WifiSelect:
      * Tipo: Screen
      * Funcionalidad: Permitir al usuario seleccionar las redes que dispone para el posicionamiento en el espacio seleccionado.
      * Precondicciones: Depende de WifiList
      * Recibe: El array generado por el módulo WifiList.
      * Entrega: Crea o actualiza el archivo MACseleccionadas.dat      
    * WifiListLiveScan: 
      * Tipo: Módulo
      * Funcionalidad: Leer la intensidad de cada una de las redes configuradas por el usuario.
      * Precondicciones: listado de MAC de las redes guardadas en el archivo MACseleccionadas.dat
      * Recibe: Ninguno
      * Entrega: Array con la MAC de cada una de las redes y la Intensidad de la señal de cada una de ellas.      
    * LecMACalibra:
      * Tipo: Screen
        * Screen1:
          * Funcionalidad: 
            * Listar Redes Seleccionadas
            * Selecccionar una de las redes para su calibración
            * Llamar Screen2
          * Diseño: 
            * Label:
              * Texto: Calibración de redes.
            * ScrollView: Contenedor que muestra las redes seleccionadas por el usuario para la aplicación.
            * SelectView: Selecciona una de las redes del ScrollView para adquirir los datos para su posterior calibración.
            * Button: Llama al Screen2, para adquiera los datos para su calibración de la red selecionada en el SelectView.           * Screen2:
          * Funcionalidad: 
          * Precondicciones:
          * Recibe:
          * Entrega:                  
        * Screen3:
          * Funcionalidad 
          * Precondicciones:
          * Recibe:
          * Entrega:                  
      * Funcionalidad: Permite que el administrador de la aplicación realice una lectura de los datos de calibración (Distancia, Intensidad) para el cálculo de la constante de intensidad de cada una de las señales de las redes configuradas para la aplicación (MACseleccionadas.dat).
      * Precondicciones: listado de MAC de las redes guardadas en el archivo MACseleccionadas.dat
      * Recibe: Ningún
      * Entrega: Un archivo con los datos para la calibración (Distancia, intensidad) para cada red; el nombre del archivo queda con el BSSID.dat.      
    * MACalibra
      * Tipo: 
      * Funcionalidad 
      * Precondicciones:
      * Recibe:
      * Entrega:
  * ArchivosDeDatos
    * MACseleccionadas.dat:
    * CTEintensidadMACseleccionadas.dat
