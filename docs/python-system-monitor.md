# Monitor básico del sistema con Python

## Objetivo

Crear un script en Python que obtenga métricas básicas del sistema Linux.

## Métricas utilizadas

- CPU
- memoria RAM
- uso de disco

## Librería

Se utilizó `psutil` para consultar métricas del sistema.

## Script

El archivo principal es:

`python/system_monitor.py`

## Prueba realizada

El script mostró correctamente valores de CPU, RAM y disco del equipo.

También se agregó una condición para mostrar una advertencia cuando el uso de disco supera el 80%.

## Resultado

Se logró obtener métricas reales del sistema desde Python como primera práctica orientada a observabilidad.
