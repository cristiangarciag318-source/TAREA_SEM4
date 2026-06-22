# Sistema de Gestion de Restaurante

Estudiante: Cristian Omar Garcia Aguilar  
Asignatura: Programacion Orientada a Objetos  
Semana: 4

---

## Descripcion del sistema

El proyecto consiste en un sistema basico de gestion para el restaurante
"Garcia y Punto", ubicado en Ambato. Fue desarrollado en Python aplicando
Programacion Orientada a Objetos.

El sistema permite registrar productos organizados por turno (Desayuno, Almuerzo
y Cena), gestionar su disponibilidad y precio, y administrar las reservas de los
clientes. Tambien es posible filtrar la carta por turno, buscar clientes por
cedula y obtener un resumen del dia con el total de comensales esperados.

El objetivo principal de la tarea es demostrar como organizar un proyecto en
modulos separados, comunicar archivos mediante importaciones y aplicar los
conceptos basicos de la POO: clases, objetos, constructores, atributos, metodos
y el metodo especial __str__.

---

## Estructura del proyecto

```
restaurante_app/
    modelos/
        __init__.py
        producto.py      - clase Producto
        cliente.py       - clase Cliente
    servicios/
        __init__.py
        restaurante.py   - clase Restaurante
    main.py              - punto de arranque del programa
```

### Descripcion de cada archivo

- modelos/producto.py: contiene la clase Producto, que representa un plato o
  bebida de la carta. Tiene atributos como codigo, nombre, turno, precio y
  disponibilidad, y metodos para activar, desactivar o cambiar el precio.

- modelos/cliente.py: contiene la clase Cliente, que representa a una persona
  con reserva en el restaurante. Guarda la cedula, nombre, telefono, numero de
  personas y si la reserva esta activa o fue cancelada.

- servicios/restaurante.py: contiene la clase Restaurante, que es el servicio
  central del sistema. Administra la carta y las reservas, filtra productos por
  turno, calcula el total de comensales y muestra el resumen del dia.

- main.py: es el punto de arranque. Crea todos los objetos, los agrega al
  servicio y ejecuta los metodos para mostrar el funcionamiento del sistema.

---

## Conceptos de POO aplicados

- Clases: Producto, Cliente, Restaurante.
- Constructor __init__: inicializa los atributos de cada objeto al crearlo.
- Atributos: definidos segun el contexto del restaurante (turno, reserva,
  numero de personas, disponibilidad del plato, etc.).
- Metodos: permiten gestionar y mostrar la informacion de los objetos.
- Metodo especial __str__: implementado en las tres clases para representar
  cada objeto como texto legible al imprimirlo en consola.
- Importaciones: main.py importa desde modelos y servicios; restaurante.py
  importa los modelos que necesita.

---

## Como ejecutar el programa

Desde la carpeta raiz del repositorio:

```
python restaurante_app/main.py
```

El programa muestra la carta completa, los productos del almuerzo, las reservas
registradas, el resultado de una busqueda por cedula y el resumen del dia.

---

## Reflexion sobre la modularizacion

Separar el codigo en modulos con responsabilidades distintas hace que el proyecto
sea mas facil de leer y de mantener. En este sistema, los modelos se encargan de
representar los datos (un plato, un cliente), el servicio concentra la logica del
negocio (como calcular comensales o filtrar por turno), y main.py solo coordina
la ejecucion.

Si en algun momento se necesita cambiar la forma en que se guardan los clientes,
se modifica unicamente el archivo cliente.py sin afectar el resto del codigo. Eso
es una ventaja concreta de programar con esta organizacion. La POO permite agrupar
datos y comportamientos en clases coherentes, lo que resulta en un codigo mas
ordenado, reutilizable y preparado para crecer.
