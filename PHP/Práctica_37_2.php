<!DOCTYPE html>
<html>

<head>

    <title>Práctica 37 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Capturar las variables que se han propagado

        session_start();

        if(isset($_SESSION['iniciada']) == true) {

            echo "Nombre: " . $_SESSION['nombre'];
            echo "<br>";
            echo "Edad: " . $_SESSION['edad'];

        }
        else{
            echo "No se ha definido la sesión";
        }

    ?>

</body>
</html> 