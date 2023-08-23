<!DOCTYPE html>
<html>

<head>

    <title>Práctica 29 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //chdir Cambia de directorio

        //getcwd Devuelve el directorio actual

        //scandir Enumera el contenido de un directorio

        echo getcwd();

        echo "<br>";

        $directorio = scandir(getcwd());

        var_dump($directorio);

        chdir("../");
        
        echo getcwd();

    ?>
</body>

</html> 