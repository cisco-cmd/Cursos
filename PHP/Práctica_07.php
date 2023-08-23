<!DOCTYPE html>
<html>

<head>

    <title>Práctica 07 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Arrays asociativos

        $exploradores = array("explorador1" => "Chrome", "explorador2" => "Firefox", "explorador3" => "Opera");

        $datos = array("nombre" => "Juan", "apellido" => "Navidad", "edad" => 19);

        echo "explorador 1: " . $exploradores["explorador1"] . "<br>";

        echo "Nombre: " . $datos["nombre"] . "<br>";

        echo "Edad: " . $datos["edad"];

        var_dump($exploradores);

        var_dump($datos);

    ?>
</body>

</html> 