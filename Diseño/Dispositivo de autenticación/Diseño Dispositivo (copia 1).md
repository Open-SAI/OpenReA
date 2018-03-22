Aplicación que permite al usuario autenticarse en la aplicación de apoyo logístico.
#h1 Logíca de funcionamiento
* Funciones:
  * Paso 1: Conectar con el dispositivo bluetooth
  * Paso 2: Enviar comando para que el hardware comience la lectura RFID
  * Paso 3: Lectura de los datos enviados por el hardware.
  * Paso 4: Si el dato coincide con el el número de referencia del usuario, generararchivo de bloque de autenticacción.  Notifique por pantalla y finalice aplicación.
  * Paso 5: Si el dato no coincide con el número de referencia del usuario, enviar un notificación en el screen de usuario no valido, y volver al paso 3.
  

