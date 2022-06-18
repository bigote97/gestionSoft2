Ejercicio clase 12
==================

Una empresa tiene los siguientes datos de sus empleados:

*   Nombre
*   Apellido
*   DNI
*   salario
*   Si es empleado eventual, una lista con los montos de cada una de las ventas concretadas por esa persona.
*   Sin es empleado permanente, la antigüedad.

El ingreso total de cada empleado es su salario más su comisión. Para calcular la comisión, se utiliza la siguiente fórmula: Para los empleados permanentes: Un 1% por cada año de antigüedad. Ejemplo: el trabajador que tiene 7 años de antigüedad tiene 7% de comisión, el trabajador con 12 años de antigüedad tiene 12% de comisión, etc. Para los empleados eventuales: Un 5% del total de ventas

### Se solicita:

Crear las clases EmpleadoEventual y EmpleadoPermanente. Entre otros métodos, estas clases deben tener un método para calcular la comisión, y otro para calcular el ingreso total. Este método debe ser polimórfico.

*   Agregar un empleado (eventual o permanente) a la lista.
*   Un método que reciba un nro de DNI y retorne el empleado que tiene ese DNI, o None si no hay ninguno.
*   Un método que reciba un texto, y retrone una lista de empleados cuyo cuyo nombre y/o apellido coincida (total o parcialmente) con ese texto.
*   Otros métodos que se puedan considerar necesarios.

#### Crear una clase Menu, que permita:

*   Agregar un empleado, tanto eventual como permanente.
*   Buscar un empleado por DNI.
*   Buscar un empleado por nombre y/o apellido.
*   Dado el DNI de un empleado, calcular su comisión y su ingreso total.
*   Mostrar un listado con nombre, apellido, DNI e ingreso total de todos los empleados de la lista.
*   Salir del programa.