<!DOCTYPE html>
<html>

<head>

    <title>Práctica 42 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Crear base de datos

        $servidor = "localhost";
        $usuario = "root";
        $password = "";

        $conexion = new mysqli($servidor, $usuario, $password);

        if(!$conexion) {
            echo "Conexión fallida";
        }
        else{
            $sql = "CREATE DATABASE usuarios";
            if(mysqli_query($conexion,$sql)) {
                echo "Base de datos creada con éxito";
            }
            else{
                echo "error: ". mysqli_error($conexion);
            }

            mysqli_select_db($conexion,"usuarios");
            $sql2 = "CREATE TABLE clientes(nombre VARCHAR(20))";
            mysqli_query($conexion,$sql2);
        }

    ?>

</body>
</html> 