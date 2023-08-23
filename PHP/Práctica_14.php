<!DOCTYPE html>
<html>

<head>

    <title>Práctica 14 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //While

        $num=10;

        while($num >=0) {
            echo $num;
            echo "<br>";
            $num--;
        }

        //Do while

        while($num != 10) {
            echo "<br> Dentro del while";
        }
        
        do {
            echo "<br> Dentro del do while";
        } while($num != 10);

    ?>
</body>

</html> 