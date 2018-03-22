<?php
//include("conexion.php");
$host = "localhost";
$user = "root";
$pw	=  "DiosPerdoname@";  
$db	= "Registro";

if(isset ($_POST['nombre']) && !empty($_POST['nombre']) && 
	isset ($_POST['Contrasena']) && !empty($_POST['Contrasena']))
	{
		$con = mysql_connect($host, $user, $pw) or die ("Problemas al conectar");
		mysql_select_db($db, $con) or die ("Problemas al conectar la DB");
		mysql_query("INSERT INTO registro1 (Nombre, PW) VALUES ('$_POST[nombre]','$_POST[Contrasena]')", $con);
		echo "datos insertados";
	}
	else {
		echo "Problemas al insertar datos";
	}
?>