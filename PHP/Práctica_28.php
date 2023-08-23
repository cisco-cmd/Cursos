<!DOCTYPE html>
<html>

<head>

    <title>Práctica 28 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Fwrite escribe dentro del fichero y devuelve los bytes escritos, fputs es una alias

        //fflush fuerza a escribir los datos en el buffer del archivo

        $miarchivo = fopen("Recursos/pr_27.txt","a+");

        //fwrite($miarchivo, "Escribiendo dentro del fichero");
        //fflush($miarchivo);

        //stat devuelve un array asociativo con informacion del fichero
        //filesize devuelve el tamaño del fichero

        $arrayfich = stat("Recursos/pr_27.txt");
        var_dump($arrayfich);

        echo filesize("Recursos/pr_27.txt");

    ?>
</body>

</html> 