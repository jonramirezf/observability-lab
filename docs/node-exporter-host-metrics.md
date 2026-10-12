# Métricas del host con Node Exporter

## Objetivo
Exponer y recolectar métricas del sistema Linux (ThinkPad T14) dentro de Prometheus.

## Arquitectura
Ubuntu Host (Node Exporter :9100) <--- Docker Container (Prometheus :9090)

## Pasos realizados
1. Instalación de `prometheus-node-exporter` en el sistema host.
2. Configuración de regla en UFW para permitir el tráfico en el puerto `9100/tcp`.
3. Configuración del trabajo `linux-host` en `prometheus/prometheus.yml` apuntando a `172.17.0.1:9100`.
4. Verificación del target en estado `UP` en `http://localhost:9090/targets`.

## Verificación
Consulta PromQL realizada para verificar la memoria disponible en GB:
`node_memory_MemAvailable_bytes / 1024 / 1024 / 1024`
