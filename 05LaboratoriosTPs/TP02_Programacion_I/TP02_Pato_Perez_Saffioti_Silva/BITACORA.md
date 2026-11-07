# Bitácora de Desarrollo - TP02

## Etapa 1: Verificación del Entorno (`evidencias/01_entorno/`)
- Revisión conjunta del equipo sobre los requisitos del entorno, versión de Python 3.x, pip y Git.
- Validación inicial del sistema operativo y dependencias base.

## Etapa 2: Diagnóstico y Resolución de Errores (`evidencias/02_instalacion/` y `03_errores/`)
- Detección de la excepción crítica `ModuleNotFoundError: No module named 'mujoco'` al intentar inicializar el simulador.
- Análisis de la causa raíz vinculada a las dependencias de Python y el entorno virtual.

## Etapa 3: Aplicación de Soluciones y Control (`evidencias/04_soluciones/`)
- Ejecución de la reinstalación y actualización mediante gestores de paquetes.
- Verificación exitosa del entorno mediante el comando de revisión.

## Etapa 4: Desarrollo del Código y Gemelo Digital (`evidencias/05_gemelo_digital/` y `codigo/tp02_pato_perez_saffioti_silva.py`)
- Implementación de la función de validación de comandos utilizando la función `type()`.
- Estructuración de la excepción personalizada `ErrorDeSeguridad` y el bucle defensivo con `continue`.

## Etapa 5: Ejecución de Misiones y Reportes (`evidencias/06_misiones/`)
- Prueba de misiones de navegación en el gemelo digital de MuJoCo.
- Generación de métricas finales de comandos procesados y rechazados por consola.