<!DOCTYPE html>
<html>

<head>

    <title>Práctica 39 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Subida de ficheros al servidor desde un formulario

        var_dump($_FILES);

        $directorio = $_FILES['imagen']['tmp_name'];
        move_uploaded_file($directorio,$_FILES['imagen']['name']);

        echo $directorio;

    ?>

</body>
</html> 