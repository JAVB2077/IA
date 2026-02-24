import networkx as nx
import matplotlib.pyplot as plt

def crear_red_pokemon():
    G = nx.DiGraph()

    # Jerarquía (clases / tipos generales)
    jerarquia = [
        ("Pokemon", "Ser_Vivo"),
        ("Tipo", "Categoria"),
        ("Zona", "Lugar")
    ]

    # Instancias: 20 pokémon + tipos + zonas (cada tupla: (nombre, clase))
    instancias = [
        # Pokémons (20)
        ("Charmander", "Pokemon"),
        ("Vulpix", "Pokemon"),
        ("Growlithe", "Pokemon"),
        ("Squirtle", "Pokemon"),
        ("Magikarp", "Pokemon"),
        ("Psyduck", "Pokemon"),
        ("Bulbasaur", "Pokemon"),
        ("Oddish", "Pokemon"),
        ("Bellsprout", "Pokemon"),
        ("Pikachu", "Pokemon"),
        ("Magnemite", "Pokemon"),
        ("Pidgey", "Pokemon"),
        ("Hoothoot", "Pokemon"),
        ("Geodude", "Pokemon"),
        ("Onix", "Pokemon"),
        ("Sandshrew", "Pokemon"),
        ("Caterpie", "Pokemon"),
        ("Scyther", "Pokemon"),
        ("Abra", "Pokemon"),
        ("Jynx", "Pokemon"),

        # Tipos
        ("Fuego", "Tipo"),
        ("Agua", "Tipo"),
        ("Planta", "Tipo"),
        ("Electrico", "Tipo"),
        ("Volador", "Tipo"),
        ("Roca", "Tipo"),
        ("Tierra", "Tipo"),
        ("Bicho", "Tipo"),
        ("Psiquico", "Tipo"),
        ("Hielo", "Tipo"),

        # Zonas de spawn
        ("Volcan", "Zona"),
        ("Cueva", "Zona"),
        ("Rio", "Zona"),
        ("Mar", "Zona"),
        ("Bosque", "Zona"),
        ("Pradera", "Zona"),
        ("Montana", "Zona"),
        ("Ciudad", "Zona"),
        ("Playa", "Zona"),
        ("Lago", "Zona"),
        ("Desierto", "Zona"),
        ("Ruinas", "Zona"),
        ("Tundra", "Zona")
    ]

    # Relaciones: (sujeto, objeto, accion)
    relaciones = [
        # tipos de cada pokémon
        ("Charmander", "Fuego", "tiene_tipo"),
        ("Vulpix", "Fuego", "tiene_tipo"),
        ("Growlithe", "Fuego", "tiene_tipo"),
        ("Squirtle", "Agua", "tiene_tipo"),
        ("Magikarp", "Agua", "tiene_tipo"),
        ("Psyduck", "Agua", "tiene_tipo"),
        ("Bulbasaur", "Planta", "tiene_tipo"),
        ("Oddish", "Planta", "tiene_tipo"),
        ("Bellsprout", "Planta", "tiene_tipo"),
        ("Pikachu", "Electrico", "tiene_tipo"),
        ("Magnemite", "Electrico", "tiene_tipo"),
        ("Pidgey", "Volador", "tiene_tipo"),
        ("Hoothoot", "Volador", "tiene_tipo"),
        ("Geodude", "Roca", "tiene_tipo"),
        ("Onix", "Roca", "tiene_tipo"),
        ("Sandshrew", "Tierra", "tiene_tipo"),
        ("Caterpie", "Bicho", "tiene_tipo"),
        ("Scyther", "Bicho", "tiene_tipo"),
        ("Abra", "Psiquico", "tiene_tipo"),
        ("Jynx", "Hielo", "tiene_tipo"),

        # zonas de spawn / aparición
        ("Charmander", "Volcan", "spawnea_en"),
        ("Vulpix", "Volcan", "spawnea_en"),
        ("Growlithe", "Pradera", "spawnea_en"),
        ("Squirtle", "Lago", "spawnea_en"),
        ("Magikarp", "Mar", "spawnea_en"),
        ("Psyduck", "Lago", "spawnea_en"),
        ("Bulbasaur", "Bosque", "spawnea_en"),
        ("Oddish", "Bosque", "spawnea_en"),
        ("Bellsprout", "Pradera", "spawnea_en"),
        ("Pikachu", "Ciudad", "spawnea_en"),
        ("Magnemite", "Ciudad", "spawnea_en"),
        ("Pidgey", "Pradera", "spawnea_en"),
        ("Hoothoot", "Bosque", "spawnea_en"),
        ("Geodude", "Montana", "spawnea_en"),
        ("Onix", "Cueva", "spawnea_en"),
        ("Sandshrew", "Desierto", "spawnea_en"),
        ("Caterpie", "Bosque", "spawnea_en"),
        ("Scyther", "Pradera", "spawnea_en"),
        ("Abra", "Ruinas", "spawnea_en"),
        ("Jynx", "Tundra", "spawnea_en")
    ]

    # Agregar jerarquía (ES_UN)
    for hijo, padre in jerarquia:
        G.add_edge(hijo, padre, relation="ES_UN")

    # Agregar instancias
    for individuo, clase in instancias:
        G.add_edge(individuo, clase, relation="ES_UNA_INSTANCIA")

    # Agregar relaciones adicionales
    for sujeto, objeto, accion in relaciones:
        G.add_edge(sujeto, objeto, relation=accion)

    return G

if __name__ == "__main__":
    print("Creando red semantica de Pokémons (20 nodos de especie)...")
    red = crear_red_pokemon()
    plt.figure(figsize=(16,12))
    pos = nx.spring_layout(red, k=0.9, iterations=80, seed=42)
    nx.draw(red, pos,
            with_labels=True,
            node_size=1200,
            node_color="lightblue",
            font_size=8,
            font_weight="bold",
            edge_color="gray",
            arrowsize=12)
    edge_labels = nx.get_edge_attributes(red, 'relation')
    nx.draw_networkx_edge_labels(red, pos, edge_labels=edge_labels, font_color='red', font_size=7)
    plt.title("Red Semántica: Pokémons, Tipos y Zonas de Spawn")
    plt.axis('off')
    plt.show()