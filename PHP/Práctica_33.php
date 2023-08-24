<!DOCTYPE html>
<html>

<head>

    <title>Práctica 33 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Definir cookies

        //setcookie se utiliza para esto y se puede definir cuando expira con la función time

        setcookie("noexpira",1);

        setcookie("micookie",2,time()+10);

        //La cookie micookie expirará en 10s

        //$_COOKIE variable superglobal para obtener el valor de una cookie

        var_dump($_COOKIE);

        setcookie("idioma","esp");

        if(isset($_COOKIE['idioma']) && $_COOKIE['idioma'] == "esp") {
            echo "Se ha definido la cookie con idioma en español";
        }

        //Para borrar cookies podemos establecer una fecha de caducidad en negativo o utilizar la función unset

        setcookie("idioma","",time()-1);

    ?>
</body>

</html> 