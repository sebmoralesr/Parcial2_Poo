# Parcial2_Poo
En este repositorio se encontrara un archivo el cual contiene el codigo de la implementacion, otro donde se encuentra la unittest, y el diagrama UML
En el codigo de la implementacion se encuntran ya hechos varios objetos, con los cuales se puede demostrar el funcionamiento del programa poniendo distintos datos como los del conductor, los asistentes y el camion, mas algunas cantidades para probar las toneladas recolectadas. Al correr el codigo se mostrara en pantalla un menu el cual le pedira al usuario que catidad deseara ver, entre ellas papel, plastico, vidrio, residuos y metal.
# Manual de Usuario - TrashCity

## Descripción
TrashCity es una aplicación que ayuda a gestionar la recolección de residuos en una ciudad. Permite registrar los turnos de recolección, realizar seguimiento de los puntos geográficos visitados durante los turnos y obtener información estadística sobre la cantidad de diferentes tipos de residuos recolectados por día.

## Requisitos del sistema
- Python 3.x instalado en el sistema.
- Conocimientos básicos de programación en Python.

## Instalación
1. Descarga el código fuente de la aplicación desde el repositorio Git.
2. Descomprime el archivo descargado en tu sistema.

## Configuración
1. Abre el archivo `main.py` en un editor de texto.
2. Realiza las siguientes modificaciones en el código según tus necesidades:

   - Define los puntos geográficos relevantes modificando la clase `PuntoGeografico`. Puedes agregar atributos adicionales según sea necesario.
   - Crea los turnos de recolección utilizando la clase `Turno`. Asigna las rutas, camiones, fechas de inicio y fin correspondientes. Puedes agregar registros de puntos geográficos utilizando el método `agregar_registro`.
   - Crea los camiones y conductores necesarios utilizando la clase `Camion`.
   - Crea las personas involucradas en la recolección utilizando la clase `Persona`.
   - Configura el centro de acopio utilizando la clase `CentroAcopio`. Puedes agregar registros de residuos utilizando el método `agregar_registro`.

## Uso
1. Abre una terminal o línea de comandos en tu sistema.
2. Navega hasta la ubicación donde descomprimiste el código fuente de TrashCity.
3. Ejecuta el siguiente comando para iniciar la aplicación:

   ```
   python main.py
   ```

4. Sigue las instrucciones en la interfaz de línea de comandos para interactuar con la aplicación. Podrás agregar turnos, registrar puntos geográficos visitados y obtener estadísticas sobre la cantidad de residuos recolectados por día.

## Ejemplos de Uso
### Agregar un turno de recolección
1. Selecciona la opción para agregar un turno en el menú principal.
2. Proporciona la información requerida, como la ruta, el camión, la fecha y hora de inicio y fin del turno.
3. Confirma la creación del turno.
4. Ahora puedes registrar los puntos geográficos visitados durante ese turno.

### Registrar puntos geográficos
1. Selecciona la opción para registrar puntos geográficos en el menú principal.
2. Proporciona la latitud y longitud del punto geográfico.
3. Confirma el registro del punto geográfico.
4. Puedes registrar varios puntos geográficos para el turno actual.

### Obtener estadísticas de residuos recolectados
1. Selecciona la opción para obtener estadísticas en el menú principal.
2. Elige el tipo de residuo del que deseas obtener estadísticas (vidrio, metal, plástico, residuos o papel).
3. Proporciona la fecha para la cual deseas obtener las estadísticas.
4. La aplicación calculará y mostrará la cantidad total de residuos recolectados para el tipo y fecha especificados.

## Soporte
Si tienes algún problema, pregunta o sugerencia, no dudes en contactar a nuestro equipo de soporte técnico. 
