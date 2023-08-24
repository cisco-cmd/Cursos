<!DOCTYPE html>
<html>

<head>

    <title>Práctica 37 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Combinar sesiones con diferentes páginas

        session_start();

        $_SESSION['iniciada']=true;
        $_SESSION['nombre']="Juanca";
        $_SESSION['edad']=20;

        echo "Identificador de la sesion: " . session_id();
        echo "<br>";
        echo "Nombre de la sesion: " . session_name();
        echo "<br>";
        echo "Nombre: " . $_SESSION['nombre'];
        echo "<br>";
        echo "Edad: " . $_SESSION['edad'];
        echo "<br>";
        echo "<a href='Práctica_37_2.php'> Comprobar las variables en otra web </a>";
        echo "<br>";
        echo "<a href='Práctica_37_3.php'> Finaliza la sesión </a>";


    ?>

</body>
</html> 