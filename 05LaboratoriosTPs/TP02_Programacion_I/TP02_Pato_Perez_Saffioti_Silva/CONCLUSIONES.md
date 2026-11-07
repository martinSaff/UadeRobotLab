# Conclusiones, Reflexiones y Cierre del Proyecto

**Integrantes del Equipo:** 
- Fabricio Pato  
- Lautaro Pérez  
- Martín Saffioti  
- Nicolás Silva  

---

## 1. Balance del Equipo y Nivel Alcanzado
El trabajo en equipo permitió desarrollar un script de control estable y tolerante a fallos para el Unitree Go2. La división de tareas facilitó la correcta organización de los archivos de código, la documentación y la recolección de evidencias.

### Nivel Alcanzado: Nivel 10
Se cumplieron la totalidad de los requerimientos de la cátedra:
1. Configuración y validación del entorno de desarrollo.
2. Manejo defensivo de excepciones y validación estricta de tipos de datos.
3. Simulación funcional del gemelo digital en MuJoCo.
4. Organización y entrega de la documentación según el Punto 18.

---

## 2. Reflexión y Cierre (Punto 20)

**a) ¿Cuál fue la principal dificultad de instalación?**  
La principal dificultad estuvo en la gestión de dependencias del entorno, como el fallo de importación generado por MuJoCo al inicio.

**b) ¿Qué error requirió mayor investigación?**  
El error `ModuleNotFoundError` al intentar cargar la librería de MuJoCo fue el más complejo de resolver, ya que requirió revisar la configuración del intérprete de Python.

**c) ¿Qué solución resultó efectiva y por qué?**  
La solución efectiva fue la reinstalación de los paquetes vía pip y la comprobación mediante el comando de verificación, lo que corrigió las rutas de las librerías.

**d) ¿Qué intento no funcionó y qué aprendieron de él?**  
Intentar ejecutar el script de control sin antes verificar el estado del entorno virtual. Aprendimos la importancia de validar el entorno de trabajo como paso previo a la ejecución.

**e) ¿Qué diferencia encontraron entre una guía antigua y la arquitectura actual?**  
Las guías antiguas requerían configuraciones manuales y librerías globales propensas a errores, mientras que la arquitectura actual utiliza entornos virtuales y herramientas de simulación estandarizadas.

**f) ¿Hasta qué nivel lograron avanzar?**  
Alcanzamos el Nivel 10, completando tanto la lógica del programa como la estructura de documentación requerida.

**g) Si tuvieran que continuar trabajando, ¿cuál sería el próximo paso?**  
El siguiente paso sería implementar trayectorias autónomas más complejas e integrar la lectura de los sensores del robot en la simulación.