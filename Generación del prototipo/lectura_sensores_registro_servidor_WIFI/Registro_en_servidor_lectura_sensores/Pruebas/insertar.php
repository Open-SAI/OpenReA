<!DOCTYPE html>
<html>
<head>
<title>Registro BD</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="Refresh" content="5;url=http://localhost/BD/form.php">	 
</head>
<?php
//include("conexion.php");
$host = "localhost";
$user = "root";
$pw	=  "DiosPerdoname@";  
$db	= "Registro";

$nombre =  $_GET["nombre"];
$Contrasena =  $_GET["Contrasena"];
echo  "nombre: $nombre <br>";
echo  "Contraseña: $Contrasena<br>";

if(isset ($_GET['nombre']) && !empty($_GET["nombre"]) && 
	isset ($_GET['Contrasena']) && !empty($_GET['Contrasena']))
	{
		$con = mysql_connect($host, $user, $pw) or die ("Problemas al conectar");
		mysql_select_db($db, $con) or die ("Problemas al conectar la DB");
		mysql_query("INSERT INTO registro1 (Nombre, PW) VALUES ('$_GET[nombre]','$_GET[Contrasena]')", $con);
		echo "datos insertados";
	}
	else {
		echo "Problemas al insertar datos";
	}
?>