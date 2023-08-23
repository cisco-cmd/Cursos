<!DOCTYPE html>
<html>

<head>

    <title>Práctica 19 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Recursividad

        function factorial($n1){
            if($n1==1) {
                return 1;
            }
            else {
                echo $n1 . "x";
                return $n1 * factorial($n1-1);
            }
        }

        $resultado=factorial(5);
        echo "<br>";
        echo $resultado;

    ?>
</body>

</html> 