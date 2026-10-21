# 🚢 Hundir la Flota

## 1. Descripción del proyecto
Este proyecto consiste en una implementación del juego **Hundir la Flota**, desarrollada en Python. Se trata de un juego por turnos en el que el jugador compite contra la máquina con el objetivo de hundir todos sus barcos antes de que esta hunda los suyos.

La partida se desarrolla en un tablero de **10 × 10 casillas**. Los barcos se colocan aleatoriamente y el jugador debe introducir las coordenadas de sus disparos para intentar localizar y hundir la flota rival.

---

## 2. Estructura del proyecto
El código se organiza en cuatro módulos principales y una carpeta que contiene el archivo de audio.

```text
Hundir-la-Flota/
│
├── main.py
├── funciones.py
├── clases.py
├── variables.py
│
└── extras/
    └── Audio.mp3
```

### `main.py`
Es el archivo principal del programa y se encarga de gestionar el desarrollo de la partida. Sus principales responsabilidades son:
* Mostrar las instrucciones iniciales y el menú de selección del modo de juego.
* Crear los tableros del jugador y de la máquina.
* Iniciar la colocación aleatoria de los barcos.
* Gestionar los turnos y los disparos de ambos participantes.
* Comprobar los resultados de los disparos y las condiciones de finalización.
* Mostrar el resultado final de la partida y reproducir el sonido cuando se hunde un barco.

### `funciones.py`
Contiene las funciones auxiliares necesarias para el funcionamiento del juego:
* **`mostrar_tablero(tablero)`**: muestra un tablero por consola, incluyendo las coordenadas de filas y columnas.
* **`coordenadas()`**: solicita al jugador las coordenadas de un disparo y comprueba que sean números válidos dentro de los límites del tablero.
* **`disparo_maquina()`**: genera aleatoriamente las coordenadas de un disparo de la máquina.
* **`menu()`**: muestra las opciones disponibles y devuelve la modalidad seleccionada.

### `clases.py`
Contiene la clase `Tablero`, que representa el tablero de cada participante y gestiona la información relacionada con los barcos y los disparos. La clase incluye los siguientes atributos y métodos:

#### Atributos
* **`tablero_propio`**: matriz que representa el tablero propio, con los barcos y los resultados de los disparos recibidos.
* **`tablero_disparos`**: matriz en la que se registran los disparos realizados contra el rival.
* **`barcos_restantes`**: número de casillas de barco que todavía no han sido alcanzadas.

#### Métodos
* **`colocar_barcos()`**: coloca aleatoriamente los barcos, comprobando que quepan en el tablero y que no se solapen ni se toquen entre sí.
* **`recibir_disparo(fila, columna)`**: comprueba el resultado de un disparo recibido y determina si un barco ha sido tocado o hundido.
* **`registrar_disparo(fila, columna, resultado)`**: actualiza el tablero de disparos según el resultado obtenido.
* **`disparo_repe(fila, columna)`**: comprueba si ya se ha disparado anteriormente a una casilla.

### `variables.py`
Centraliza las constantes y la configuración general del juego:
* **Dimensiones del tablero**: 10 filas y 10 columnas.
* **Símbolos**: utilizados para representar el agua, los barcos, los impactos y los fallos.
* **Distribución de la flota**: definida mediante un diccionario que relaciona la eslora de cada barco con su cantidad.

Esta organización permite modificar la configuración del juego sin tener que cambiarla en múltiples partes del código.

---

## 3. Funcionamiento del juego

### 3.1. Inicialización
Al ejecutar el programa, se muestran las instrucciones y el menú principal. Una vez seleccionada la modalidad, se crean los tableros correspondientes al jugador y a la máquina. 

A continuación, se colocan aleatoriamente los barcos de ambas flotas en orientación horizontal o vertical. El programa comprueba que cada barco permanezca dentro de los límites del tablero y que ninguna de sus casillas esté ocupada ni sea adyacente a otro barco.

