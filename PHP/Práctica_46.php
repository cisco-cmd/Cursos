<!DOCTYPE html>
<html>

<head>

    <title>Práctica 46 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <form name="myform" method="get" action="Práctica_46_2.php">
        <p>
            <label for="nombre"> Nombre: </label>
            <input type="text" name="nombre">

    <?php

        //Actualización de datos

        $minombre = $_GET["nombre"];

        $servidor = "localhost";
        $usuario = "root";
        $password = "";

        $conexion = new mysqli($servidor, $usuario, $password) or die("Error de conexión");

        mysqli_select_db($conexion,"usuarios");

        $consultar = "SELECT nombre FROM clientes";

        $registros = mysqli_query($conexion,$consultar);

        echo "<label for = 'seleccionar'> Elige un nombre: </label>";
        echo "<select name = 'seleccionar' >";
        while($registro=mysqli_fetch_row($registros)){
            echo "<option value='$registro[0]'>".$registro[0]."</option>";
        }

        echo "</select>";

    ?>

    <input type="submit" value="Modificar">

</body>
</html> 