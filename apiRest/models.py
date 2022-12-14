from django import forms
from django.db import models
from djongo import models


class Espacio(models.Model):

    class TIPO_ESPACIO(models.TextChoices):
        CAFETERIA = 'CF','Cafeteria'
        AUDITORIO = 'AU','Auditorio'
        OFICINA_AD = 'OA', 'Oficina administrativa'
        OFICINA_DE = 'OD','Oficina docente'
        RESTAURANTE = 'RE','Restaurante'
        LABORATORIO = 'LAB','Laboratorio'
        SALA_ESTUDIO = 'SE','Sala de estudio'
        SALON = 'SA','Salon'
        SALA_COMPUTO = 'SC','Sala de computo'

    nombre = models.CharField(max_length = 100, default = "", null = True)
    sePuedeComer = models.BooleanField(default = False, null = True)
    tipoEspacio = models.CharField(choices=TIPO_ESPACIO.choices, null = True)
    prestamoEquipos = models.BooleanField(default = False, null = True)
    piso = models.CharField(max_length = 3)

    class Meta:
        abstract = True

class Edificio(models.Model):
    id_edificio = models.SmallIntegerField(primary_key = True, unique = True)
    nombre = models.CharField(max_length = 100)
    palabras_clave = models.CharField(max_length = 100, null = True)
    descripcion = models.CharField(max_length = 500)
    imagen = models.CharField(max_length = 500, null = True)
    aforoActual = models.IntegerField(default = 0, null = True)
    espacios = models.ArrayField(model_container=Espacio, null = True)
    listaDeEntradas = models.CharField(max_length = 500, null = True)

    class Meta:
        indexes = [
            models.Index(fields=['nombre']),
            models.Index(fields=['palabras_clave'])
        ]

class Nodo(models.Model):
    idNodo = models.IntegerField(primary_key = True, unique = True)
    peso = models.IntegerField(default = 0)
    habilitado = models.BooleanField(default = False, null = True)
    vecinos =  models.CharField(max_length = 500, null = True)
    tipoEspacio = models.FloatField(default = 1,null = True)


class HistorialUbicacion(models.Model):
    idNodo = models.IntegerField(default = 0, null = True)
    fecha = models.DateTimeField(auto_now_add = True, null = True)

    @classmethod
    def create(cls, idNodo, fecha):
        historial = cls(idNodo=idNodo,fecha = fecha)

        # do something with the book
        return historial

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['idNodo'])
        ]


class Usuario(models.Model):
    uId = models.CharField(max_length = 500, primary_key = True, unique = True, default = "")
    email = models.CharField(max_length = 200 , default = "")
    nombre = models.CharField(max_length = 200, default = "")
    nodoActual = models.IntegerField(default = -1, null = True)
    historialDeBusqueda = models.CharField(max_length = 500, null = True)
    historialDeUbicaciones = models.ArrayField(model_container=HistorialUbicacion, null = True)

