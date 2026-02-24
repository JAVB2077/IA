import json

def cargar_base_conocimiento(ruta):
    with open(ruta, 'r',encoding='utf-8') as archivo:
        return json.load(archivo)

def aplicar_reglas_inferencia(kb):
    print("Iniciando motor de inferencia avanzado/...")
    individuos = kb["individuos"]
    inferencias = kb["conocimiento_inferido"]
