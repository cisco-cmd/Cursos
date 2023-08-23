<!DOCTYPE html>
<html>

<head>

    <title>Práctica 18 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Paso por valor y por referencia (En una hace una copia de la variable sin modificarla en otra utiliza directamente la variable original y la modifica)

        $num1=4;

        function mifuncion ($n1) {

            $n1 = $n1 +2;

        }

        function otrafuncion(&$n1) {
            $n1 = $n1 +2;
        }

        mifuncion($num1);
        echo $num1 . "<br>";

        otrafuncion($num1);
        echo $num1 . "<br>";
    ?>
</body>

</html> 