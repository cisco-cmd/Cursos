<!DOCTYPE html>
<html>

<head>

    <title>Práctica 46 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Borrar datos

        $minombre = $_GET["nombre"];

        $modificar = $_GET["seleccionar"];

        $servidor = "localhost";
        $usuario = "root";
        $password = "";

        $conexion = new mysqli($servidor, $usuario, $password) or die("Error de conexión");

        mysqli_select_db($conexion,"usuarios");

        $sql = "UPDATE clientes SET nombre = '$minombre' WHERE nombre = '$modificar'";
        mysqli_query($conexion,$sql);

    ?>

</body>
</html> 