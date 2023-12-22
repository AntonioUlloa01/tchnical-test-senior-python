# tchnical-test-senior-python

## Instrucciones de instalacion

1. Clonar este repositorio:
  ```git clone https://github.com/AntonioUlloa01/tchnical-test-senior-python.git ```
3. Instalar python en caso de no tenerlo.
4. Crear un venv para la administracion de los paquetes
   - Abrir una terminal en la carpeta raiz del proyecto y ejecutar el sigueinte comando para la creacion del venv "python -m venv .venv"
   - Ejecutar el siguiente comando para inicializar el venv
     ```.venv/Scripts/activate```
5. Instalar las dependencias del proyecto con el comando
     ```pip install -r requirements.txt```
6. Declaran la variable entorno de Flask para poder ejecutarlo
   - En la terminal tenemos que movernos a la carpeta app
   - posteriormente ejecutamos el comando
     ```set "FLASK_APP=app.py```
  
## Ejecion del proyecto
1. dentro de la carpeta app ejecutamos el comando
   ```flask run```
   o bien
   ```python -m flask run```
   esto lanzara el servidor para poder realizar las consultas de los datos
3. En caso de que la base de datos no contenga información existen archivos de migración que nor permitiran crear las tablas y llenarlas con datos de pruebas,
   para ello es necesario parar el servidor y ejecutar el siguiente comando
   ```flask db upgrade```
    lo cual no permitira ejecutar los archivos de migracion y llevar la base de datos a la version mas reciente.


## Ejecucion de pruebas unitarios
En la terminal nos movemos a la carpeta principal con el comando
``` cd ..```

unaves estando ubicados en la carpeta principal ejecutamos el comando
```pytest -v```

para poder visualizar en consola la ejecuion de la pruebas unitarias.


##Notas generales
1. En el problema de las estaciones del año por la fecha de cracion de una orden exiten un error en los resultados esperados
  En el numero de orden **114-0291773-7262697** segun la tabla la estacion del año deberia de ser **Winter** cuando lo correcto es que sea **Fall**
  En el numero de orden **112-5230502-8173028** segun la tabla la estacion del año deberia de ser **Summer* cuando lo correcto es que sea **Winter**

  Al momento de realizar las pruebas unitarias es definieron los casos de prueba segun la tabla de resultados esperados es por eso que dos de las pruebas fallan.

2. En el problema de las citas en la barberia al ejecutar el reporte de los mejores 5 barberos solo se obtienen 4 registros, 
  aun que el sistema esta preparado para mostrar los 5 barberos dentro de los datos de prueba proporcionados solo existen 4 barberos distintos es por eso que
  solo se muestran 4 registros.

3. Al momento de ejecutar el reporte de los mejores 5 dias existe dias que tiene el mismo numero de citas por lo que seria necesario definir alguna regla de negocio
   que permita controlar los casos en los que existen registros con el mismo numero de citas.



