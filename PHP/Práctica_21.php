<!DOCTYPE html>
<html>

<head>

    <title>Práctica 21 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Funciones para ordenar arrays (sort para ordenar en orden ascendente y rsort en descendente)

        $dias = array("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo");

        var_dump($dias);
        
        sort ($dias);

        var_dump($dias);

        rsort($dias);

        var_dump($dias);

        //Otra función para ordenar arrays es asort, los ordena en ascendente pero sin modificar las keys

        asort ($dias);

        var_dump($dias);

        //Otra función para ordenar arrays es ksort, los ordena en base a las keys

        $edades = array("Juan" => 18, "Miguel" => 20, "Ana" => 14);

        ksort ($edades);

        var_dump($edades);

        //Otra función para ordenar arrays es shuffle, los ordena de forma aleatoria

        shuffle($edades);
        var_dump($edades);

    ?>
</body>

</html> 