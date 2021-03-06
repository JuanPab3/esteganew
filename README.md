# Método de uso

Esteganew es una libreria que maneja distintas herramientas para generar metodos de protección de la información; por medio de la estaganografia en imagenes.

### Recomendaciones Iniciales.
- Principalmente tener instalada las librerias _PIL_ y _cryptography_. <br/>
Para instalarlas, hay que usar los siguientes comandos en linux:
```
sudo pip3 install cryptography
```
```
sudo pip3 install PIL
```

- Toda imagen que valla a pasar por el proceso esteganografico, debe estar dentro de la carpeta. Del archivo a utilizar.


## Instrucciones de uso.

1. Para importar todo el contenido de esteganew hay que hacerlo de la siguiente forma:

```
from Esteganew.esteganew import *
```

2. Como gran parte de Esteganew esta orientada a objetos es importante tener en cuenta que para utilizar la libreria hay que crear objetos de tipo "Esteganew"
```
objeto = Esteganew(nombre_imagen, mensaje,nuevo_nombre)

```
Esta clase tiene requiere en un principio como primer argumento el nombre de la imagen que será utilizada (con extención tipo: '.png', '.tiff,' .jpg'... etc.) de tipo 'str', como segundo argumento el mensaje que se desea esconder tambien de tipo 'str' y para el tercer argumento se exige un nombre para el archivo de salida de tipo 'str'.

3. Los objetos de tipo Esteganew pueden implementar las siguientes funciones:

  * **generar_data():**<br/>
    Esta función se encarga de transformar el mensaje a binario. Lo que hace es adjuntar a una lista el valor de cada caracter, el cual se obtiene en un principio transformandolo a su valor en Unicode, y luego este a binario.

  * **modificar_pixeles()**<br/>
    La razón de esta función es la de convertir los pixeles necesarios de la imagen (según lo largo del mensaje) en nuvos pixeles alterando el valor RGB de cada pixel reduciendolo en una unidad.
  * **cambiar_pix()**<br/>
    Esta función se encarga de modificar ya en la nueva image los valores de los pixeles. A partir de las cordenadas (x, y) de la imagen.
  * **codificar()**<br/>
    La función codificar() esta dada para retornar un archivo en formato '.png', con el mensaje ya escondido.
  * **decodificar()**<br/>
    Esta función cumple la labor de retornar el mensaje oculto dentro de una imagen ya codificada.

4. Aparte de las funciones de tipo objeto Esteganew hay unas herramientas de encriptación de mensajes que pueden ayudar a proteger el mensaje dentro de la imagen:
  * **llave()**<br/>
    Con esta función se genera una llave para empezar el proceso de encriptación, la cual es de tipo "bytes", la cual es necesaria para poder crear un mensaje encriptado.
  * **enCRYptar()**<br/>
    Esta se encarga de recibir un mensaje de tipo str, y a partir de la función 'llave()', procesos de codificación nativos de python y el modulo de encriptación 'Feret' de la librería 'cryptography.fernet'.
  * **deCRYptar()**<br/>
    Se encarga de recibir un mensaje encriptado de tipo str y el nombre de un archivo con extención '.key', luego por medio de la función 'open()' nativa de python extrae el texto del archivo '.key' para aplicar  funciones del modulo Fermet, que ayudan a recuperar el mensaje encriptado.



__ __ __ __
Esperamos que pueda servir de algo... <br/>
Muchas gracias *<3*
