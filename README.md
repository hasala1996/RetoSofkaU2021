# RetoSofkaU2021
Este repositorio contiene el Challange Sofka 2021. Proyecto para juego de preguntas de seleccion multiple con unica respuesta, en Python.
Se utiliza la Programacion Orientada a Objetos, se emplean librerias como pandas para cargar el archivo de Excel como base de datos.
Es importante tener el archivo Base_Datos_Jugadoros_Historicos.xlsx cerrado mientras se ejecuta la aplicacion, cada vez que se termine de ejecutar, la aplicacion
guardara los registros historicos en este archivo de Excel y tambien los mostrará en consola.
Cuando la aplicacion no se esté ejecutando, se puede consultar el archivo de excel.
El archivo principal es ChallangeSofka.py, correr este archivo para iniciar el juego.
categoria1.text, categoria2.text,categoria3.text,categoria4.text,categoria5.text, contienen las pregutnas y respuestas de cada nivel.

Funcionalidades:
1. Registro de datos del jugador : nombre,apellidos, puntaje obtenido, nivel alcanzado
2. Seleccion de preguntas aleatorias dependiendo del nivel de dificultad.
3. Cada vez que se responde correctamente, aumenta de nivel.
4. Si el jugador lo desea, puede retirarse del juego con su premio acumulado o continuar jugando hasta finalizar
5. Si el usuario no contesta una respuesta correcta o valida, el juego se termina y pierde su acumulado.
6. Total de 25 preguntas almacenadas en archivos txt segun nivel de dificultad.
7. El premio se acumula cada vez que contesta correctamente.
8. Debe seleccionar 1 respuesta correcta de las 4 posibles.
