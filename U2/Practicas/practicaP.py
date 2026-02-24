import networkx as nx
import matplotlib.pyplot as plt

def crear_red_pokemon():
    G = nx.DiGraph()
    
    jerarquia =[
        ("Pokemon", "Ser_Vivo"),
        ("Tipo", "Categoria"),
        ("Zona", "Lugar")
    ]

    instancias = [
        # Pokémons 
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
        ("Hielo", "Tipo")
    ]

    relaciones =[
        ("Charmander", "Fuego", "es_de_tipo"),
        ("Vulpix", "Fuego", "es_de_tipo"),
        ("Growlithe", "Fuego", "es_de_tipo"),
        ("Squirtle", "Agua", "es_de_tipo"),
        ("Magikarp", "Agua", "es_de_tipo"),
        ("Psyduck", "Agua", "es_de_tipo"),
        ("Bulbasaur", "Planta", "es_de_tipo"),
        ("Oddish", "Planta", "es_de_tipo"),
        ("Bellsprout", "Planta", "es_de_tipo"),
        ("Pikachu", "Electrico", "es_de_tipo"),
        ("Magnemite", "Electrico", "es_de_tipo"),
        ("Pidgey", "Volador", "es_de_tipo"),
        ("Hoothoot", "Volador", "es_de_tipo"),
        ("Geodude", "Roca", "es_de_tipo"),
        ("Onix", "Roca", "es_de_tipo"),
        ("Sandshrew", "Tierra", "es_de_tipo"),
        ("Caterpie", "Bicho", "es_de_tipo"),
        ("Scyther", "Bicho", "es_de_tipo"),
        ("Abra", "Psiquico", "es_de_tipo"),
        ("Jynx", "Hielo", "es_de_tipo")
    ]

    for hijo, padre in jerarquia:
        G.add_edge(hijo, padre, relation="ES_UN")

    for individuo, clase in instancias:
        G.add_edge(individuo, clase, relation="ES_UNA_INSTANCIA")

    for sujeto, objeto, accion in relaciones:
        G.add_edge(sujeto, objeto, relation=accion)
    return G

if __name__ == "__main__":
    print("Creando red semantica Pokémon")
    red = crear_red_pokemon()
    plt.figure(figsize=(14,10))
    pos = nx.spring_layout(red, k=0.7, iterations=42)
    nx.draw(red, pos, with_labels=True, node_size=2500, node_color="lightblue", font_size=9, font_weight="bold", edge_color="gray", arrowsize=15)
    edge_labels = nx.get_edge_attributes(red, 'relation')
    nx.draw_networkx_edge_labels(red, pos, edge_labels=edge_labels, font_color='orange', font_size=8)
    plt.title("Red Semantica: Pokemon")
    plt.axis('off')
    plt.show()