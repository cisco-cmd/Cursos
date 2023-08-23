<!DOCTYPE html>
<html>

<head>

    <title>Práctica 06 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Arrays indexados

        $dias = array("Lunes","Martes","Miercoles","Jueves","Viernes");

        $temperaturas = [23,14,31,10];

        //Array vacio sin número o con 15 espacios vacios
        $vacio = array(15);

        //Acceso al array

        echo $dias[1]. "<br>";
        echo $temperaturas[0]. "<br>";
        var_dump($dias);
        var_dump($temperaturas);


    ?>
</body>

</html> 