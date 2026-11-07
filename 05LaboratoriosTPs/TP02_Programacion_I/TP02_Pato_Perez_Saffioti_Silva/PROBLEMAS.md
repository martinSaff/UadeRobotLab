# Registro de Problemas y Soluciones Técnicas

## Problema 1: Ausencia del Módulo MuJoCo (`evidencias/03_errores/`)
- **Síntoma:** Interrupción de la ejecución con el mensaje `ModuleNotFoundError: No module named 'mujoco'`.
- **Causa Raíz:** Falta de registro de la librería en el intérprete de Python activo al momento de levantar el simulador.
- **Hipótesis del Equipo:** La librería no se encontraba instalada en el entorno virtual o requería actualización explícita por pip.
- **Solución Aplicada (`evidencias/04_soluciones/`):** Reinstalación de paquetes y validación con los scripts provistos por la cátedra.
- **Resultado:** Carga correcta de las librerías gráficas.

## Problema 2: Entrada de Datos Inválidos en Consola
- **Síntoma:** Posible bloqueo del flujo ante ingresos de parámetros erróneos por parte del usuario.
- **Solución Aplicada:** Uso del bucle defensivo con la sentencia `continue` para omitir comandos erróneos sin interrumpir la ejecución global del robot.