# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  .....................................
#  Comision:           .....................................
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO, MISION_PROPIA, MISIONES


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    # TU CODIGO ACA
    if type(comando) != tuple or len(comando) == 0:
        return False

    accion = comando[0]

    if accion in ("detenerse", "saludar"):
        return len(comando) == 1

    if accion in ("avanzar", "girar"):
        if len(comando) != 3:
            return False
        
        _, velocidad, tiempo = comando

        es_num_vel = (type(velocidad) == int or type(velocidad) == float)
        es_num_tiempo = (type(tiempo) == int or type(tiempo) == float)

        if not es_num_vel or not es_num_tiempo:
            return False

        if tiempo < 0:
            return False

        return True

    return False


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    # TU CODIGO ACA
    accion = comando[0]

    try:
        if accion == "avanzar":
            _, velocidad, tiempo = comando
            robot.avanzar(velocidad=velocidad, tiempo=tiempo)
        elif accion == "girar":
            _, velocidad, tiempo = comando
            robot.girar(velocidad=velocidad, tiempo=tiempo)
        elif accion == "detenerse":
            robot.detenerse()
        elif accion == "saludar":
            robot.saludar()
        else:
            return f"Comando desconocido: {accion}"
        
        return "OK"
    
    except ErrorDeSeguridad as e:
        return f"Rechazado por seguridad: {e}"
    except Exception as e:
        return f"Error de ejecución: {e}"


# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.
    """
    # TU CODIGO ACA
    print(f"\n--- Iniciando ejecución de misión ({len(mision)} comandos) ---")

    for comando in mision:
        if not comando_es_valido(comando):
            motivo = f"Comando inválido por sintaxis o parámetros erróneos: {comando}"
            print(f"[OMITIDO] {motivo}")
            historial.append({
                "comando": comando,
                "valido": False,
                "ejecutado": False,
                "motivo": motivo
            })
            continue

        resultado = ejecutar_comando(robot, comando)

        if resultado == "OK":
            print(f"[EJECUTADO] {comando}")
            historial.append({
                "comando": comando,
                "valido": True,
                "ejecutado": True,
                "motivo": ""
            })
        else:
            print(f"[RECHAZADO] {comando} -> {resultado}")
            historial.append({
                "comando": comando,
                "valido": True,
                "ejecutado": False,
                "motivo": resultado
            })

    print("--- Misión finalizada ---\n")


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    # TU CODIGO ACA
    total = len(historial)
    ejecutados_bien = 0
    for h in historial:
        if h["ejecutado"]:
            ejecutados_bien += 1

    rechazados = total - ejecutados_bien

    print("=====================================")
    print("         REPORTE FINAL DE MISIÓN")
    print("=====================================")
    print(f" Total de comandos procesados : {total}")
    print(f" Ejecutados correctamente     : {ejecutados_bien}")
    print(f" Rechazados / Omitidos        : {rechazados}")
    print("-------------------------------------")
    print(" Detalle de anomalías / rechazos:")
    
    hubo_rechazos = False
    i = 1
    for h in historial:
        if not h["ejecutado"]:
            hubo_rechazos = True
            print(f"  {i}. Comando: {h['comando']}")
            print(f"     Motivo : {h['motivo']}")
            i += 1

    if not hubo_rechazos:
        print("  (Ninguno. Todos los comandos se ejecutaron con éxito).")
    print("=====================================")


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        print("=====================================")
        print("     SELECCIÓN DE MISIÓN - GO2")
        print("=====================================")
        print("Misiones disponibles:")
        print("  - basica")
        print("  - cuadrado")
        print("  - errores")
        print("  - larga")
        print("-------------------------------------")
        
        opcion = input("Escribí el nombre de la misión que querés ejecutar: ").strip().lower()

        if opcion in MISIONES:
            mision_elegida = MISIONES[opcion]
            print(f"\nCargando misión '{opcion}'...")
            
            ejecutar_mision(robot, mision_elegida, historial)
            generar_reporte(historial)
        else:
            print(f"\n[ERROR] La misión '{opcion}' no es válida o no existe.")

    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
