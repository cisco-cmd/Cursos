<!DOCTYPE html>
<html>

<head>

    <title>Práctica 36 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //session_start Iniciar o reanudar una sesión asignando un ID único (Se coloca al principio del archivo)

        //session_id obtiene o asigna un id (Debe de ir antes del inicio de sesión)

        //session_name obtiene o asigna un nombre a la sesión (si no se indica el nombre se usa por defecto PHPSESSID definido en php.ini)

        session_id("22");

        echo session_id();

        echo "<br>";

        echo session_name();
        session_start();

        $_SESSION['iniciada'] = true;
        $_SESSION['nombre'] = "Juanca";

        var_dump($_SESSION);

        echo "<br>";

        echo "Nombre " . $_SESSION['nombre'];

        echo "<br>";

        unset($_SESSION['nombre']);

        if(isset($_SESSION['nombre']) == false) {
            echo "Nombre no definido";
        }

        //session_destroy destruye la información de una sesión

        session_destroy();

        //session_unset para eliminar sesiones;

    ?>

</body>
</html> 