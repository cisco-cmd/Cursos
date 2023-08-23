<!DOCTYPE html>
<html>

<head>

    <title>Práctica 15 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Break y Continue

        for($i=1;$i<=10;$i++) {
            echo "El valor de i ". $i . "<br>";
            if($i == 3) {
                break;
            }
        }

        for($k=1;$k<=10;$k++) {
            if($k == 3) {
                continue;
            }
            echo "El valor de k ". $k . "<br>";
        }

    ?>
</body>

</html> 