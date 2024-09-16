# Lyata Algorithmics Test

Requeremientos: Python 3.10

### Ejecución: 

- Windows: python main.py
- Linux: python3 main.py

### Notas:

1. El sistema le indicará a través de la terminal el dato que está pidiendo (Número de tamaño de una lista o la lista separada por espacios)
2. El sistema detectará errores en los datos de entrada y le dará 3 intentos máximo en cada __etapa__. 
    - No se permiten caracteres o decimales en el dato del tamaño de una lista o en los items de las listas.
    - Está permitido omitir o dejar en blanco el tamaño de una lista, el sistema lo interpretará como una lista de tamaño libre.
    - En caso de ingresar un tamaño de lista, el sistema no le permitira ingresar una lista de un tamaño distinto aunque esta no tenga errores.

3. La ejecución del sistema tiene 5 etapas:
    - Ingreso del tamaño de la lista de prueba (solo presionar enter si desea un tamaño libre).
    - Ingreso de la lista de prueba.
    - Ingreso del tamaño de la lista de consulta (solo presionar enter si desea un tamaño libre).
    - Ingreso de la lista de consulta.
    - Muestra de resultados.

4. Ejemplo:

- Input
```
6
2 4 5 8 10 12
7
1 2 4 6 9 12 13
```

- Output
```
X 2
X 4
2 5
5 8
8 10
10 X
12 X
```