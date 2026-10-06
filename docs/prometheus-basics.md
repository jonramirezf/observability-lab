# Prometheus básico

## Objetivo

Agregar Prometheus al laboratorio de observabilidad usando Docker Compose.

## Configuración

Prometheus se ejecuta en un contenedor y queda disponible en:

http://localhost:9090

La configuración principal está en:

`prometheus/prometheus.yml`

El intervalo de recolección configurado es de 15 segundos.

## Conceptos aprendidos

- Target: sistema o servicio del que Prometheus obtiene métricas.
- Scrape: proceso de consultar un endpoint de métricas.
- `up`: indica si Prometheus puede obtener métricas de un target.
  - `1` = disponible
  - `0` = no disponible

## Estado actual

Prometheus está funcionando y su propio target aparece en estado `UP`.

## Próximo paso

Agregar métricas del sistema Linux para visualizar CPU y memoria del equipo.
