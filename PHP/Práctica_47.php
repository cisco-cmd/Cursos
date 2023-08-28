<!DOCTYPE html>
<html>

<head>

    <title>Práctica 47 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Creación de clases

        class PrimeraClase {
            public $nombre = "Juanca";

            public function mostrarNombre() {
                echo $this->nombre;
            }
        }

        $instancia = new PrimeraClase();

        echo $instancia->nombre;
        echo "<br>";
        $instancia ->mostrarNombre();
    ?>

</body>
</html> 