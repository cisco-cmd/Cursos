<!DOCTYPE html>
<html>

<head>

    <title>Práctica 22 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Funciones para modificar el contenido de un array (array_shift elimina el primer elemento del array y array_unshift permite añadir un elemento al principio del array)

        $frutas = array("Naranja","Manzana","Pera","Plátano","Melón");

        var_dump($frutas);

        $eliminado = array_shift($frutas);

        var_dump($eliminado);

        var_dump($frutas);

        array_unshift($frutas,"Melocotón");

        var_dump($frutas);

        //array_pop elimina el último elemento del array y array_push permite añadir elementos al final del array

        var_dump($frutas);

        $eliminado1 = array_pop($frutas);

        var_dump($eliminado1);

        var_dump($frutas);

        array_push($frutas,"Fresa");

        var_dump($frutas);


    ?>
</body>

</html> 