### 3.2. Turno del jugador
Durante el turno del jugador, se muestran su tablero y el registro de sus disparos contra la máquina. El jugador introduce una fila y una columna, ambas comprendidas entre 0 y 9. Si las coordenadas no son válidas, se solicitan de nuevo. Si la casilla ya había sido atacada, también se pide elegir otra. 

Cuando el disparo es válido, se comprueba si alcanza un barco enemigo:
* **Impacto**: se marca la casilla con `X`. El jugador conserva el turno y puede volver a disparar.
* **Fallo**: se marca la casilla con `O` y el turno pasa a la máquina.
* **Barco hundido**: cuando todas las casillas de un barco han sido alcanzadas, se notifica que ha sido hundido y se reproduce un efecto de sonido.

### 3.3. Turno de la máquina
La máquina genera aleatoriamente las coordenadas de sus disparos. Antes de disparar, comprueba que no haya atacado previamente esa casilla. El número de disparos realizados durante este turno depende de la modalidad seleccionada:
* **Modo normal**: realiza un disparo.
* **Modo de mayor dificultad**: realiza dos disparos.

Los resultados se registran en los tableros correspondientes y se actualiza el número de casillas de barco que quedan a flote.

### 3.4. Finalización de la partida
La partida continúa mientras ambos participantes tengan casillas de barco sin alcanzar. Cuando uno de ellos pierde todas las casillas de su flota, el juego finaliza y se muestra un mensaje indicando si el jugador ha ganado o si la máquina ha resultado vencedora.

---

## 4. Características principales
* **Tablero de 10 × 10**: utiliza coordenadas numéricas para localizar las casillas.
* **Colocación aleatoria**: los barcos se generan en posiciones y orientaciones aleatorias.
* **Separación entre barcos**: los barcos no pueden solaparse ni tocarse, tampoco en diagonal.
* **Dos modalidades de dificultad**: la máquina puede realizar uno o dos disparos por turno.
* **Validación de coordenadas**: se comprueba que las entradas del jugador estén dentro de los límites del tablero.
* **Control de disparos repetidos**: se evita que los participantes vuelvan a disparar a una casilla ya atacada.
* **Registro de impactos y fallos**: los resultados se reflejan en las matrices de los tableros.
* **Detección de barcos hundidos**: se registran las casillas pendientes de cada barco para determinar cuándo ha sido hundido.
* **Efectos de sonido**: se reproduce un archivo de audio cuando el jugador hunde un barco enemigo.

---

## 5. Configuración de la flota
La distribución de los barcos se define en `variables.py` mediante el diccionario `barcos_dict`. Las claves representan la eslora de los barcos, medida en casillas, y los valores indican cuántos barcos hay de cada tamaño.

| Eslora | Cantidad |
| :--- | :--- |
| 1 casilla | 4 |
| 2 casillas | 3 |
| 3 casillas | 2 |
| 4 casillas | 1 |
| **Total** | **10 barcos** |

Cada flota ocupa un total de **20 casillas**.

---

## 6. Tecnologías y dependencias
El proyecto utiliza las siguientes herramientas y módulos:
* **Python**: lenguaje utilizado para desarrollar la lógica del juego.
* **`random`**: permite generar posiciones, orientaciones y disparos aleatorios.
* **`time`**: introduce pausas entre mensajes para controlar el ritmo de la partida.
* **`pygame`**: se utiliza para reproducir el sonido asociado al hundimiento de un barco.

### Instalación de dependencias
Para instalar Pygame, es necesario ejecutar el siguiente comando en la terminal:

```bash
pip install pygame
```

*Nota: Los módulos `random` y `time` forman parte de la biblioteca estándar de Python, por lo que no necesitan instalarse por separado (pero sí que hay que importarlas).*

---

## 7. Ejecución
Una vez instaladas las dependencias y comprobado que los archivos se encuentran en las rutas correspondientes, el juego se inicia ejecutando el archivo principal:

```bash
python main.py
```

El programa se ejecuta en la consola, desde la que se muestran los tableros, se introducen las coordenadas y se reciben los mensajes correspondientes al desarrollo de la partida.
