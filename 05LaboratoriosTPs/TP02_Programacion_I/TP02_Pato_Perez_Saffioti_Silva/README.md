# TP02 - Gemelo Digital y Control de Navegación del Unitree Go2
**Integrantes del Equipo:** 
- Fabricio Pato  
- Lautaro Pérez  
- Martín Saffioti  
- Nicolás Silva  

**Materia:** Programación I / Laboratorio de Robótica  
**Nivel alcanzado:** Nivel 10  

## Descripción
Proyecto de simulación y control en entorno digital (MuJoCo) para el robot cuadrúpedo Unitree Go2. Implementación de controladores defensivos, validación de tuplas de movimiento, manejo de excepciones de seguridad y generación de reportes de ejecución.

## Estructura del Proyecto
- `codigo/`: Contiene el script principal del controlador (`tp02_pato_perez_saffioti_silva.py`).
- `evidencias/`: Carpeta contenedora de las 6 subcarpetas con capturas y explicaciones del proceso:
  - `01_entorno/`: Verificación inicial de herramientas y versiones.
  - `02_instalacion/`: Configuración de librerías del simulador.
  - `03_errores/`: Registro de excepciones críticas (ej. `ModuleNotFoundError`).
  - `04_soluciones/`: Aplicación de correcciones técnicas.
  - `05_gemelo_digital/`: Renderizado y pruebas del robot en MuJoCo.
  - `06_misiones/`: Ejecución de trayectorias y reportes de consola.
- `BITACORA.md`: Registro cronológico del desarrollo.
- `PROBLEMAS.md`: Análisis técnico de errores y soluciones.
- `CONCLUSIONES.md`: Evaluación final del sistema.

## Instrucciones de Ejecución
1. Iniciar el simulador MuJoCo ejecutando el lanzador del entorno y seleccionando el modelo Go2.
2. Ejecutar el script principal desde la terminal del repositorio:
   ```bash
   python TP02_Pato_Perez_Saffioti_Silva/codigo/tp02_pato_perez_saffioti_silva.py