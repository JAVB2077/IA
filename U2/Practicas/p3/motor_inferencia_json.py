import json

def cargar_base_conocimiento(ruta):
    with open(ruta, 'r',encoding='utf-8') as archivo:
        return json.load(archivo)
    
def razonador_logico(kb):
    print("Iniciando motor de inferencia...")
    individuos = kb["individuos"]
    inferencias = kb["conocimiento_inferido"]

#Recorrido
    for nombre, datos in individuos.items():
        #tiene padres esta persona?
        if "padres" in datos and len(datos["padres"]) == 2:
            padre1_nombre = datos["padres"][0]
            padre2_nombre = datos["padres"][1]

            padre1_datos = individuos.get(padre1_nombre, {})
            padre2_datos = individuos.get(padre2_nombre, {})

            #Verificamos si estan casados
            casados = False
            if padre1_datos.get("esposa") == padre2_nombre or padre1_nombre.get("esposo") == padre2_nombre:
                casados = True
            elif padre2_datos.get("esposa") == padre1_nombre or padre2_datos.get("esposo") == padre1_nombre:
                casados = True
            #INFERENCIA
            if casados:
                inferencias[nombre] = {
                    "nueva_clase": "HijoDeMatrimonio",
                    "razon": f"Se dedujo por que sus padres {padre1_nombre} y {padre2_nombre} son esposos",
                }
                print(f"Inferencia en contrada para: {nombre}")
    return kb

def main():
    archivo_json = "ontologia.json"

    #cargar base de conocimiento
    base_conocimiento = cargar_base_conocimiento(archivo_json)
    print("Conocimiento Explicito Inicial")
    print(json.dumps(base_conocimiento, indent=2))
    print("\n-----------------------------------\n")

    #inferencia 
    kb_actualizada = razonador_logico(base_conocimiento)

    #resultado
    print("\nConocimiento Inferido")
    print(json.dumps(kb_actualizada, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()