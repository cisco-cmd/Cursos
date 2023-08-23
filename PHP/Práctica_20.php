<!DOCTYPE html>
<html>

<head>

    <title>Práctica 20 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Funciones con arrays

        //array_diff encuentra diferencias entre arrays

        $numeros1 = array(11,22,33);
        $numeros2 = array(11,33,55);

        $colores = array("color1" => "rojo", "color2" => "verde", "color3" => "azul", "color4" => "naranja");
        $colores2 = array("color1" => "verde", "color2" => "azul", "color3" => "amarillo");

        $diferencias1 = array_diff($colores,$colores2);
        var_dump($diferencias1);

        //array_merge une dos o más arrays

        $diferencias2 = array_merge($colores,$colores2);
        var_dump($diferencias2);
    ?>
</body>

</html> 