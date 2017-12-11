<!DOCTYPE html>
<html>
<head>
<title>formulario</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</head>

<body>

<?php
	$Lat = "3";
	$Lon = "3";
	$Tem = "3";
	$VelT = "3";
	

    header ("Location: http://10.42.0.1/BD/GPS/InsertarGPS.php?Latitud=$Lat&Longitud=$Lon&Temperatura=$Tem&Velocidad=$VelT");
?>



</body>


</html>