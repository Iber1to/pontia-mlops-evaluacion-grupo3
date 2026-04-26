# Rollback

El rollback consiste en volver a desplegar una versión anterior estable del modelo o del código.

## Rollback de código

1. Identificar el commit estable anterior en GitHub.
2. Crear una rama de rollback:

```bash
git checkout main
git pull origin main
git checkout -b rollback/version-estable
```

3. Revertir el commit problemático:

```bash
git revert <commit_sha>
```

4. Subir la rama:

```bash
git push origin rollback/version-estable
```

5. Crear Pull Request contra `main`.
6. Esperar a que pase la pipeline de integración.
7. Solicitar Code Review.
8. Hacer merge.
9. Ejecutar de nuevo el workflow de deploy si aplica.

---

## Rollback de modelo

Los modelos entrenados se registran como artefactos en GitHub Releases. Para volver a una versión anterior:

1. Ir a la sección **Releases** del repositorio.
2. Identificar una release estable anterior, por ejemplo:

```text
model-1
```

3. Volver a publicar los artefactos estables como una nueva release, por ejemplo:

```text
model-rollback-1
```

4. Redesplegar la API en Render
5. Validar que la API arranca correctamente y descarga los artefactos de la nueva última release.
6. Probar los endpoints:

```text
/health
/docs
/predict
/metrics
```

Como la API usa /releases/latest, no apunta a una versión fija concreta del modelo. Por eso, para hacer rollback no basta con seleccionar una release anterior: hay que conseguir que los artefactos estables vuelvan a estar disponibles como la última release publicada, o modificar el código para permitir seleccionar una release concreta mediante una variable de entorno.

---

## Rollback desde Render

En Render también puede realizarse rollback desde el historial de despliegues:

1. Entrar en el servicio desplegado.
2. Abrir la sección de deploys.
3. Seleccionar un despliegue anterior correcto.
4. Ejecutar redeploy de esa versión.
5. Validar `/health`, `/docs` y `/predict`.

---

## Mejora futura

Una mejora posible sería añadir una variable de entorno `MODEL_VERSION` para permitir que la API descargue una release concreta en lugar de usar siempre `/releases/latest`.

Ejemplo:

```text
MODEL_VERSION=model-1
```

---
