# technical-test-senior-python

## Instrucciones de instalacion

1. Clonar este repositorio:
  ```git clone https://github.com/AntonioUlloa01/tchnical-test-senior-python.git ```
2. Al clonar el repositorio validar que se encuentra en la rama **master* ya que ahi es donde esta alojado el proyecto.
3. Instalar python en caso de no tenerlo.
4. Crear un venv para la administración de los paquetes
   - Abrir una terminal en la carpeta raiz del proyecto y ejecutar el siguiente comando para la creación del venv "python -m venv .venv"
   - Ejecutar el siguiente comando para inicializar el venv
     ```.venv/Scripts/activate```
5. Instalar las dependencias del proyecto con el comando
     ```pip install -r requirements.txt```
6. Declaran la variable de entorno de Flask para poder ejecutarlo
   - En la terminal tenemos que movernos a la carpeta app
   - posteriormente ejecutamos el comando
     ```set "FLASK_APP=app.py```
  
## Ejecución del proyecto
1. dentro de la carpeta app ejecutamos el comando
   ```flask run```
   o bien
   ```python -m flask run```
   esto lanzará el servidor para poder realizar las consultas de los datos
3. En caso de que la base de datos no contenga información, existen archivos de migración que nos permitirán crear las tablas y llenarlas con datos de pruebas,
   para ello es necesario parar el servidor y ejecutar el siguiente comando
   ```flask db upgrade```, lo cual no permitirá ejecutar los archivos de migración y llevar la base de datos a la versión más reciente.


## Ejecución de pruebas unitarias
En la terminal nos movemos a la carpeta principal con el comando
``` cd ..```

una vez estando ubicados en la carpeta principal ejecutamos el comando
```pytest -v```

Para poder visualizar en consola la ejecución de las pruebas unitarias.


## Notas generales
1. En el problema de las estaciones del año por la fecha de creación de una orden existen un error en los resultados esperados
  En el número de orden **114-0291773-7262697** según la tabla la estación del año debería de ser **Winter** cuando lo correcto es que sea **Fall**
  En el número de orden **112-5230502-8173028** según la tabla la estación del año debería de ser **Summer* cuando lo correcto es que sea **Winter**

  Al momento de realizar las pruebas unitarias es definieron los casos de prueba según la tabla de resultados esperados, es por eso que dos de las pruebas fallan.

2. En el problema de las citas en la barbería, al ejecutar el reporte de los mejores 5 barberos solo se obtienen 4 registros, 
  aunque el sistema está preparado para mostrar los 5 barberos dentro de los datos de prueba proporcionados solo existen 4 barberos distintos, es por eso que
  solo se muestran 4 registros.

3. Al momento de ejecutar el reporte de los mejores 5 días existe días que tiene el mismo número de citas, por lo que sería necesario definir alguna regla de negocio
   que permita controlar los casos en los que existen registros con el mismo número de citas.



