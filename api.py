from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

app = FastAPI()

# get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session =  Depends(generador_sesion)):
    print("Api consultando lista de alumnos")
    return repo.mostrar_alumnos(sesion)
# get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumnos_por_id(id:int,sesion:Session = Depends(generador_sesion)):
    print("Api consultando alumnos por id")
    return repo.alumnos_por_id(sesion, id)
# get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id}/calificaciones")
def califi_por_id_alumn(id:int, sesion:Session = Depends(generador_sesion)):
    print("Api consultando calificaciones por id de alumno")
    return repo.calificaciones_por_id_alumno(sesion, id)
# get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumn (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api consultando foto por id de alumno")
    return repo.fotos_por_id_alumno(sesion, id)
# get("/fotos/{id}”)
@app.get("/fotos/{id}")
def fotos_por_id (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api consultando fotos por id")
    return repo.fotos_por_id(sesion, id)
# get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificaciones_por_id (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api consultando calificaciones por id")
    return repo.calificaciones_por_id(sesion, id)
# delete("/fotos/{id}”)
@app.delete("/fotos/{id}")
def borrar_foto (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api borrando fotos")
    repo.borrar_foto_por_id(sesion, id)
    return {"Foto_borrada", "ok"}
# delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def borrar_calificaciones (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api borrando calificaciones")
    repo.calificaciones_por_id(sesion, id)
    return {"calificacion_borrada", "ok"}
# delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def borrar_califi_por_id_alumn(id:int, sesion:Session = Depends(generador_sesion)):
    print("Api borrando calificacion por id de alumno")
    repo.borrar_califi_por_id_alum(sesion, id)
    return {"calificacion_borrada", "ok"}
# delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_por_id(id:int, sesion:Session = Depends(generador_sesion)):
    print("Api borrando fotos por id de alumno")
    repo.borrar_foto_por_id(sesion, id)
    return {"Foto_borrada", "ok"}
# delete("/alumnos/{id})
@app.delete("/alumnos/{id}")
def borrar_alumnos (id:int, sesion:Session = Depends(generador_sesion)):
    print("Api borrando alumnos por id")
    repo.borrar_califi_por_id_alum(sesion, id)
    repo.borrar_foto_por_id(sesion, id)
    repo.borrar_alumno_por_id(sesion, id)
    return{"Alumno_borrado", "ok"}