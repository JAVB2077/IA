import json

def cargar_base_Alpha(ruta):
    with open(ruta, 'r',encoding='utf-8') as archivo:
        return json.load(archivo)
    
def razonador_logico_Alpha(kb):
    print("Iniciando motor de inferencia Alpha...")
    individuos = kb["individuos"]
    inferencias = kb["conocimiento_inferido"]

    for nombre, datos in individuos.items():
        # 1. ¿Este individuo está intentando entrar a algún lugar?
        if "intento_entrar_a" in datos:
            destino_nombre = datos["intento_entrar_a"]
            datos_destino = individuos.get(destino_nombre)

            if datos_destino:
                # Extraemos los niveles (usando 0 como default si no existen)
                nivel_usuario = datos.get("nivel_seguridad", 0)
                nivel_minimo = datos_destino.get("nivel_requerido", 0)

                # 2. COMPARACIÓN LÓGICA
                if nivel_usuario >= nivel_minimo:
                    inferencias[nombre] = {
                        "estado": "AccesoPermitido",
                        "razon": f"Nivel {nivel_usuario} es suficiente para el requisito de {nivel_minimo} en {destino_nombre}"
                    }
                else:
                    inferencias[nombre] = {
                        "estado": "ALERTA_SEGURIDAD",
                        "razon": f"Nivel {nivel_usuario} es insuficiente para entrar a {destino_nombre} (Mínimo: {nivel_minimo})"
                    }
    return kb
def main():
    archivo_json = "ontologia_Alpha2.json"

    #cargar base de conocimiento
    base_conocimiento = cargar_base_Alpha(archivo_json)
    print("Conocimiento Explicito Inicial")
    print(json.dumps(base_conocimiento, indent=2))
    print("\n-----------------------------------\n")

    #inferencia
    kb_actualizada = razonador_logico_Alpha(base_conocimiento)

    #resultado
    print("\nConocimiento Inferido")
    print(json.dumps(kb_actualizada, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()