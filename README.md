# Rush-Hour Solver with Planning

## About the Project


## Getting Started
### Installation and Usage
Para llevar a cabo este solver, solo se requiere de tener el ejecutable, con su archivo .dll, en el mismo directorio donde se quiere ejecutar. Para ello simplemente ha de:
1. Clonar este repositorio git:
``` 
$ git clone https://github.com/OscarMoliina/Rush-Hour-Solver 
```
Una vez clonado, habrá en el directorio los archivos `metricff.exe` y `cygwin1.dll`, junto a `domain.pddl` y el creador de problemas `rush_hour_creator.py`.

Para definir el estado inicial del puzle, ejecuta el script de python. Este pedirá 2 diccionarios donde cada clave será el número del coche y cada valor será una lista de menor a mayor de todas las celdas que ocupa:

2. Crea el estado inicial (ej.):
```
$ python3 rush_hour_creator
```
```python
>>> Ingrese los coches horizontales: {1:[12,13]}
>>> Ingrese los coches verticales: {1:[21,31]}
```
Este archivo escribirá en el fitxero `problem.pddl` el estado inicial del juego a resolver.

Una vez creado el estado inicial del juego, solo queda ejecutar el planificador con el dominio del problema y el estado inicial en cuestión:

3. Ejecuta el planificador:
```
$ ./metricff -o domain.pddl -f problem.pddl
```
Si el problema es resoluble, el planificador devolverá la traza de movimientos que hay que hacer para resolver el puzle de un modo parecido a este:
```
0: MOVER_DERECHA R C41 C42 C42 C43
1: MOVER_DERECHA R C42 C43 C43 C44
2: MOVER_DERECHA R C43 C44 C44 C45
3: MOVER_DERECHA R C44 C45 C45 C46
```

---
## Contact
Oscar Molina - oscar03molina@gmail.com

