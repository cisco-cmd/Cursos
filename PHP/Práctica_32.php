<!DOCTYPE html>
<html>

<head>

    <title>Práctica 32 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //abs valor absoluto

        //max máximo de un conjunto de números

        //min mínimo de un conjunto de números

        //rand genera números aleatorios

        //sqrt calcula raíz cuadrada

        $num1=3.55;
        $num2=5.33;
        $num3=-1.2385;
        $num4=1100101;

        echo (abs($num3));

        echo "<br>";

        echo (max($num3,$num1,$num2));

        echo "<br>";

        echo (min($num3,$num1,$num2));

        echo "<br>";

        echo rand(1,100);

        echo "<br>";

        echo sqrt($num2);

        //decbin transforma de decimal a binario

        //bindec de binario a decimal

        //dechex de decimal a hexadecimal

        //hexdec de hexadecimal a decimal

        echo (decbin($num3));

        echo "<br>";

        echo (bindec($num4));

        echo "<br>";

        echo (dechex($num1));

        echo "<br>";

        echo hexdec("EA");

    ?>
</body>

</html> 