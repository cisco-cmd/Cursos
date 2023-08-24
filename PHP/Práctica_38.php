<!DOCTYPE html>
<html>

<head>

    <title>Práctica 38 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Formularios

        if(isset($_POST['usuario'])) {
            if(!empty($_POST['usuario'])){
                $usuario = $_POST['usuario'];
                echo "Nombre de usuario: " . $usuario . "<br>";
            }
        }

        if(isset($_POST['password'])) {
            if(!empty($_POST['password'])){
                $password = $_POST['password'];
                echo "Nombre de password: " . $password;
            }
        }

    ?>

</body>
</html> 