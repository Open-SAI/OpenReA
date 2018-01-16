<!DOCTYPE HTML>
<html>
<head>
<title>Registro GPS</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</head><meta http-equiv="refresh" content="3">
<center>
<table><tr><td>
<HR SIZE=5 WIDTH=100% HEIGTH= 70%><img src="http://10.42.0.1/Imagenes/opensaiLOGO.png" width="294" height="185">
<HR SIZE=5 WIDTH=100% HEIGTH= 70%></td><td>
<HR SIZE=5 WIDTH=100% HEIGTH= 70%><img src="http://10.42.0.1/Imagenes/contenido.png" width="868" height="68" alt=" "> 
<HR SIZE=5 WIDTH=100% HEIGTH= 70%></td></tr></table>
</center> 

<body>

<body background="http://10.42.0.1/Imagenes/log3.png"> 
<body bgcolor='#8bb0ed'>
<h1>OPENSAI</h1>
<h2>ESP8266, NEO 6M y LM35.  GPS, Termometro, WIFI</h2>
<h4> Latitud: Latitud &ordm <br>
Longitud:  Longitud &ordm <br>
Temperatura:  Temperatura &ordm <br> 
Tiempo Proc.:  VeTrans  ms</h4>
<h4>Diego Parra<br>Bogot&aacute, Colombia.</h4>


<?php
$host = "localhost";
$user = "root"; 
$pw	=  "DiosPerdoname@"; 
$db	= "Registro";
$Lat  = "123" ;
$Lon  = "234" ;
$Tem  =  "23";
$VelT  = "32";

if(	isset ($Lat) && !empty($Lat) && 
		isset ($Lon) && !empty($Lon) && 
		isset ($Tem) && !empty($Tem) && 
		isset ($VelT) && !empty($VelT))
{ 
	$con = mysql_connect($host, $user, $pw) or die ("Problemas al conectar"); 
	mysql_select_db($db, $con) or die ("Problemas al conectar la DB");
	mysql_query("INSERT INTO GEODATA (Latitud, Longitud, Temperatura, Velocidad) VALUES ('$Lat','$Lon', '$Tem', '$VelT')", $con);
	echo "datos insertados";
} 
else 
{ 
	echo "Problemas al insertar datos";
} 
?>

</body>
</html>
