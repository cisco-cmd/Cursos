<!DOCTYPE html>
<html>

<head>

    <title>Práctica 41 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Envió de emails

            $to = $_POST['mail'];
            $subject = "Email de confirmación";
            $mensaje = $_POST['mensaje'];
            $from = "jcnavidad04@gmail.com";
            $headers = "From: $from";
            mail($to,$subject,$mensaje,$headers);

    ?>

</body>
</html> 