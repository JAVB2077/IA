import json

def cargar_base_conocimiento(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def aplicar_reglas_inferencia_pokemon(kb):
    print("Iniciando motor de inferencia Pokémon...")
    individuos = kb["individuos"]

    # Inicializamos las listas de inferencias para cada individuo
    inferencias = {nombre: {"equipo_pokemon": [],"evolucion_fase_2": [],"compatriotas": [],
                            "colegas_profesion_o_bando": [],"comparte_tipo": []} for nombre in individuos}

    for sujeto, datos_sujeto in individuos.items():
        # Extracción de datos clave del sujeto
        region_sujeto = datos_sujeto.get("region_origen")
        profesion_sujeto = datos_sujeto.get("profesion")
        afiliacion_sujeto = datos_sujeto.get("afiliacion")
        tipos_sujeto = set(datos_sujeto.get("tipos_elementales", []))
        entrenador_sujeto = datos_sujeto.get("entrenador")
        evolucion_directa = datos_sujeto.get("evolucion")

        # 1. Inferencia Inversa: Equipo Pokémon
        # Si este individuo es un Pokémon y tiene entrenador, lo agregamos al equipo del entrenador
        if entrenador_sujeto and entrenador_sujeto in individuos:
            if sujeto not in inferencias[entrenador_sujeto]["equipo_pokemon"]:
                inferencias[entrenador_sujeto]["equipo_pokemon"].append(sujeto)

        # 2. Inferencia Transitiva: Evolución de Fase 2
        # Si A evoluciona a B, y B evoluciona a C -> C es la fase 2 de A
        if evolucion_directa and evolucion_directa in individuos:
            evo_fase_2 = individuos[evolucion_directa].get("evolucion")
            if evo_fase_2:
                if evo_fase_2 not in inferencias[sujeto]["evolucion_fase_2"]:
                    inferencias[sujeto]["evolucion_fase_2"].append(evo_fase_2)

        # 3. Comparaciones 1 a 1 con otros individuos
        for otro, datos_otro in individuos.items():
            if sujeto == otro:
                continue

            # Inferencia: Compatriotas (Misma región)
            region_otro = datos_otro.get("region_origen")
            if region_sujeto and region_sujeto == region_otro:
                if otro not in inferencias[sujeto]["compatriotas"]:
                    inferencias[sujeto]["compatriotas"].append(otro)

            # Inferencia: Colegas de Profesión o Bando (Misma profesión o afiliación)
            profesion_otro = datos_otro.get("profesion")
            afiliacion_otro = datos_otro.get("afiliacion")
            
            comparte_profesion = profesion_sujeto and profesion_sujeto == profesion_otro
            comparte_afiliacion = afiliacion_sujeto and afiliacion_sujeto == afiliacion_otro
            
            if comparte_profesion or comparte_afiliacion:
                if otro not in inferencias[sujeto]["colegas_profesion_o_bando"]:
                    inferencias[sujeto]["colegas_profesion_o_bando"].append(otro)

            # Inferencia: Comparten tipo elemental (Intersección de conjuntos)
            tipos_otro = set(datos_otro.get("tipos_elementales", []))
            if tipos_sujeto and tipos_otro and not tipos_sujeto.isdisjoint(tipos_otro):
                if otro not in inferencias[sujeto]["comparte_tipo"]:
                    inferencias[sujeto]["comparte_tipo"].append(otro)

    # Limpieza: Eliminamos listas vacías para que el JSON quede limpio
    inferencias_limpias = {}
    for individuo, deducciones in inferencias.items():
        deducciones_filtradas = {k: v for k, v in deducciones.items() if len(v) > 0}
        if deducciones_filtradas:
            inferencias_limpias[individuo] = deducciones_filtradas

    # Guardamos el conocimiento inferido en la base de conocimiento
    kb["conocimiento_inferido"] = inferencias_limpias
    return kb
    
def main():
    # Asegúrate de que el nombre coincida con tu archivo JSON guardado
    archivo_json = 'ontologia4.json' 

    try:
        base_conocimiento = cargar_base_conocimiento(archivo_json)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_json}. Asegúrate de guardarlo en el mismo directorio.")
        return

    kb_actualizada = aplicar_reglas_inferencia_pokemon(base_conocimiento)

    print("======================================================")
    print("Conocimiento Inferido: (Nuevos hechos descubiertos)")
    print("======================================================")
    print(json.dumps(kb_actualizada["conocimiento_inferido"], indent=4, ensure_ascii=False))

    with open('ontologia_inferida.json', 'w', encoding='utf-8') as f:
        json.dump(kb_actualizada, f, indent=4, ensure_ascii=False)
    print(f"\nConocimiento inferido guardado exitosamente en 'ontologia_inferida.json'")

if __name__ == "__main__":
    main()