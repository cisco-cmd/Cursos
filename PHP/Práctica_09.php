<!DOCTYPE html>
<html>

<head>

    <title>Práctica 09 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        $num1=10;
        $num2=20;
        $num3=30;
        $num4=30;
        $num4=40;

        //Operadores de incremento/decremento ++ --

        echo ++$num1."<br>";
        echo --$num2."<br>";

        //Operadores lógicos AND(&&) OR(||) XOR NOT(!)

        if($num1+$num2 && $num3 == $num4) {
            echo "La suma de num1 y num2 y num3 es igual a num4 <br>";
        }
        else {
            echo "La suma de num1 y num2 y num3 no es igual a num4 <br>";
        }

        if($num1+$num2 || $num3 == $num4) {
            echo "La suma de num1 y num2 y num3 es diferente a num4 <br>";
        }
        else {
            echo "La suma de num1 y num2 y num3 es igual a num4 <br>";
        }

        //Operadores para String LO VISTO CON LA CONCATENACIÓN

    ?>
</body>

</html> 