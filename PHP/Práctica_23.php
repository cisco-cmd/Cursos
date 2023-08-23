<!DOCTYPE html>
<html>

<head>

    <title>Práctica 23 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Funciones interesantes para arrays (count para contar elementos de un array, current muestra la posición del puntero, end muestra la posición del último puntero, reset ordena los punteros , array_search sirve para buscar un elemento de un array !devuelve la key!)

        $frutas = array("Naranja","Manzana","Pera","Plátano","Melón");

        $elementos = count($frutas);

        echo $elementos . "<br>";

        $colores = array("color1" => "rojo", "color2" => "verde", "color3" => "azul", "color4" => "naranja");

        $clave = array_search("azul",$colores);

        if ($clave) {
            echo "La clave de azul es: " . $clave;
        }
        else {
            echo "No se ha encontrado la clave de azul";
        }
    ?>
</body>

</html> 