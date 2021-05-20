Introducción
============

Descripción
***********

Este Sistema, desarrollado en Python 3, ha sido creado como un código solución complementario al TFG - Sistemas de recomendaciones para accessos a estadios de fútbol.
Dicho TFG trata de definir y crear un sistema de recomendaciones para los usuarios que desean acceder a un estadio de futbol, de forma que se brinden a estos diferentes soluciones de rutas 
en función de las necesidades de cada espectador.

Este sistema ofrece 4 salidas o rutas distintas al usuario:

* Rutas más corta desde la puerta de entrada hasta el asiento.
* Rutas más rapia desde la puerta de entrada hasta el asiento.
* Rutas más corta y que maximice las necesidades del usuario.
* Ruta con simulación de control de aglomeraciones.

Instalación
***********
El código no require de instalación pero si si de una serie de pasos de configuraciones para poder ejecutarlo.

1. Instalar Python3:
--------------------
Python debe estar instlado en el equipo para poder ejecutar el programa.

Se puede descargar desde la `Página oficial de Python <https://www.python.org/downloads/>`_


2. Instalar librerías:
----------------------
Se deben instalar la siguientes librarías para poder ejecutar el programa:

Matplotlib

.. code:: bash

    $ pip install matplotlib
	
Networkx
.. code:: bash


    $ pip install networkx
	
Colorama

.. code:: bash

    $ pip install colorama
	

	
3. Distribución de ficheros y carpetas:
---------------------------------------
Los ficheros deben estar colocados de la siguiente forma::

    
		CODIGO
		├── Main.py
		├── Funciones.py
		├── Clases.py
		└── Ficheros
			├── Sectores.csv
			├── Nodos.json


Ejecución
****************
Para ejecutar el progrma se debe lanzar el programa Main.py


En Windows:

Doble click en el fichero Main.py 


Desde la CMD

.. code:: bash

    $ python Main.py


.. code:: bash

    $ python3 Main.py


	

En Linux:

.. code:: bash

    $ python Main.py


.. code:: bash

    $ python3 Main.py



Uso del programa
****************

Al ejecutar el programa Main.py:

1. Se muestra el grafo del estadio al usuario.

2.El usuario debe introducir los datos de su asiento:

* Sector - Con un formato SXX (Donde XX es el numero que identifica al sector)

* Fila 

* Columna

* Puerta de entrada

.. note:: Si el sector o la columna esta fuera del rango de filas o columnas del sector, se producirá una excepción.
.. note:: Actualmente solo se permite la puerta de entrada 'P1'.


3. Se selecciona el tipo de ruta que se desea obtener.

.. note:: Si el tipo es  'Rutas más corta y que maximice las necesidades del usuario', se abrirá una ventana para solicitar las preferencias del usuario.


