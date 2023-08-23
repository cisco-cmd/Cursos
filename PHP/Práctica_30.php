<!DOCTYPE html>
<html>

<head>

    <title>Práctica 30 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //is_int comprueba si un número es entero

        //is_float comprueba si un número es decimal

        $edad = 220000;

        $nota = 7.22;

        if(is_int($edad)){
            echo "El número ".$edad." es entero. <br>";
        }
        elseif(is_float($edad)){
            echo "El número ".$edad." es decimal. <br>";
        }

        if(is_int($nota)){
            echo "El número ".$nota." es entero. <br>";
        }
        elseif(is_float($nota)){
            echo "El número ".$nota." es decimal. <br>";
        }

        //number_format da formato a un número

        echo number_format($edad,2,",",".");

    ?>
</body>

</html> 