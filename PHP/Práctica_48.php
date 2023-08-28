<!DOCTYPE html>
<html>

<head>

    <title>Práctica 48 PHP</title>
    <meta charset="UTF-8">

</head>

<body>

    <?php

        //Creación de clases

        class alumno {
            
            private $nombre = null;

            private $apellidos = null;

            function getNombre() {
                return $this->nombre;
            }

            function getApellidos() {
                return $this->apellidos;
            }

            function setNombre($nombre) {
                return $this->nombre = $nombre;
            }

            function setApellidos($apellidos) {
                return $this->apellidos = $apellidos;
            }

            function calcularLetras($nombre) {
                return strlen($this->nombre);
            }

        }

        $alumno1 = new alumno();
        $alumno1->setNombre("Juan Carlos");
        $alumno1->setApellidos("Navidad Garcia");


        $nombreAlumno1 = $alumno1->getNombre();
        $apellidosAlumno1 = $alumno1->getApellidos();
        $letras = $alumno1->calcularLetras($nombreAlumno1);

        echo $nombreAlumno1;
        echo "<br>";
        echo $apellidosAlumno1;
        echo "<br>";
        echo $letras;

        if(class_exists("alumno")) {
            echo "Clase ". get_class($alumno1) ." esta definida";
        }

        $metodosAlumno = get_class_methods("alumno");
        var_dump($metodosAlumno);

        $propiedadesAlumno = get_class_vars("alumno");
        var_dump($propiedadesAlumno);

    ?>

</body>
</html> 