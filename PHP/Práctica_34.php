<?php

    if(isset($_GET['aceptar'])) {
        $caducidad = time() + (60*60*24*365);
        setcookie('micookie',1,$caducidad);
    }

?>

<!DOCTYPE html>
<html>

<head>

    <title>Práctica 34 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        if (!isset($_GET['ACEPTAR']) && !isset($_COOKIE['micookie'])) : ?>

        <div>
            <h2> Cookies </h2>
            <p> Debes aceptar las cookies para seguir navegando </p>
            <a href="?aceptar=1"> Aceptar </a>
        </div>

    <?php
    endif;
    ?>
</body>
</html> 