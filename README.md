# RushHour - Planning

## About the Project


## Getting Started
### Installation and Usage
Para llevar a cabo este solver, solo se requiere de tener el ejecutable, con su archivo .dll, en el mismo directorio donde se quiere ejecutar. Para ello simplemente ha de:
1. Clonar este repositorio git:
``` 
$ git clone https://github.com/OscarMoliina/RushHour_Planning 
```
Una vez clonado, habrá en el directorio los archivos `metricff.exe` y `cygwin1.dll`, junto a `domain.pddl` y el creador de problemas `rush_hour_creator.py`.

Para definir el estado inicial del puzle, ejecuta el script de python con los siguientes argumentos `<coches_horizontales> <coches_verticales>`, 2 diccionarios donde cada clave será el número del coche y cada valor será una lista de menor a mayor de todas las celdas que ocupa:

2. Crea el estado inicial (ej.):
```
$ python3 rush_hour_creator {1:[11,12,13],2:[24,25]} {1:[45,55]}
```
Este archivo escribirá en el fitxero `problem.pddl` el estado inicial del juego a resolver.

Una vez creado el estado inicial del juego, solo queda ejecutar el planificador con el dominio del problema y el estado inicial en cuestión:

3. Ejecuta el planificador:
```
$ ./metricff -o domain.pddl -f problem.pddl
```

---
## Contact
Oscar Molina - oscar03molina@gmail.com

