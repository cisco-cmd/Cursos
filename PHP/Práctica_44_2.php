<!DOCTYPE html>
<html>

<head>

    <title>Práctica 44 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Comprobar datos

        $minombre = $_GET["nombre"];

        $servidor = "localhost";
        $usuario = "root";
        $password = "";

        $conexion = new mysqli($servidor, $usuario, $password) or die("Error de conexión");

        mysqli_select_db($conexion,"usuarios");

        $comprobar = "SELECT nombre FROM clientes";

        $registros = mysqli_query($conexion,$comprobar);

        while($registro=mysqli_fetch_row($registros)) {
            echo "Nombre: " . $registro[0];
            echo "<br>";
            if($registro[0] = $minombre){
                $encontrado = true;
            } else{
                $encontrado = false;
            }
        }

        if ($encontrado) {
            echo $minombre . " se encuentra en la base de datos";
        } else {
            echo $minombre . " no se encuentra en la base de datos";
        }

    ?>

</body>
</html> 