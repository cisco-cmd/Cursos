<!DOCTYPE html>
<html>

<head>

    <title>Práctica 12 PHP</title>
    <meta charset="UTF-8">

</head>

<body>
    <?php

        //Switch

        $dia=3;

        switch($dia){
            case 1:
                echo "Lunes";
            break;
            case 2:
                echo "Martes";
            break;
            case 3:
                echo "Miercoles";
            break;
            default:
                echo "Día no válido";
        }

    ?>
</body>

</html> 