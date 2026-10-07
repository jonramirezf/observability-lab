cat > docs/yaml-basics.md <<'EOF'
# YAML - Conceptos básicos

YAML es un formato de texto utilizado para escribir configuraciones de forma estructurada y legible.

Sus extensiones más comunes son:

- `.yaml`
- `.yml`

## Idea principal

YAML no ejecuta nada por sí solo.

Otra herramienta lee el archivo y utiliza esa configuración.

Ejemplos:

- Docker Compose → `compose.yaml`
- Prometheus → `prometheus.yml`
- GitHub Actions → archivos `.yml`
- Kubernetes → archivos `.yaml`
- OpenTelemetry → archivos `.yaml`

## Claves y valores

```yaml
nombre: prometheus
puerto: 9090
