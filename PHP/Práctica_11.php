<!DOCTYPE html>
<html>

<head>

    <title>Práctica 11 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //If y Else

        $num1 = 4;
        $num2 = 8;
        $dia = 5;

        if($num1>=5) {
            echo "<br> Aprobado";
        }
        else {echo "<br> Suspenso";}

        if($num2>=5) {
            echo "<br> Aprobado";
        }
        else {echo "<br> Suspenso";}

        //Operador ternario

        $final = $num1 >= 5 ? "<br> Aprobado" : "<br> Suspenso";

        echo $final;

        //elseif / else if

        if($num1>$num2) {
            echo "<br> Es mayor";
        }
        elseif ($num1==$num2) {
            echo "<br> Es igual";
        }
        else {
            echo "<br> Es menor";
        }

    ?>
</body>

</html> 