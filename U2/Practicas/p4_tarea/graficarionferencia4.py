import networkx as nx
import matplotlib.pyplot as plt
import json

def cargar_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def generar_grafo():
    # Asegúrate de usar el archivo generado por el script de inferencia
    try:
        kb = cargar_json('ontologia_inferida.json')
    except FileNotFoundError:
        print("Error: No se encontró 'pokemon_ontologia_inferida.json'. Ejecuta primero el motor de inferencia.")
        return

    G = nx.DiGraph()

    # Corrección del error tipográfico: "individuoa" -> "individuos"
    individuos = kb.get("individuos", {})
    inferidos = kb.get("conocimiento_inferido", {})

    # 1. Crear Nodos (Entrenadores, Pokémon, Organizaciones, Regiones)
    for nombre in individuos.keys():
        G.add_node(nombre)

    # 2. Relaciones Explícitas (Del JSON original)
    for sujeto, datos in individuos.items():
        # Relaciones directas simples
        if "entrenador" in datos:
            G.add_edge(sujeto, datos["entrenador"], relation="entrenador", tipo="explicito")
        if "evolucion" in datos:
            G.add_edge(sujeto, datos["evolucion"], relation="evoluciona_a", tipo="explicito")
        if "pre_evolucion" in datos:
            G.add_edge(sujeto, datos["pre_evolucion"], relation="evoluciona_de", tipo="explicito")
        if "rival" in datos:
            G.add_edge(sujeto, datos["rival"], relation="rival_de", tipo="explicito")
        if "abuelo" in datos:
            G.add_edge(sujeto, datos["abuelo"], relation="nieto_de", tipo="explicito")
        if "nieto" in datos:
            G.add_edge(sujeto, datos["nieto"], relation="abuelo_de", tipo="explicito")
        if "lider" in datos:
            G.add_edge(sujeto, datos["lider"], relation="liderado_por", tipo="explicito")
        
        # Relaciones en listas (amigos, compañeros)
        for amigo in datos.get("amigos", []):
            G.add_edge(sujeto, amigo, relation="amigo_de", tipo="explicito")
        for compañero in datos.get("compañeros", []):
            G.add_edge(sujeto, compañero, relation="compañero_de", tipo="explicito")

    # 3. Relaciones Inferidas (Del motor de inferencia)
    for sujeto, deducciones in inferidos.items():
        for tipo_relacion, lista_nombres in deducciones.items():
            for nombre_inferido in lista_nombres:
                # Corrección: Se quitó las comillas para usar el valor de la variable
                G.add_edge(sujeto, nombre_inferido, relation=tipo_relacion, tipo="inferido")

    # ----- DIBUJAR GRAFO -------
    print("Generando imagen de la red Pokémon...")
    plt.figure(figsize=(20, 14)) # Tamaño un poco más grande por la cantidad de nodos

    # Layout: Ajusta k para separar los nodos si se amontonan
    pos = nx.spring_layout(G, k=1.8, iterations=80, seed=42)
    
    # Nodos (Colores temáticos de Pokémon: Rojo Pokeball o Amarillo)
    nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='#ffcb05', edgecolors='#3b4cca', linewidths=2)
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

    # Separar aristas por tipo
    aristas_explicitas = [(u, v) for u, v, d in G.edges(data=True) if d['tipo'] == 'explicito']
    aristas_inferidas = [(u, v) for u, v, d in G.edges(data=True) if d['tipo'] == 'inferido']

    # Flechas Explícitas (Grises)
    nx.draw_networkx_edges(G, pos, edgelist=aristas_explicitas, edge_color='gray',
                           arrows=True, arrowsize=15, connectionstyle='arc3, rad=0.1')
    
    # Flechas Inferidas (Rojas y punteadas)
    nx.draw_networkx_edges(G, pos, edgelist=aristas_inferidas, edge_color='red', style='dashed',
                           arrows=True, arrowsize=15, connectionstyle='arc3, rad=0.2')
    
    # Etiquetas de las relaciones
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, font_color='darkblue')

    # Leyenda
    plt.plot([], [], color='gray', label='Relación Explícita (JSON Original)')
    plt.plot([], [], color='red', linestyle='dashed', label='Relación Inferida (Motor IA)')
    plt.legend(loc='upper left', fontsize=12)

    plt.title("Red Semántica Pokémon: Conocimiento Explícito vs Inferido", fontsize=18, fontweight='bold', color='#3b4cca')
    plt.axis('off')

    nombre_archivo = "grafo_pokemon_inferencia.png"
    plt.savefig(nombre_archivo, bbox_inches='tight', dpi=200) # Mayor DPI para que el texto se lea mejor
    print(f"¡Listo! La imagen ha sido guardada como: {nombre_archivo}")

if __name__ == "__main__":
    generar_grafo()