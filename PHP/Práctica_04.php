<!DOCTYPE html>
<html>

<head>

    <title>Práctica 04 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Función por parámetros
        $numero = 32;
        function prueba($prueba) {
            echo $prueba . "<br>";
        }

        //Función con variable global
        function prueba2() {
            global $numero;
            echo $numero;
        }

        echo prueba($numero);
        echo prueba2(). "<br>";

        //Variables globales

        echo "La variable número vale: " . $GLOBALS['numero'] . "<br>";
        echo "Nombre del servidor: " . $_SERVER['SERVER_NAME'] . "<br>";
        echo "Software del servidor: " . $_SERVER['SERVER_SOFTWARE'] . "<br>";
        echo "Puerto del servidor: " . $_SERVER['SERVER_PORT'] . "<br>";

    ?>
</body>

</html> 