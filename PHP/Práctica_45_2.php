<!DOCTYPE html>
<html>

<head>

    <title>Práctica 45 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Borrar datos

        $minombre = $_GET["nombre"];

        $servidor = "localhost";
        $usuario = "root";
        $password = "";

        $conexion = new mysqli($servidor, $usuario, $password) or die("Error de conexión");

        mysqli_select_db($conexion,"usuarios");

        $eliminar = "SELECT nombre FROM clientes";

        $registros = mysqli_query($conexion,$eliminar);

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
            $sql = "DELETE FROM clientes WHERE nombre = '$minombre'";
            mysqli_query($conexion,$sql);
            echo $minombre . " ha sido eliminado de la base de datos";
        } else {
            echo $minombre . " no se encuentra en la base de datos";
        }

    ?>

</body>
</html> 