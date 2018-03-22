# Aplicación que permite al usuario autenticarse en la aplicación de apoyo logístico.

<img src="https://github.com/Open-SAI/ReA/blob/master/Dise%C3%B1o/Dispositivo%20de%20autenticaci%C3%B3n/APP-LOGIN/Documentos/ImagenesAPP/Screenshot_2018-03-05-17-23-20.png">

<img src="https://github.com/Open-SAI/ReA/blob/master/Dise%C3%B1o/Dispositivo%20de%20autenticaci%C3%B3n/APP-LOGIN/Documentos/ImagenesAPP/20180315_180434.jpg" width="600" heigth="1000">

# Logíca de funcionamiento
* Funciones:
  * Paso 1: Conectar con el dispositivo bluetooth
  * Paso 2: Enviar comando para que el hardware comience la lectura RFID
  * Paso 3: Lectura de los datos enviados por el hardware.
  * Paso 4: Si el dato coincide con el el número de referencia del usuario, generararchivo de bloque de autenticacción.  Notifique por pantalla y finalice aplicación.
  * Paso 5: Si el dato no coincide con el número de referencia del usuario, enviar un notificación en el screen de usuario no valido, y volver al paso 3.

  
### Test de la App
El test se realizo con Telenium y se prueba el funcionamiento total de la App
<img src="https://github.com/Open-SAI/ReA/blob/master/Dise%C3%B1o/Dispositivo%20de%20autenticaci%C3%B3n/APP-LOGIN/Documentos/Testeos/imagenesTest/test0.png">
<img src="https://github.com/Open-SAI/ReA/blob/master/Dise%C3%B1o/Dispositivo%20de%20autenticaci%C3%B3n/APP-LOGIN/Documentos/Testeos/imagenesTest/test1.png">
<img src="https://github.com/Open-SAI/ReA/blob/master/Dise%C3%B1o/Dispositivo%20de%20autenticaci%C3%B3n/APP-LOGIN/Documentos/Testeos/imagenesTest/test2.png">
<img src="https://github.com/Open-SAI/ReA/blob/master/Dise%C3%B1o/Dispositivo%20de%20autenticaci%C3%B3n/APP-LOGIN/Documentos/Testeos/imagenesTest/test3.png">
