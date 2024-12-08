# Mediante el uso de la biblioteca SQLAlchemy, implementa las siguientes consultas (select y delete) a la BD.
import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# SELECT * FROM app.alumnos
def mostrar_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()
# SELECT * FROM app.alumnos WHERE id={id_al}
def alumnos_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.alumnos WHERE id={id_al}", id_al)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_al).first()
# SELECT * FROM app.fotos
def mostrar_fotos (sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()
# SELECT * FROM app.fotos WHERE id={id_fo}
def fotos_por_id(sesion:Session, id_fo:int):
    print("SELECT * FROM app.fotos WHERE id={id_fo}", id_fo)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_fo).first()
# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def fotos_por_id_alumno (sesion:Session, id_al:int):
    print("SELECT * FROM app.fotos WHERE id_alumnos={id_al}", id_al)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_al).first()
# SELECT * FROM app.calificaciones
def mostrar_calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()
# SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificaciones_por_id(sesion:Session, id_fo:int):
    print("SELECT * FROM app.calificaciones WHERE id={id_fo}", id_fo)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id== id_fo).first()
# SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_por_id_alumno(sesion:Session, id_al:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}", id_al)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_al).first()
# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borrar_alumno_por_id (sesion:Session, id_al:int):
    print("DELETE FROM app.alumnos WHERE id_alumnos={id_al}", id_al)
    alumn = alumnos_por_id(sesion, id_al)
    if alumn is not None:
        sesion.delete(alumn)
        sesion.commit()
    respuesta = {
        "mensaje":"Alumno eliminado"
    }
    return respuesta
# DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def borrar_califi_por_id_alum(sesion:Session, id_al:int):
    print("DELETE FROM app.calificaciones WHERE id_alumnos={id_al}", id_al)
    alumn = calificaciones_por_id (sesion, id_al)
    if alumn is not None:
        sesion.delete(alumn)
        sesion.commit()
    respuesta = {
        "mensaje":"Alumno eliminado"
    }
    return respuesta
# DELETE FROM app.fotos WHERE id_alumnos={id_al}
def borrar_foto_por_id(sesion:Session, id_al:int):
    print("DELETE FROM app.fotos WHERE id_alumnos={id_al}", id_al)
    alumn = fotos_por_id(sesion, id_al)
    if alumn is not None:
        sesion.delete(alumn)
        sesion.commit()
    respuesta={
        "mensaje":"Alumno eliminado"
    }
    return respuesta
