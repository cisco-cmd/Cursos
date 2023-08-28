<!DOCTYPE html>
<html>

<head>

    <title>Práctica 43 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Inserción de datos

        $minombre = $_GET["nombre"];

        $servidor = "localhost";
        $usuario = "root";
        $password = "";

        $conexion = new mysqli($servidor, $usuario, $password) or die("Error de conexión");

        mysqli_select_db($conexion,"usuarios");

        $insertar = "INSERT clientes (nombre) VALUE ('$minombre')";

        mysqli_query($conexion,$insertar);

    ?>

</body>
</html> 