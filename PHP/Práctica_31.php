<!DOCTYPE html>
<html>

<head>

    <title>Práctica 31 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //round redondea con la precisión indicada

        //ceil redondea hacia arriba

        //floor redondea hacia abajo

        $num1=3.55;
        $num2=5.33;
        $num3=-1.2385;

        echo round($num3,2);

        echo "<br>";

        echo ceil($num1);

        echo "<br>";

        echo floor($num2);

        echo "<br>";

        echo(round($num1,PHP_ROUND_HALF_UP));

        echo "<br>";

        echo(round($num3,PHP_ROUND_HALF_DOWN));

        echo "<br>";

        echo(round($num3,PHP_ROUND_HALF_ODD));

        echo "<br>";

        echo(round($num3,PHP_ROUND_HALF_EVEN));

    ?>
</body>

</html> 