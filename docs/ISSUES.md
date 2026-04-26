# Issues y problemas encontrados durante el desarrollo

Este documento recoge los principales problemas encontrados durante el desarrollo del proyecto, así como las soluciones aplicadas.

## 1. Required status check no aparecía en GitHub Rulesets

### Problema

Al configurar el ruleset de la rama `main`, GitHub mostraba `No results` al intentar añadir el check obligatorio.

### Causa

El workflow de integración todavía no había generado un status check seleccionable para la rama/PR, o se estaba buscando por el nombre del workflow en lugar del nombre del job.

### Solución

Se ejecutó la pipeline de integración desde un Pull Request y se añadió como required check el job `integrate`.

### Resultado

La rama `main` quedó protegida con:

- Pull Request obligatorio.
- Status check obligatorio.
- Rama actualizada antes de mergear.
- Bloqueo de force push.
- Restricción de borrado.

---

## 2. Cambios build.yml ejecución manual

- Se añade `workflow_dispatch` al workflow de Build Model.
- Se mantiene el trigger automático en push a `main`.
- Se deja el workflow alineado con los requisitos del ejercicio.

### Validación

- El workflow podrá ejecutarse manualmente desde GitHub Actions.
- El build seguirá ejecutándose automáticamente tras merge a `main

---

## 3.Mejora del flujo CD: deploy automático tras build correcto

### Situación inicial

El workflow `Deploy Model` solo se podía ejecutar manualmente mediante `workflow_dispatch`.

### Mejora detectada

Para que el flujo estuviera más alineado con una práctica DevOps, se decidió automatizar el despliegue tras la finalización correcta del workflow `Build Model`.

### Solución aplicada

Se modificó `.github/workflows/deploy.yml` para añadir un trigger `workflow_run` que escucha la finalización del workflow `Build Model` en la rama `main`.

El deploy solo se ejecuta automáticamente si `Build Model` termina con estado `success`.

### Resultado

El flujo queda como:

```text
PR → Integration → Review → Merge a main → Build Model → Deploy Model → Render

```

---
