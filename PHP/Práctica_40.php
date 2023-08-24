<!DOCTYPE html>
<html>

<head>

    <title>Práctica 40 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Subida de ficheros al servidor desde un formulario

        $directoriosubida="C:\wamp64\www\php\img\ ";
        $max_file_size="20000000";
        $extensiones = array("jpg","png","pdf");

        if(isset($_POST["submit"]) && isset($_FILES['imagen'])){

            $errores=0;
            $nombre = $_FILES['imagen']['name'];
            $filesize = $_FILES['imagen']['size'];
            $directoriotemp = $_FILES['imagen']['tmp_name'];
            $tipo = $_FILES['imagen']['type'];
            $arrayfichero = pathinfo($nombre);
            $extension = $arrayfichero['extension'];

            if(!in_array($extension,$extensiones)){
                echo "Extensión no válida.";
                $errores = 1;
            }

            if($filesize > $max_file_size){
                echo "La imagen supera el tamaño máximo.";
                echo $filesize;
                $errores = 1;
            }

            if($errores == 0){
                $nombrecompleto = $directoriosubida.$nombre;
                move_uploaded_file($directoriotemp,$nombrecompleto);
                echo "Fichero subido correctamente. " . $nombrecompleto;

            }

        }

    ?>

</body>
</html> 