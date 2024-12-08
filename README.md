# Prática SD- Implementación de ORM Y API con FastAPI
## Requisitos

- **Python 3.8+**
- **SQLAlchemy**
- **FastAPI**
- **PostgreSQL**
- **Psycopg2** (biblioteca para conectar PostgreSQL con Python)
## Estructura del proyecto 
├── orm/
│   ├── config.py         # Configuración                               de conexión a                               la base de                                  datos.
│   ├── modelos.py        # Mapeo de tablas                             a clases de                                 Python.
│   └── repo.py           # Consultas a la                              base de datos                               con SQLAlchemy.
├── api.py                # Implementación                              de la API con                               FastAPI.
├── bd_alumnos.sql        # Script SQL para crear la base de datos.

# Descripción de los archivos 

> orm/config.py

Configura la conexión a la base de datos PostgreSQL.

Contiene una función para crear sesiones de conexión a la base de datos.


> orm/modelos.py

Define las clases ORM mapeadas a las tablas:

Alumnos

Fotos

Calificaciones



> orm/repo.py

Implementa las siguientes consultas SQL usando SQLAlchemy:

* SELECT * FROM app.alumnos
* SELECT * FROM app.alumnos WHERE id={id_al}
* SELECT * FROM app.fotos
* SELECT * FROM app.fotos WHERE id={id_fo}
* SELECT * FROM app.fotos WHERE id_alumnos={id_al}
* SELECT * FROM app.calificaciones
* SELECT * FROM app.calificaciones WHERE id={id_fo}
* SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
* DELETE FROM app.alumnos WHERE id_alumnos={id_al}
* DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
* DELETE FROM app.fotos WHERE id_alumnos={id_al}

> api.py

Proporciona un servidor FastAPI que expone endpoints para:

Consultar alumnos, calificaciones y fotos.

Eliminar registros de alumnos, calificaciones y fotos.


Endpoints implementados:

* get("/alumnos”)
* get("/alumnos/{id})
* get("/alumnos/{id}/calificaciones")
* get("/alumnos/{id}/fotos")
* get("/fotos/{id}”)
* get("/calificaciones/{id}”)
* delete("/fotos/{id}”)
* delete("/calificaciones/{id}”)
* delete("/alumnos/{id}/calificaciones")
* delete("/alumnos/{id}/fotos")
* delete("/alumnos/{id})
