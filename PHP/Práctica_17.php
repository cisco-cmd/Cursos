<!DOCTYPE html>
<html>

<head>

    <title>Práctica 17 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Funciones

        $num1=5;
        $num2=10;

        function sumar() {
            echo "Soy la función sumar <br>";
        }

        sumar();

        function sumarnumeros($n1,$n2) {
            echo $n1 + $n2 ."<br>";
        }

        sumarnumeros($num1,$num2);

        function sumarnumerosreturn ($n1,$n2) {
            return $n1 + $n2;
        }

        $resultado = sumarnumerosreturn($num1,$num2);

        echo $resultado;

    ?>
</body>

</html> 