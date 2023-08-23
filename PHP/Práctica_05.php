<!DOCTYPE html>
<html>

<head>

    <title>Práctica 05 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Constantes

        const PI = 3.14;
        echo PI . "<br>";

        //Definir

        define("PI2",3.141592);
        echo PI2 . "<br>";

        //Variables pasadas, fichero 05_2
        echo "Nombre: " . $_GET["nombre"] . " y apellido: " . $_GET["apellido"];


    ?>
</body>

</html> 