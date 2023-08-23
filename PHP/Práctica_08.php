<!DOCTYPE html>
<html>

<head>

    <title>Práctica 08 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Operadores
        $num1 = 5;
        $num2 = "10";

        echo "La suma de ".$num1." y ".$num2." es igual a ".$num1 + $num2."<br>";

        //Igual con restas, multiplicaciones, divisiones, restos, etc...

        //Comienzos del if y comparadores

        if($num1==$num2) {
            echo "<br> Son iguales";
        }
        else {echo "<br> no son iguales";}

        if($num1!=$num2) {
            echo "<br> No son iguales";
        }
        else {echo "<br> Son iguales";}

        if($num1===$num2) {
            echo "<br> Son iguales y del mismo tipo";
        }
        else {echo "<br> no son iguales o de diferente tipo";}

        if($num1<$num2) {
            echo "<br>".$num1." es menor que ".$num2;
        }
        else {echo "<br>".$num1." es mayor que ".$num2;}


        

        //Operador ternario

        $num1<>$num2?"No son iguales":"Son iguales";


    ?>
</body>

</html> 