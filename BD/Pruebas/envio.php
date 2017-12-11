<!DOCTYPE html>
<html>
<head>
<title>formulario</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="refresh" content="3">
</head>
<body>	
<?php

$host = "localhost";
$user = "root";
$pw	=  "DiosPerdoname@";  
$db	= "Registro";
$Lat  = "234";
$Lon  = "2345"; 
$Tem  =  "23";
$VelT  = "123";


if(isset ($Lat) && !empty($Lat) && 
	isset ($Lon) && !empty($Lon) &&
	isset ($Tem) && !empty($Tem) &&
	isset ($VelT) && !empty($VelT) )
	{
		$con = mysql_connect($host, $user, $pw) or die ("Problemas al conectar");
		mysql_select_db($db, $con) or die ("Problemas al conectar la DB");
		mysql_query("INSERT INTO GEODATA (Latitud, Longitud, Temperatura, Velocidad) VALUES ('$Lat','$Lon', '$Tem', '$VelT')", $con);
		echo "datos insertados";
		}
	else {
		echo "Problemas al insertar datos";
	}

?>
</body>
</html>