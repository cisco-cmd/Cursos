<!DOCTYPE html>
<html>

<head>

    <title>Práctica 37 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Destruye la sesión

        if(isset($_SESSION['iniciada']) == true) {

            session_unset();
            session_destroy();

        }
        else {
            echo "La sesión está finalizada";
        }
        
    ?>

</body>
</html> 