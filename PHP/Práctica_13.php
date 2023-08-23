<!DOCTYPE html>
<html>

<head>

    <title>Práctica 13 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //For

        $num = 5;

        //Numeros entre el 1 y el 10
        for($i=1;$i<=10;$i++) {
            echo $i;
            echo "<br>";
        }

        //Numeros pares del 0 al 30
        for($k=0;$k<=30;$k+=2) {
            echo $k;
            echo "<br>";
        }

        //Foreach

        $datos = array("uno" => 1, "dos" => 2, "tres" => 3);

        foreach($datos as $k => $v) {
            echo "Valores[$k] => $v";
            echo "<br>";
        }

    ?>
</body>

</html> 